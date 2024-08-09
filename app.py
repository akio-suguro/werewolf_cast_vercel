from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    roles = ['人狼'] * 3 + ['狂人'] * 1 + ['占い師'] * 1 + ['霊能'] * 1 + ['騎士'] * 1 + ['村人'] * 6
    players = []
    result = {}
    white_player = None
    message = ""

    if request.method == 'POST':
        players = request.form['players'].strip().split('\n')
        message = players

        # プレイヤー名の入力が1つも無い場合、自動でプレイヤー名を当てて配役する
        if players == ['']:
            players = [f'プレイヤー{i+1}' for i in range(13)]

        if len(players) == 13:
            # レギュ通りに配役
            random.shuffle(players)
            for i, role in enumerate(roles):
                result[players[i]] = role

            # ランダム白の選択
            non_werewolves = [player for player, role in result.items() if role not in ['人狼', '占い師']]
            white_player = random.choice(non_werewolves)

        else:
            result = "プレイヤーの数が13人ではありません。"

    return render_template('index.html',
                           players=players,
                           result=result,
                           white_player=white_player,
                           message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

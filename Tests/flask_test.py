from flask import Flask
from flask import request
import random
import hashlib

app = Flask(__name__)
game = ''


@app.route('/gamestate')
def get_state():
    return "GAME!"

@app.route('/rolldice')
def roll_dice():
    dice1, dice2 = random.randint(1, 6), random.randint(1, 6)
    #update game instance...

    # return dice result
    return str(dice1) + '-' + str(dice2)

@app.route('/buy')
def buy():
    request.args.get('property')
    #update game instance...

    # return success
    return "SUCCESS"

#example for hash
@app.route('/hash')
def hash():
    data = request.args.get('data')
    return hashlib.md5(str(data).encode('utf-8')).digest()


if __name__ == '__main__':
    app.run()
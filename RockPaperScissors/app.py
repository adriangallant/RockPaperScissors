# Make a Rock, Paper, Scissors Program
# I did my own version, then made improvements inspired from (notably dictionary, enums, exceptions)
# https://realpython.com/python-rock-paper-scissors/#play-several-games-in-a-row https://cocalc.com
# https://www.digitalocean.com/community/tutorials/how-to-create-your-first-web-application-using-flask-and-python-3#introduction
from services import GameLogicService as gameLogicService
from markupsafe import escape
from flask import Flask, abort

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def hello():
    return '<h1>Hello, World!</h1>'


@app.route('/about/')
def about():
    return '<h3>This is a Flask web application.</h3>'


@app.route('/capitalize/<word>/')
def capitalize(word):
    return '<h1>{}</h1>'.format(escape(word.capitalize()))


@app.route('/add/<int:n1>/<int:n2>/')
def add(n1, n2):
    return '<h1>{}</h1>'.format(n1 + n2)


@app.route('/users/<int:user_id>/')
def greet_user(user_id):
    users = ['Bob', 'Jane', 'Adam']
    try:
        return '<h2>Hi {}</h2>'.format(users[user_id])
    except IndexError:
        abort(404)


# TODO: ADD DATABASE FOR CPU/PLAYER STAT TRACKING?
# TODO: ADD FRONTEND
# TODO: ADD DISTINCT USER FUNCTIONALITY

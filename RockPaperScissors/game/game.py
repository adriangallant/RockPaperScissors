# https://realpython.com/flask-blueprint/#what-a-flask-application-looks-like
from markupsafe import escape
from flask import Blueprint, render_template, abort, jsonify, request
from database import databaseService as dbService

game_blueprint = Blueprint('game_blueprint', __name__,
                           template_folder='templates',
                           static_folder='static',
                           static_url_path='assets')


@game_blueprint.route('/')
@game_blueprint.route('/rules/')
def rules():
    return render_template('game/rules.html')


@game_blueprint.route('/play/')
def play_game():
    return render_template('game/play_game.html')


@game_blueprint.route('/insertResult/', methods=['POST'])
def insert_result():
    game_result = request.json
    try:
        dbService.insert_result(game_result)
        return jsonify('Game recorded successfully!')
    except IndexError:
        abort(404)


#############################
#############################
# TEST ROUTES BELOW
#############################
#############################


@game_blueprint.route('/about/')
def about():
    return '<h3>This is a Flask web application.</h3>'


@game_blueprint.route('/capitalize/<word>/')
def capitalize(word):
    return '<h1>{}</h1>'.format(escape(word.capitalize()))


@game_blueprint.route('/add/<int:n1>/<int:n2>/')
def add(n1, n2):
    return '<h1>{}</h1>'.format(n1 + n2)


@game_blueprint.route('/users/<int:user_id>/')
def greet_user(user_id):
    users = ['Bob', 'Jane', 'Adam']
    try:
        return '<h2>Hi {}</h2>'.format(users[user_id])
    except IndexError:
        abort(404)

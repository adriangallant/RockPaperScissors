# Make a Rock, Paper, Scissors Program
# I did my own version, then made improvements inspired from (notably dictionary, enums, exceptions)
# https://realpython.com/python-rock-paper-scissors/#play-several-games-in-a-row https://cocalc.com
# https://www.digitalocean.com/community/tutorials/how-to-create-your-first-web-application-using-flask-and-python-3#introduction
from flask import Flask, render_template
from game.game import game_blueprint
from authentication.authentication import authentication_blueprint

app = Flask(__name__)
app.register_blueprint(authentication_blueprint, url_prefix='/')
app.register_blueprint(game_blueprint, url_prefix='/game')

# TODO: ADD DATABASE FOR CPU/PLAYER STAT TRACKING?
# TODO: ADD FRONTEND
# TODO: ADD DISTINCT USER FUNCTIONALITY

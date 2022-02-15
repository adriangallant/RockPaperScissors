from flask import Blueprint, render_template, abort

authentication_blueprint = Blueprint('authentication_blueprint', __name__,
                                     template_folder='templates',
                                     static_folder='static',
                                     static_url_path='assets')


@authentication_blueprint.route('/')
@authentication_blueprint.route('/authentication/')
def introduction_screen():
    return render_template('authentication/start_screen.html')



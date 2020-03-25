from flask import Flask, render_template
#import python_game_code.random_functions
#import python_game_code.rooms
#import python_game_code.runner
#import python_game_code.play
#play = python_game_code.play
def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

        #link is base page
    from . import link
    app.register_blueprint(link.bp)
    @app.route('/')
    def link():
        return render_template('base.html')
    #game is used for playing compared to login


    return app

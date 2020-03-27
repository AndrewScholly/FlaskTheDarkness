from flask import Flask, render_template

import python_game_code.random_functions
import python_game_code.test_value
from . import rooms
# import python_game_code.rooms
# import python_game_code.runner


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

        # link is base page
    from . import link
    app.register_blueprint(link.bp)

    from . import game
    app.register_blueprint(game.bp)

    @app.route('/')
    def link():
        return render_template('index.html')

    @app.route('/game')
    def game():
        room = [
            rooms.room1(),
            rooms.room2(),
            rooms.room3(),
            rooms.room4(),
            rooms.room5()
        ]
        scenes = [
            rooms.room1_scene1(),
            rooms.room2_scene1(),
            rooms.room3_scene1(),
            rooms.room4_scene1(),
            rooms.room5_scene1()
        ]
        x = python_game_code.random_functions.random_number()
        y = python_game_code.random_functions.random_scene()
        current_room = room[x]
        text = current_room.which_room
        current_scene = scenes[x]
        more_text = current_scene.choices()
        return render_template('game.html', room=text, scene=more_text)

    return app

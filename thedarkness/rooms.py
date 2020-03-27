from flask import request
import python_game_code.random_functions
class room1(object):
    which_room = "Finding the Sword"
    def choices(self):
        return self.room1_scene1

class room1_scene1(room1):
    def choices(self):
        rocks = [
        'throw rock',
        'throw rocks',
        'throw',
        'rock',
        'rocks',
        'throws'
        'Throw',
        'Throw rock',
        'Throw Rock'
        ]
        return "You enter the corridor, looking around for the sword, when a darkness being jumps out at you! Without any pieces yet, you need to defeat the being somehow without touching him. There are some rocks nearby"
        if request.method == "POST":
            answer = request.form['answer']
            def right_answer():
                for i in rocks:
                    if answer == i:
                        return "You found the sword!"

class room2(object):
    which_room = "Finding the Saber"
    def choices(self):
        return self.room2_scene1

class room2_scene1(room2):
    def choices(self):
        return "You enter room2"


class room3(object):
    which_room = "Finding the Blaster"
    def choices(self):
        return self.room2_scene1

class room3_scene1(room3):
    def choices(self):
        return "You enter room3"



class room4(object):
    which_room = "Finding the Wand"
    def choices(self):
        return self.room3_scene1

class room4_scene1(room4):
    def choices(self):
        return "You enter room4"



class room5(object):
    which_room = "Saving Reality"
    def choices(self):
        return self.room5_scene1

class room5_scene1(room5):
    def choices(self):
        return "You enter room5"

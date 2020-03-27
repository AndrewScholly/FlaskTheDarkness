import python_game_code.random_functions
class room1(object):
    which_room = "Finding the Sword"
    def choices(self):
        return self.room1_scene1

class room1_scene1(room1):
    def choices(self):
        return "You enter room1"


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

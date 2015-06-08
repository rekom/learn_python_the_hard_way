class Scene(object):

    def enter(self):
        pass


class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        pass

class Death(Scene):

    killed = [
    "You are dead, really dead",
    "You fail your mission",
    "Bye, you noob"
    ]

    def enter(self):
        print Death.killed[randint(0, 3)]

class CentralCorridor(Scene):

    def enter(self):
        print "You enter in place with two"
        print "corridors, left and right"
        choice = raw_input("Which one you choose?"> )
        if choice == "left":
            print "You have found a banana!"
            print "You advance and see the Laser Weapon Armory"
            return laser_weapon_armory
        elif choice == "right":
            print "There is an army in front of you"
            print "As they see you the shoot at you"
            print "with megablaster, you can't dodge!"
            return death




class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass


class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

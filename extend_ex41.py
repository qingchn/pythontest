#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import exit
from random import randint

class Game(object):
    def __init__(self,start):
        self.quips = [
            "You died. You kinda suck at this.",
            "Your mom would be proud. If she were smarter.",
            "Such a luser.",
            "I have a small puppy that's better at this."
       ]

        self.start = start

    def play(self):
        """


        """
        next = self.start

        while True:
            print "\n--------"
            room = getattr(self,next)
            next = room()

    def death(self):
        print self.quips[randint(0,len(self.quips)-1)]
        exit(1)

    def central_corridor(self):
        print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
        print "your entire crew. You are the last surviving member and your last"
        print "mission is to get the neutron destruct bomb from the Weapons Armory,"
        print "put it in the bridge, and blow the ship up after getting into an "
        print "escape pod."
        print "\n"
        print "You're running down the central corridor to the Weapons Armory when"
        print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
        print "flowing around his hate filled body. He's blocking the door to the"
        print "Armory and about to pull a weapon to blast you."

        action = raw_input(">")

        if action == "shoot!":
            print "completely ruins his brand new costume his mother bought him, which"
            print "you are dead. Then he eats you."
            return 'death'
        elif action == "dodge!":
            print "your head and eats you."
            return 'death'
        elif action == "tell a joke":
            return 'laser_weapon_armory'
        elif action == 'ok':
            print "you down a tall"
            return 'down_tall'
        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'

    def laser_weapon_armory(self):
        print "You do a dive roll into the Weapon Armory, crouch and scan the room"
        print "for more Gothons that might be hiding. It's dead quiet, too quiet."
        print "You stand up and run to the far side of the room and find the"
        print "get the bomb. The code is 3 digits."
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        print code
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print "BZZZZEDDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code:
            print "The container clicks open and the seal breaks, letting gas out."
            print "You grab the neutron bomb and run as fast as you can to the"
            print "bridge where you must place it in the right spot."
            return 'the_bridge'
        else:
            print "ship from their ship and you die."
            return 'death'


    def the_bridge(self):
        print "arm and don't want to set it off."

        action = raw_input("> ")

        if action == "throw the bomb":
            print "the bomb. You die knowing they will probably blow up when"
            print "it goes off."
            return 'death'
        elif action == "slowly place the bomb":
            print "get off this tin can."
            return 'escape_pod'
        else:
            return "the_bridge"
    def escape_pod(self):
        print "do you take?"
        good_pod = randint(1,5)
        print good_pod
        guess = raw_input("[pod #]> ")

        if int(guess) != good_pod:
            print "You jump into pod %s and hit the eject button." % guess
            return 'death'
        else:
            print "time. You won!"
            exit(0)
    def down_tall(self):
        print "This is a down tall."
        ans = raw_input("are you af?")

        if ans == "yes":
            print "Ok boys,you are good"
            return 'central_corridor'
        else:
            print "you are a bad boys"
            exit(1)



a_game = Game("central_corridor")
a_game.play()








































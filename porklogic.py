# Importing the art lib to make the game title look a little cooler
from art import *
from colored import fg, attr #Importing colored to help color some text
sectionOneloc = False
#Section Zero logic
def sectionZero():
            print("You have just escaped the bacon factory...")
            print("Behind you is the bacon factory, but ahead of you are different paths you can take")
            print("You can go back into the factory and accept your fate, or you start your journey")
            print("Which direction will you go?\n")
            sectionZeroMove = input("Go where?\n")
            if sectionZeroMove == "south": #Setting up a give up condition
                print(fg("red") + "You gave up!?" + attr(0))
                exit()
            elif sectionZeroMove == "west":
                print(fg("red") + "The terrain is too rough, you can't go that way!\n" + attr(0))
            elif sectionZeroMove == "north":
                print("You head north\n")
                sectionTwo() #Calls sectionTwo function to move on to next area
            elif sectionZeroMove == "east":
                print("You head east")
                sectionOne()
            else:
                print(fg("red") + "Try again" + attr(0)) #Adding in the colored lib functions to color text red
#Section One logic
def sectionOne():
    print("You are now in a grass field")
    exit()
#Section Two logic
def sectionTwo():
    print("You are now on a gravel road")
    exit()

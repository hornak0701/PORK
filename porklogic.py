'''
Logic module for the main pork.py file
This will handle all of the map navigation/movement
Will also handle the game over and win conditions
If inventory and combat is added into the game, that will likely be put
in a seperate file and not here
Initial code by coderchameleon
'''
# Library imports
from art import *  # Importing the art lib to make title look cooler
from colored import fg, attr  # Importing colored to help color some text
import time  # Importing this to implement some waits in between prints
# Global variables declared
health = 3  # For tracking Hammy's health
disguise = False  # Checking if Hammy has the bear disguise

# Section Zero logic
def sectionZero():
  print("You have just escaped the bacon factory...")
  time.sleep(1)  # Adding 1 sec wait between some print statements
  print("Behind you is the bacon factory, but ahead of you are", end=" ")
  print("different paths you can take")
  time.sleep(1)
  print("You can go back into the factory and accept your fate,", end=" ")
  print("or you start your journey")
  time.sleep(1)
  # Using the lowercase function below to make input easier to deal with
  sectionZeroMove = input("Which direction do you go?\n").lower()
  # Determine next action based on input
  # South
  if sectionZeroMove == "south":  # Setting up a give up condition
    print(fg("red") + "You gave up!?" + attr(0))
    exit()
  # West
  elif sectionZeroMove == "west":
    print(fg("red") + "The terrain is too rough, you can't go that way!\n" + attr(0))
    sectionZero()
  # North
  elif sectionZeroMove == "north":
    print("You head north...\n")
    sectionTwo()  # Calls sectionTwo function to move to next area
  # East
  elif sectionZeroMove == "east":
    print("You head east...\n")
    sectionOne()
  # Invalid input using the colored library for text color
  else:
    print(fg("red") + "Try again" + attr(0))
    sectionZero()


# Section One logic
def sectionOne():
  print("You are now in a grassy field.")
  print("To your South you see the smoke stacks of the bacon", end=" ")
  print("factory,it would be bad to go that way")
  time.sleep(1)
  print("You see a thick forest to the East.")  # No go direction
  time.wait(1)
  print("To the North you see some rocky hills past the field")
  time.sleep(1)
  sectionOneMove = input("Which direction will you go?\n").lower()
  # Determine next action based on input
  # North (yes I know I was not consistent with the direction)
  if sectionOneMove == "north":
    print("You head north...\n")
    sectionThree()  # Launching section 3 function
  # East
  elif sectionOneMove == "east":
    print("You start to head into the forest...\n")
    print("The trees and brush quickly becomes too thick to pass!\n")
    time.sleep(1)
    print(fg("red") + "The terrain is too rough, you can't go that way!\n" + attr(0))
    sectionOne()
  # South
  elif sectionOneMove == "south":  # Prohibit movement this direction
    print(fg("red") + "That way goes back to the factory, you cannot go that way!\n" + attr(0))
    sectionOne()
  # West
  elif sectionOneMove == "west":  # Prohibit movement back
    print(fg("red") + "You just came from that direction!\n" + attr(0))
    sectionOne()
  # Invalid input
  else:
    print(fg("red") + "Try again" + attr(0))
    sectionOne()


# Section Two logic
def sectionTwo():
  print("You are now on a gravel road")
  print("To your North you see what looks like the edge of a village.")
  time.sleep(1)
  print("To your East you see some rocky hills.")
  time.sleep(1)
  print("South you see where you escaped the factory")
  time.sleep(1)
  # print("To your West you see the edge of a lake.")  # Cut content
  sectionTwoMove = input("Which direction will you go?\n").lower()
  # North
  if sectionTwoMove == "north":
    print("You head north...\n")
    sectionFive()
  # East
  elif sectionTwoMove == "east":
    print("You head east...\n")
    sectionThree()
  # South
  elif sectionTwoMove == "south":
    print(fg("red") + "You just came from that direction!\n" + attr(0))
    sectionTwo()
  # West
  elif sectionTwoMove == "west":
    print(fg("red") + "You cannot go that way right now...\n" + attr(0))
    sectionTwo()
  # Invalid input
  else:
    print(fg("red") + "Try again" + attr(0))
    sectionTwo()


# Section 3 Logic
def sectionThree():
  print("After some time walking through rocky terrain...")
  print("You come to the entrance a dark and damp cave.")
  time.sleep(1)
  print("Inside the cave you hear some grunts and rustling around.")
  time.sleep(1)
  print("To your North you see a cliff with what could be a large drop")
  time.sleep(1)
  print("Moving East will take you into the cave proper.")
  time.sleep(1)
  sectionThreeMove = input("Which direction will you go?\n").lower()
  # North
  if sectionThreeMove == "north":
    print("You head to the north...\n")
    sectionSeven()
  # East
  elif sectionThreeMove == "east":
    print("You make your way into the cave...\n")
    sectionFour()
  # South
  elif sectionThreeMove == "south":
    print(fg("red") + "You just came from that direction!\n" + attr(0))
    sectionThree()
  # West
  elif sectionThreeMove == "west":  # blocking off west to avoid confusion
    print(fg("red") + "You cannot go that way right now...\n" + attr(0))
    sectionThree
# Invalid input
  else:
    print(fg("red") + "Try again" + attr(0))
    sectionThree()


# Section 4 Logic
# TODO tie this section into the combat module
def sectionFour():
  print("Welcome to section four!")
  print("This is a placeholder for the bear fight")
  exit()


# Section 5 Logic
def sectionFive():
  print("You come to the edge of a village.")
  print("There are some sparse buildings near you but more in the distance.")
  time.sleep(1)
  print("If you proceed north into the town you might be spotted.")
  time.sleep(1)
  print("To the east are some cliffs you could not get past.")
  time.sleep(1)
  print("You have enough time to go back to the gravel road.")
  time.sleep(1)
  sectionFiveMove = input("Which direction will you go?\n").lower()
  # North
  if sectionFiveMove == "north":  # Going into win condition section
    print("You head further into the village...\n")
    sectionNine()
  # East
  elif sectionFiveMove == "east":  # Blocking off east
   print(fg("red") + "You cannot go that way right now...\n" + attr(0))
   sectionNine()
  # South
  elif sectionFiveMove == "south":
    print("You head back to the gravel road quickly.")
    sectionTwo()
  # West
  elif sectionFiveMove == "west":
    print(fg("red") + "You cannot go that way right now...\n" + attr(0))
    sectionFive()
  # Invalid Input
  else:
    print(fg("red") + "Try again" + attr(0))
    sectionFive()


'''
This section below is going to be cut for scope purposes

# Section 6 Logic (Cut)
def sectionSix():
  print("Welcome to section six!")
  exit()
'''


# Section 7 Logic
def sectionSeven():  # This is going to cause Hammy 1 HP damage
  global health  # Working with the global health varible
  health -= 1  # Dropping Hammy's health down by 1
  print("As you walk you come toward the edge of a cliff")
  print("You slowly walk foward and look down and see it is steep")
  time.sleep(1)
  print("You decide to slowly start descend down the cliff...")
  time.sleep(3)
  print("Suddenly one of your hoof holds gives way and you fall!")
  time.sleep(1)
  print("You land on a small outcropping a ways down from where you fell.")
  time.sleep(1)
  print(fg("red") + "You are alive but a little hurt" + attr(0))
  print("You decide it is too dangerous and make your way back up the cliff")
  time.sleep(2)
  print("You make it back up okay and set back toward the small cave you came from...\n")
  print(fg("red") + "You walk with a slight limp\n" + attr(0))
  sectionThree()


'''
This section below is going to be cut for scope purposes

# Section 8 Logic (Cut)
def sectionEight():
  print("Welcome to section eight!")
  exit()
'''


# Section 9 Logic
def sectionNine():
  print("You slowly try to sneak further into the village...")
  time.sleep(1)
  print("You carefully try to make your way through without attracting attention")
  time.sleep(3)
  print("You are making good progress until...")
  time.sleep(2)
  # This will be fleshed out more soon and is mostly a placeholder
  # TODO flesh this text out more.
  if disguise == True:
    print("You hear someone shriek \"eek! A bear!\"")
    print("Everyone ran away!")
    time.sleep(2)
    print("Congragulations! You have escaped!")
    exit()
  elif disguise == False:
    print("You hear someone yell, \"Grab that bacon!\"")
    print("You have been caught!\n")
    print("-----------------------")
    time.sleep(3)
    tprint("You are bacon", space=1)
    exit()
  else:  # Error handling just in case
    print("Unhandled error...restarting")
    time.sleep(1)
    print("----------------------------")
    sectionOne()  

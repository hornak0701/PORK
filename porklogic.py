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


# Section Zero logic
def sectionZero():
  print("You have just escaped the bacon factory...")
  print("Behind you is the bacon factory, but ahead of you are", end=" ")
  print("different paths you can take")
  print("You can go back into the factory and accept your fate,", end=" ")
  print("or you start your journey")
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
  print("You see a thick forest to the East.")  # No go direction
  print("To the North you see some rocky hills past the field")
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
  print("To your East you see some rocky hills.")
  print("South you see where you escaped the factory")
  print("To your West you see the edge of a lake.")
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
    print("You head west \n")
    sectionSix()
  # Invalid input
  else:
    print(fg("red") + "Try again" + attr(0))
    sectionTwo()


# Section 3 Logic
def sectionThree():
  print("After some time walking through rocky terrain...")
  print("You come to the entrance a dark and damp cave.")
  print("Inside the cave you hear some grunts and rustling around.")
  print("To your North you see a cliff with what could be a large drop")
  print("Moving East will take you into the cave proper.")
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
def sectionFour():
  print("Welcome to section four!")
  exit()


# Section 5 Logic
def sectionFive():
  print("Welcome to section five!")
  exit()


# Section 6 Logic
def sectionSix():
  print("Welcome to section six!")
  exit()


# Section 7 Logic
def sectionSeven():
  print("Welcome to section seven!")
  exit()


# Section 8 Logic
def sectionEight():
  print("Welcome to section eight!")
  exit()


# Section 9 Logic
def sectionNine():
  print("Welcome to section nine!")
  exit()

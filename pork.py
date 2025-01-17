'''
Pork, a Zork like game about a pig named Hammy
This is the main file which starts and runs the game itself
Map movement is done through a seperate file name porklogic.py
Initial code by coderchameleon
'''
# Library imports
from art import *  # Importing the art lib to make the game title look a little cooler
from colored import fg, attr  # Importing colored to help color some text
import porklogic  # Importing functions from game logic file
import time  # Importing to start adding in waits between print statements
tprint("PORK", space=3)  # Printing the game title, using tprint to make it look fancy
health = 3  # Making this a global variable so it can be touched by all functions if needed
# Creating master function to run game
def runGame():
  # Intro text
  print("You are named Hammy\n")
  print("You are a pig and you must make your way through the forest.\n")
  print("You do not have time to backtrack so choose wisely!\n")
  print("Don't become bacon!\n")
# Creating a while loop to keep track of health and end the game if Hammy dies
# Like below, I do not think this is working as intended, but functions
  while health != 0:
    porklogic.sectionZero()
'''
Tracking player health game over condition here
Currently I do not think this is actually working, maybe move to this
function over to porklogic?

if health <= 0:
  print("You have become bacon!")
  break
'''

# Getting yes or no input for game start
# gameTitle function contains the game start secion so invalid inputs do not result in an exit
def gameTitle():
  gameStart = input("Do you dare enter? (y/n)\n").lower()  # Using lowercase function
# Actions resulting from input
  if gameStart == "y":
    print("Welcome!")
    runGame()  # This launches the main part of the game defined above
  elif gameStart == "n":
    print("Farewell!")
    exit()
  else:
    print("Valid inputs are y or n")
    gameTitle()  # This allows invalid key inputs to loop back for another input


# Running gameTitle function to start the game
gameTitle()

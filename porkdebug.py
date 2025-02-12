'''
Pork, a Zork like game about a pig named Hammy
This is the main file which starts and runs the game itself
Map movement is done through a seperate file name porklogic.py
Initial code by coderchameleon
This module is intended for debuggin/testing the map sections in a more
effecient way rather than running through the actualy game to test each one
'''
# Library imports
from art import *  # Importing the art lib to make the game title look a little cooler
from colored import fg, attr  # Importing colored to help color some text
import porklogic  # Importing functions from game logic file
import time  # Importing to start adding in waits between print statements
def debugMain(): # The main debug function (just a placeholder currently)
   # creating a dictionary to be used for the function call based on input
   sections = {
    "1": porklogic.sectionOne,
    "2": porklogic.sectionTwo,
    "3": porklogic.sectionThree,
    "4": porklogic.sectionFour,
    "5": porklogic.sectionFive,
    "7": porklogic.sectionSeven,
    "9": porklogic.sectionNine,
    }
   sectionDebug = input("Which section to debug?").lower()
   print("Going to map section " + sectionDebug)
   time.sleep(2)
   if sectionDebug in sections: # taking input and calling the associated function
    sections[sectionDebug]()
   else:
    print("Invalid, make sure that map section exists.")

'''
Pork, a Zork like game about a pig
Initial code by bombercode
'''
# Importing the art lib to make the game title look a little cooler
from art import *
from colored import fg, attr #Importing colored to help color some text
import porklogic #Importing functions from game logic file
tprint("PORK", space=3)
health = 3 #Making this a global variable so it can be touched by all functions if needed
#Creating master function to run game
def runGame():
#Intro text
    print("You are named Hammy\n")
    print("You are a pig and you must make your way through the forest.\n")
    print("Don't become bacon!\n")
#Creating a while loop to keep track of health and end the game if Hammy dies
    while health != 0:
        porklogic.sectionZero()
# Tracking player health game over condition here
        if health <= 0:
            print("You have become bacon!")
            break
#Getting yes or no input for game start
#gameTitle function contains the game start secion so invalid inputs do not result in an exit
def gameTitle():
    gameStart = input("Do you dare enter? (y/n)")
#Actions resulting from input
    if gameStart == "y":
        print("Welcome!")
        runGame() #This launches the main part of the game defined above as runGame for the actual game to start
    elif gameStart == "n":
        print("Farewell!")
        exit()
    else:
        print("Valid inputs are y or n")
        gameTitle() #This allows invalid key inputs to loop back for another input
#Running gameTitle funciton to start the game
gameTitle()

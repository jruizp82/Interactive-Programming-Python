# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

# import the modules

import simplegui
import random
import math

# initialize global variables used in your code

num_range = 100
secret_num = 0
remaining_num = 0

# helper function to initial game

def init():
    global num_range
    global secret_num
    global remaining_num
    
    # generate a random secret number in a given range
    secret_num = random.randrange(0,num_range)
    
    # find out the number of allowed guesses based 
    # on the range of the secret number
    remaining_num = math.ceil(math.log(num_range,2))
    
    print "New Game. Range is from 0 to", num_range
    print "Number of remaining guesses is", remaining_num
    
# define event handlers for control panel
    
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range
    num_range = 100
    print
    init()
 
def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range
    num_range = 1000
    print
    init()
    
def get_input(guess):
    # main game logic goes here	
    global secret_num
    global remaining_num
    
    # convert guess into an integer 
    guess_num = int(guess)
    
    remaining_num -= 1
    print
    print "Guess was ", guess_num
    print "Number of remaining guesses is ", remaining_num
    
    # compares the guess number to the secret number 
    # and prints out the appropriate response
    if (secret_num < guess_num):
        print "Lower!"
    elif (secret_num > guess_num):
        print "Higher!"
    else:
        print "Correct!"
        print
        init() 
        
    # if you ran out of guesses you loses
    # and a new game start    
    if(remaining_num == 0):
        print "You lose. You ran out of guesses"
        print
        init()
  
# create frame

f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements

f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", get_input, 200)

init()

# start frame

f.start()

# always remember to check your completed program against the grading rubric

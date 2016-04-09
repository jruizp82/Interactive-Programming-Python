# implementation of card game - Memory

import simplegui
import random

numbers = range(8) * 2
random.shuffle(numbers)

exposed = ["False", "False", "False", "False", "False", "False", 
           "False", "False", "True", "False", "False", "False", 
           "False", "False", "False", "False"]


# helper function to initialize globals
def init():
    pass  

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    card_pos = 0
    #number_pos = 10
    for i in range(16):
        if exposed[i] == "False":
            canvas.draw_polygon([(card_pos, 0), (card_pos, 100), (card_pos+50, 100), (card_pos+50, 0)], 2, "Brown", "Green")
            #card_pos = card_pos+50
        else:
            canvas.draw_text(str(numbers[i]),(card_pos+10,65),48,"White")
            #number_pos = number_pos+50
        card_pos = card_pos+50

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
label = frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()


# Always remember to review the grading rubric
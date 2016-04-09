# implementation of card game - Memory

import simplegui
import random

numbers = range(8) * 2
exposed = ["False", "False", "False", "False", "False", "False", 
           "False", "False", "False", "False", "False", "False", 
           "False", "False", "False", "False"]
state = 0
click1 = 0
click2 = 0
count = 0

# helper function to initialize globals
def init():
    global state, exposed, count, numbers
    random.shuffle(numbers)
    state = 0
    count = 0
    label.set_text('Moves = 0')
    exposed = ["False", "False", "False", "False", "False", "False", 
           "False", "False", "False", "False", "False", "False", 
           "False", "False", "False", "False"]
     
# define event handlers
def mouseclick(pos):
    global state
    global click1, click2
    global exposed
    global count
    
    # add game state logic here
    index = pos[0] // 50  
    if exposed[index] == "False":
        if state == 0:
            click1 = index
            exposed[click1] = "True"            
            state = 1
            count += 1
            label.set_text('Moves = ' + str(count))
        elif state == 1:
            click2 = index
            exposed[click2] = "True"
            state = 2
        else:
            if numbers[click1] != numbers[click2]:
               exposed[click1] = "False"
               exposed[click2] = "False" 
            click1 = index
            exposed[click1] = "True"
            count += 1
            label.set_text('Moves = ' + str(count))
            state = 1     
        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    card_pos = 0
    global exposed
    for i in range(16):
        if exposed[i] == "False":
            canvas.draw_polygon([(card_pos, 0), (card_pos, 100), (card_pos+50, 100), (card_pos+50, 0)], 2, "Brown", "Green")
        else:
            canvas.draw_text(str(numbers[i]),(card_pos+10,65),48,"White")
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
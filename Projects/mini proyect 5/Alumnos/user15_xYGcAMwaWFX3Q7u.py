# implementation of card game - Memory

# Dominique LaCasse

import simplegui
import random

# helper function to initialize globals
def init():
    global deck, exposed, state, first, second, moves
    state, moves = 0, 0
    deck = [] # store card numbers
    exposed = [] # store booleans for displaying cards
    first, second = 0, 0 # store current cards in play
    deck = range(8)
    deck.extend(range(8))
    random.shuffle(deck)
    exposed = range(16)
    for i in exposed:
        exposed[i] = False
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, exposed, first, second, moves
    if state == 0:
        state = 1
    elif state == 1:
        state = 2
    else:
        state = 1
    i = pos[0] // 50 # check mouse pos and set i to index
    if exposed[i] == True: # check if card is exposed
        return # if already exposed, ignore mouse click
    # check for pair, if true: expose both cards (had to add exposed[i] test to prevent adjacent card from exposing[second]
    if state == 2 and deck[first] == deck[second] and exposed[i] == deck[second]:
        exposed[first] = True
        exposed[second] = True 
    # if not pair, flip over the two exposed cards
    if state == 1 and deck[first] != deck[second]:
        exposed[first] = False
        exposed[second] = False    
    # card selection and display 
    if state == 1:
        exposed[i] = True 
        first = i              
    elif state == 2:              
        exposed[i] = True 
        second = i 
        moves += 1
                             
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed, moves
    x, i = 0, 0
    while i < len(exposed):
        if exposed[i]: # draw black background & exposed cards
            canvas.draw_line((x + 25, 0), (x + 25, 100), 50, "Black")
            canvas.draw_text(str(deck[i]), (x + 12, 70), 60, "White")
        x += 50
        i += 1
        # draw grid lines every 50 pixels
        canvas.draw_line((x, 0), (x, 100), 2, "Black")
        label.set_text("Moves = " + str(moves))

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.set_canvas_background("Green")
frame.add_button("Restart", init)
label = frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()

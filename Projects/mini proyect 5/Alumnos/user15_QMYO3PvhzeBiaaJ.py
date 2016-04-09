# implementation of card game - Memory

import simplegui
import random

list_a = []
deck = []
exposed = [False] * 16
card = 0
prev_card = 0
current = 0
counter = 0
state = 0


# helper function to initialize globals
def init():
    global list_a, deck, exposed, counter
    exposed = [False] * 16
    list_a = range(0, 8)
    list_b = range(0, 8)
    deck = list_a.extend(list_b)
    deck = list_a
    random.shuffle(list_a)
    counter = 0
    label.set_text("Moves = 0")

     
# define event handlers
def mouseclick(pos):
    global exposed, state, card, prev_card, counter, deck
    position = list(pos)
    current = position[0]//50
    if exposed[current] == False:
        if state == 0:
            card = current
            exposed[card] = True
            state = 1
        elif state == 1:  
            counter += 1
            text_counter = str(counter)
            label.set_text("Moves = " + text_counter)
            prev_card = card
            card = current
            exposed[card] = True
            state = 2
        elif state == 2:   
            if deck[prev_card] == deck[card]:
                exposed[current] = True
                card = current
                state = 1
            else:
                exposed[current] = True
                exposed[card] = False
                exposed[prev_card] = False
                prev_card = card
                card = current
                state = 1               
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global deck
    for number in range(16):
        if exposed[number]:
            canvas.draw_text(str(deck[number]), (number*50 + 15, 65), 36, "White")
        else:
            canvas.draw_polygon([(0+50*number, 0), (0 + 50*number, 100), (50 + 50*number, 100), (50 + 50*number, 0)], 5, "Red", "White")

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
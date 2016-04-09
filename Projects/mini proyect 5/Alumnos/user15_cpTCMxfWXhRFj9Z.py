# implementation of card game - Memory

import simplegui
import random

numbers = range(8)+range(8)
random.shuffle(numbers)
exposed = 16*[False]
move =0
# helper function to initialize globals
def init():
    global move, state, numbers, exposed
    state, move = 0,0  
    random.shuffle(numbers)
    exposed = 16*[False]
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, exposed, current , pre, move   
    if state == 0:
        if not exposed[pos[0]//50]:
            current,pre = pos[0]//50, pos[0]//50
            exposed[current] = True
            state = 1
            move += 1 
    elif state == 1:
        if not exposed[pos[0]//50]:
            current = pos[0]//50
            exposed[current] = True
            state = 2
    else:
        if not exposed[pos[0]//50]:
            if numbers[current] == numbers[pre]:
                exposed[current],exposed[pre]=True,True
                pre = pos[0]//50
                exposed[pre] = True
                state = 1
            else:
                exposed[current],exposed[pre]=False,False
                pre = pos[0]//50
                exposed[pos[0]//50] = True
                state = 1
        move += 1
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global numbers, exposed, move 
    for i in range(16):
        if exposed[i] == False:
            canvas.draw_polygon([[50*i, 0], [50*i, 100],
                                 [50*(i+1), 100],[50*(i+1),0]], 1.5, "Red", "Green")
        else:
            canvas.draw_text(str(numbers[i]), (50*i, 80), 75, "White")
    label.set_text("Moves = "+str(move))
# create frame and add a button and labels
frame = simplegui.create_frame("Memory Game!", 800, 100)
frame.add_button("Restart", init)
label = frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()

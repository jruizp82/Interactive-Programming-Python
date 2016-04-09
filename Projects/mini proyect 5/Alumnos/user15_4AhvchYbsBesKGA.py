# implementation of card game - Memory

import simplegui
import random

deck1 = range(8)
deck2 = range(8)
random.shuffle(deck1)
random.shuffle(deck2)
deck = deck1 + deck2

expose = [False]*16


# helper function to initialize globals
def init():
    global state, count, expose
    random.shuffle(deck)
    state = 0
    count = 0
    expose = [False] * 16
     

     
# define event handlers
def mouseclick(pos):
    global expose, state, click1, click2, count
    # add game state logic here
    index = pos[0]//50
    if state == 0:
        state = 1
        count += 1
        click1 = index
        expose[index] = True
    elif state == 1 and not expose[index]:
        state = 2
        click2 = index
        expose[index] = True
    elif state == 2 :
        if not deck[click1] == deck[click2]:
            expose[click1], expose[click2] = False, False
        if not expose[index]:
            state = 1
            count += 1
            click1 = index
            expose[index] = True
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for n in range(16):
        if expose[n]:
            canvas.draw_text(str(deck[n]), [50 * n, 100], 110, "Red")
        else:
            canvas.draw_polygon([(50*n, 0), (50*(n+1)-1, 0), (50*(n+1)-1, 100), (50*n, 100)], 1, "Green", "Green")
    label.set_text("Moves = " + str(count))
    pass


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
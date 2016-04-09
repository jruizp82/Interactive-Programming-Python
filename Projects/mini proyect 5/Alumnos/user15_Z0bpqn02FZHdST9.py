# implementation of card game - Memory
'''canvas.draw_polygon([(4+50*a, 4), (50+50*a, 4), (50+50*a, 98),(4+50*a,98)], 3, "Orange", "Green")
            a = pos_1
            canvas.draw_polygon([(4+50*a, 4), (50+50*a, 4), (50+50*a, 98),(4+50*a,98)], 3, "Orange", "Black")
            canvas.draw_text(str(number_list[0+a]), (10+50*a,75),70,"white")
'''        
import simplegui
import random
a = -1
a1 = 0
a2 = 0
b1 = 0
b2 = 0
state = 0
position = []
num1= range(0,8)
num2= range(0,8)
number_list = num1+num2
random.shuffle(number_list)
ok = []
move = 0
ss = 0
# helper function to initialize globals
def init():
    global state, ok, move
    ok = []
    random.shuffle(number_list)
    state = 0
    move = 0
    label.set_text("Moves =" + str(move))
     
# define event handlers
def mouseclick(pos):
    # add game state logic here

    global position, state, a1, a2, move,ss
    position = pos
    ss += 1
    if ss%2 == 0:
        move +=1
        label.set_text("Moves =" + str(move))
        print move
    if state == 0:
        global b1
        state = 1
        a1 = position[0]//50
        ok.append(a1)
        b1 = number_list[a1]
    elif state == 1:
        global b2
        a2 = position[0]//50
        if a1 == a2:
            ss=0
        else:      
            state = 2
            ok.append(a2)
            b2 = number_list[a2]
         
    else:
        if b1 != b2:
            ok.remove(a1)
            ok.remove(a2)
        state = 1
        a1 = position[0]//50
        ok.append(a1)
        b1 = number_list[a1]
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global a1, a2, a, ok, b1, b2
          
    if state == 0:
        for a in range(0,16):
            canvas.draw_polygon([(4+50*a, 4), (50+50*a, 4), (50+50*a, 98),(4+50*a,98)], 3, "Orange", "Green")
    if state == 1: 
        
        for a in ok:
            canvas.draw_polygon([(4+50*a, 4), (50+50*a, 4), (50+50*a, 98),(4+50*a,98)], 3, "Orange", "Black")
            canvas.draw_text(str(number_list[0+a]), (10+50*a,75),70,"white")
        for a in range(0,16):
           if a not in ok:
               canvas.draw_polygon([(4+50*a, 4), (50+50*a, 4), (50+50*a, 98),(4+50*a,98)], 3, "Orange", "Green")
         
    if state == 2:
        
        for a in ok:
            canvas.draw_polygon([(4+50*a, 4), (50+50*a, 4), (50+50*a, 98),(4+50*a,98)], 3, "Orange", "Black")
            canvas.draw_text(str(number_list[0+a]), (10+50*a,75),70,"white")
        for a in range(0,16):
           if a not in ok:
               canvas.draw_polygon([(4+50*a, 4), (50+50*a, 4), (50+50*a, 98),(4+50*a,98)], 3, "Orange", "Green")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
label = frame.add_label("Moves=0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()


# Always remember to review the grading rubric
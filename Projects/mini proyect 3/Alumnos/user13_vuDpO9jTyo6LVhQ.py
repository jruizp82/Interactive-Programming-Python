# template for "Stopwatch: The Game"
import simplegui
import math
# define global variables
counter = 0
t = 0
points = 0
tries = 0
started = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    pass
    global counter
    t = counter
    a_min = t // 600
    b_sec = (t / 10) // 10
    c_sec = (t // 10) % 10
    d_sec = t % 10
    return str (a_min)+ ":" + str (b_sec) + str (c_sec) + "." + str (d_sec)

def score():
    global points, tries, t
    if t % 10 == 0:
        points = points + 1
        tries += 1
    else:
        tries += 1
    show = str(points) + "/" + str(points)
    return show

    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
       timer.stop()
       started = False
       score()
    
    
def reset():
    global counter
    counter = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    counter += 1

# define draw handler
def draw(canvas):
    canvas.draw_text (str (score()), (130, 20), 14, "Black")
    canvas.draw_text (str (format(t)), (75, 100), 18, "Black")
    
# create frame
frame = simplegui.create_frame("Stopwatch: the game", 200, 200)
frame.set_canvas_background("Red")
frame.set_draw_handler(draw)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
timer = simplegui.create_timer(100, tick)



# register event handlers


# start frame
frame.start()
timer.start()

# Please remember to review the grading rubric

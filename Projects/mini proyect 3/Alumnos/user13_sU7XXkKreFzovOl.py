# template for "Stopwatch: The Game"
import simplegui

# define global variables
time = 0
stop = 0
stop_sec = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    """Format A:BC.D"""
    d = str(t%10)
    c = str((t//10)%10)
    b = str(((t//10)%60)//10)
    a = str((t//600)%10)
    return a + ":" + b + c + "." + d
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def reset_button_handler():
    global time, stop, stop_sec
    time = 0
    stop = 0
    stop_sec = 0
    
def start_button_handler():
    timer.start()

def stop_button_handler():
    global stop, stop_sec, time
    if timer.is_running():
        stop += 1
        timer.stop()
        if (time % 10 == 0):
            stop_sec += 1;

# define event handler for timer with 0.1 sec interval
def tick():
    global time
    if (time < 10000):
        time += 1
    else:
        timer.stop()

# define draw handler
def draw(canvas):
    canvas.draw_text(str(format(time)), [100,110], 40, "Black")
    canvas.draw_text(str(stop_sec) + " / " + str(stop), (200, 35), 30, "Green")
    
# create frame
frame = simplegui.create_frame("StopWatch", 300, 200)
frame.add_button("Start", start_button_handler, 100)
frame.add_button("Reset", reset_button_handler, 100)
frame.add_button("Stop", stop_button_handler, 100)

# register event handlers
frame.set_draw_handler(draw)
frame.set_canvas_background("White")
timer = simplegui.create_timer(100, tick)

# start frame
frame.start()


# Please remember to review the grading rubric
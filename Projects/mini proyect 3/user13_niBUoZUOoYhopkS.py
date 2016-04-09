# template for "Stopwatch: The Game"

# import the module
import simplegui

# define global variables
counter = 0
x = 0  # number_successful_stops 
y = 0  # number_total_stops
d = 0  # the amount of the remaining tenths of seconds 

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(counter):
    
    # get a by dividing the tenths of seconds by 600
    # using integer division
    a = counter // 600
    
    # get b(the amount of tens of of seconds)
    seconds = counter // 10
    remainder = seconds % 60
    b = remainder // 10
    
    # get c(the amount of seconds in excess of tens of seconds)
    c = remainder % 10
    
    # get d(the amount of the remaining tenths of seconds)
    global d
    d = counter % 10
    return str(a) + ":" + str(b) + str(c) + "." + str(d)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    global x, y, d
    # if timer is running increments the number total stops
    if timer.is_running():
        y += 1
        # if timer is running and the digit of the tenths of seconds is 0,
        # increments the number successfull stops
        if (d % 10) == 0:
            x += 1
        timer.stop()   
    
def reset():
    # set these numbers back to zero
    global counter, x, y
    counter = 0
    x = 0
    y = 0
    timer.stop()

# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    counter += 1
    # the clock resets when reaches 10 minutes
    if counter >= 6000:
        reset()

# define draw handler
def draw(canvas):
    global x,y
    time = format(counter)
    canvas.draw_text(time, [60, 110], 36, "White")
    canvas.draw_text(str(x)+"/"+str(y), [150, 20], 24, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 200, 200)

# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)

# start frame
frame.start()

# Please remember to review the grading rubric

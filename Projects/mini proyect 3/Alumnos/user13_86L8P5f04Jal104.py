# template for "Stopwatch: The Game"

import simplegui
# Random is imported for my random message system.
# Doesn't do anything on the rest of the program.
import random

# define global variables
time = 0
stop_attempts = 0
successful_stops = 0
clock_ticking = False
msg = ""

# list of messages just for fun
good_msg = ['Excelent!', 'Nice reflexes!', "You're good!", "Keep it up!", 'Good job!']
bad_msg = ['Sucker!', 'Nice try', 'Keep trying!', 'Try again']

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    """ Formats time so it looks like a stopwatch """
    a_minutes = t // 600
    b_seconds = ((t // 10) % 60) // 10
    c_seconds = (t // 10) % 10
    d_tenths = t % 10
    return str(a_minutes) + ":" + str(b_seconds) + str(c_seconds) +"." + str(d_tenths)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    """ Starts main timer """
    global clock_ticking
    timer.start()
    clock_ticking = True
    
def stop():
    """ Stops main timer and grants points for successful stops"""
    global successful_stops, stop_attempts, clock_ticking, msg
    if clock_ticking:
        timer.stop()
        clock_ticking = False
        msg_timer.start()
        if (time % 10) == 0:
            successful_stops += 1
             # grabs a random good_msg to print from the list
            random_msg = random.randrange(0, len(good_msg))
            msg = good_msg[random_msg]
        else:
            stop_attempts += 1
            # grabs a random bad_msg to print from the list
            random_msg = random.randrange(0, len(bad_msg))
            msg = bad_msg[random_msg]
    
def reset():
    """ Resets main timer """
    global time, stop_attempts, successful_stops, clock_ticking, msg
    time = 0
    stop_attempts = 0
    successful_stops = 0
    clock_ticking = False
    msg = ""
    

# define event handler for timer with 0.1 sec interval
def timer_handler():
    """ Handles time for the stopwatch """
    global time
    time += 1
    return time

# score handler
def score():
    global stop_attempts, successful_stop
    return "Hits: " + str(successful_stops)+ " / Total: " + str(stop_attempts)
    

# message event handlers
def message():
    """ Prints message """
    return msg

def message_timer():
    """ Cleans printed message """
    global msg
    msg = ""
    msg_timer.stop()
    return msg

# define draw handler
def draw(canvas):
    # Draws timer        
    canvas.draw_text(format(time),(170, 170), 60, "Yellow", "serif")
    # Draw current score
    canvas.draw_text(score(),(120, 80), 40, "Yellow", "serif")
    # Draws message      
    canvas.draw_text(message(),(180, 220), 30, "White", "serif")
    # Draws instructions   
    canvas.draw_text("Stop the watch when the tenths of seconds are 0!",(70, 270), 20, "White", "serif")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 500, 300)
frame.set_canvas_background("Green")

# register event handlers
frame.add_label("Click 'Start' to begin game",200)
frame.add_label("'Stop' to stop the watch",200)
frame.add_label("'Reset' to start over",200)
frame.add_label("",200)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, timer_handler)

# timer for message duration
# when timer activates, message is erased on method message_timer
msg_timer = simplegui.create_timer(1100, message_timer)

# start frame
frame.start()

# Please remember to review the grading rubric

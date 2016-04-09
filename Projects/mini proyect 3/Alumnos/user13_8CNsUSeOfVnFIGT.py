# template for "Stopwatch: The Game"
import simplegui
import math

# define global variables
mytime = 0
milliseconds_per_timestep = 100
is_stopped = True
total_stops = 0
stops_on_sec = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    t_min = math.floor(t/600)
    t_remainder = t - (t_min*600)
    t_sec = math.floor(t_remainder/10)
    t_remainder = t_remainder - t_sec*10
    t_sec10 = t_remainder
    time_str = "%d:%02d.%d" %(t_min, t_sec, t_sec10)
    return time_str
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def stop_timer():
    global is_stopped, mytime, total_stops, stops_on_sec    
    timer.stop()
    if not is_stopped:
        #figure out scoring, since game was 'active'
        if (mytime % 10 == 0): stops_on_sec = stops_on_sec + 1
        total_stops = total_stops + 1            
    is_stopped = True
    
def start_timer():
    global is_stopped
    is_stopped = False
    timer.start()
    
def reset_timer():
    global mytime, total_stops, stops_on_sec, is_stopped
    mytime = 0
    total_stops = 0
    stops_on_sec = 0
    is_stopped = True #to avoid reset giving a false 'hit' in the game
    stop_timer()
    
# define event handler for timer with 0.1 sec interval
def update():
    global mytime
    mytime = mytime + 1 
    print mytime #debugging only
    return
    
# define draw handler
def display_time(canvas):
    global mytime, total_stops, stops_on_sec
    canvas.draw_text(format(mytime), (110,140), 30, "Black", "monospace")
    canvas.draw_text(str(stops_on_sec)+"/"+str(total_stops), (220,40), 30, "Red", "sans-serif")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 300)
frame.set_canvas_background("Teal")
frame.set_draw_handler(display_time)
frame.add_button("Start", start_timer, 100)
frame.add_button("Stop", stop_timer, 100)
frame.add_button("Reset", reset_timer, 100)

# register event handlers
timer = simplegui.create_timer(milliseconds_per_timestep, update)

# start frame
frame.start()

# Please remember to review the grading rubric

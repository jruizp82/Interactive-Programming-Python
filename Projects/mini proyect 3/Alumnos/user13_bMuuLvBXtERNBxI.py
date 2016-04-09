# template for "Stopwatch: The Game"
import simplegui
import random

# define global variables
time = 0

tries = 0
hits = 0

hardmode = 0
pos1 = 0
pos2 = 0
pos3 = 0
pos4 = 0

a = 0
b = 0
c = 0
d = 0

frame = simplegui.create_frame("stopwatch game thing", 300, 300)

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format():
    global time, a, b, c, d
    
    if time == 10 :
        c = c + 1
        time = 0
    if c == 10 :
       b = b + 1
       c = 0
    if b == 6 :
       a = a + 1
       b = 0
    
    d = time / 1
    return a, b, c, d

    
    
    
def timer_start():
    timer.start()
    timer2.start()
def timer_stop():
    if timer.is_running():
        hit()
    timer.stop()
    timer2.stop()
    
def timer_reset():
    global time, a, b, c, d, tries, hits, hardmode
    a = 0
    b = 0
    c = 0
    d = 0
    time = 0
    tries = 0
    hits = 0
    hardmode = 0
    timer.stop()
    timer2.stop()
    return time, a, b, c, d, tries, hits, hardmode

def hit():
    global d, tries, hits
    tries = tries + 1
    if d == 0 :
        hits = hits + 1
    return tries, hits

def hardmode():
    global hardmode
    timer.start()
    timer2.start()
    hardmode = 1
    return hardmode


def harddraw():
    global pos1, pos2, pos3, pos4
    pos1 = random.randrange(2, 295)
    pos2 = random.randrange(2, 295)
    pos3 = random.randrange(2, 295)
    pos4 = random.randrange(2, 295)
    return pos1, pos2, pos3, pos4

    
def tick():
    global time
    time = time + 1
    format()
    return time
    
    
timer = simplegui.create_timer(100, tick)
timer2 = simplegui.create_timer(200, harddraw)


# Draw handler
def draw(canvas):
    global a, b, c, d, tries, hits, hardmode, pos1, pos2, pos3, pos4
    canvas.draw_text(str(a) + ":" + str(b) + str(c) + "." + str(d), (75, 120), 20, "Red")
    canvas.draw_text("aim for the full seconds", (100, 150), 15, "red")
    canvas.draw_text("tries:" + str(tries) + "/" + "hits:" + str(hits), (75, 75), 20, "red")
    if hardmode == 1 :
            canvas.draw_circle([pos1, pos2], 20, 12, "Green")
            canvas.draw_circle([pos3, pos4], 5, 5, "blue", "blue")
            canvas.draw_text("HEY! LISTEN!", [pos3,(pos4 + 17)], 12, "blue")
            canvas.draw_circle([pos2, pos2], 5, 3, "red", "green")
            canvas.draw_circle([pos1, pos1], 15, 12, "Green")
            canvas.draw_circle([pos3, pos3], 30, 15, "yellow")
            canvas.draw_circle([pos4, pos3], 12, 12, "red")
            canvas.draw_circle([pos2, pos4], 90, 15, "Green")
            canvas.draw_text("hardmode", (25, 25), 15, "red")
# Buttons 
frame.set_draw_handler(draw)
button1 = frame.add_button("start timer", timer_start, 100)
button2 = frame.add_button("stop timer", timer_stop, 100)
button3 = frame.add_button("hit without stopping", hit, 120)
button4 = frame.add_button("reset", timer_reset, 75)
button5 = frame.add_button("hard-mode", hardmode, 75)





frame.start()

# Please remember to review the grading rubric
"""
Grading Rubric - 13 pts total (scaled to 100 pts)

    1 pt - The program successfully opens a frame with the stopwatch stopped.
    1 pt - The program has a working "Start" button that starts the timer.
    1 pt - The program has a working "Stop" button that stops the timer.
    1 pt - The program has a working "Reset" button that stops the timer (if running) and resets the timer to 0.
    4 pts - The time is formatted according to the description in step 4 above. Award partial credit corresponding to 1 pt per correct digit. For example, a version that just draw tenths of seconds as a whole number should receive 1 pt. A version that draws the time with a correctly placed decimal point (but no leading zeros) only should receive 2 pts. A version that draws minutes, seconds and tenths of seconds but fails to always allocate two digits to seconds should receive 3 pts.
    2 pts - The program correctly draws the number of successful stops at a whole second versus the total number of stops. Give one point for each number displayed. If the score is correctly reported as a percentage instead, give only one point.
    2 pts - The "Stop" button correctly updates these success/attempts numbers. Give only one point if hitting the "Stop" button changes these numbers when the timer is already stopped.
    1 pt - The "Reset" button clears the success/attempts numbers.
"""

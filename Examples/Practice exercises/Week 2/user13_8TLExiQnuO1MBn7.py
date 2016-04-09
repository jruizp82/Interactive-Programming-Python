# Register three buttons

###################################################
# Student should add code where relevant to the following.

import simplegui 


# Handlers for buttons
def set_red():
    global color
    color = "red"
    
def set_blue():
    global color
    color = "blue"
    
def print_color():
    print color

# Create frame and register event handlers
frame = simplegui.create_frame("Set and print colors", 200, 200)
frame.add_button("Set color to red", set_red)
frame.add_button("Set color to blue", set_blue)
frame.add_button("Print current color", print_color)


# Start the frame animation
frame.start()


###################################################
# Test

set_red()
print_color()
set_blue()
print_color()
set_red()
set_blue()
print_color()

###################################################
# Expected output from test

#red
#blue
#blue

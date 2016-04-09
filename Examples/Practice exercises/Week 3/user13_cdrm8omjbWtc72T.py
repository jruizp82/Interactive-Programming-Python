# Display an X

###################################################
# Student should add code where relevant to the following.

import simplegui 

# Draw handler
def draw(canvas):
    # Note that vertical position for the text was computed manually
    canvas.draw_text("X",[0, 32], 48, "Red")
    

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Display X", 96, 96)
frame.set_draw_handler(draw)


# Start the frame animation
frame.start()


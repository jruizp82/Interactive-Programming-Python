# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
ball_pos = [0, 0]
ball_vel = [0, 0]
paddle1_pos = 0.0
paddle2_pos = 0.0
paddle1_vel = 0.0
paddle2_vel = 0.0
right = True


# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT /2]
    random_vel = [random.randrange(120,140)/60, random.randrange(60,180)/60]
        
    if right:
        ball_vel[0] = random_vel[0]
        ball_vel[1] = -random_vel[1]
    else:
        ball_vel[0] = -random_vel[0]
        ball_vel[1] = -random_vel[1]  
    
# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    paddle1_pos = HEIGHT /2
    paddle2_pos = HEIGHT /2
    ball_init(right)    

def draw(c):
    global score1, score2, paddle1_pos, paddle1_vel, paddle2_vel, paddle2_pos, ball_pos, ball_vel
    #ball_init(right)
    
    # update paddle's vertical position, keep paddle on the screen
    if (HALF_PAD_HEIGHT <= paddle1_pos + paddle1_vel <= HEIGHT - HALF_PAD_HEIGHT):
        paddle1_pos += paddle1_vel
    if (HALF_PAD_HEIGHT <= paddle2_pos + paddle2_vel <= HEIGHT - HALF_PAD_HEIGHT):
        paddle2_pos += paddle2_vel  
    
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    
    # left paddle
    c.draw_line((HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT),(HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT), 8, "White")
    
    
    # right paddle
    c.draw_line((WIDTH - PAD_WIDTH/2, paddle2_pos + HALF_PAD_HEIGHT), (WIDTH - PAD_WIDTH/2, paddle2_pos - HALF_PAD_HEIGHT), 8, "White")
    
     
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    print ball_pos    
    # collide and reflect off of left hand side of canvas
    if ball_pos[0] <= BALL_RADIUS:
        ball_vel[0] = - ball_vel[0]
    if ball_pos[0] >= (WIDTH - 1) - BALL_RADIUS:
        ball_vel[0] = - ball_vel[0]
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
    if ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH):
        ball_init(right)
    if ball_pos[0] >= ((WIDTH - PAD_WIDTH) - BALL_RADIUS):
        ball_init(right)    
    
    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    #acc = 1
    if key == simplegui.KEY_MAP["w"]:
        #paddle1_vel -= acc
        paddle1_vel = -2.0
    elif key == simplegui.KEY_MAP["s"]:
        #paddle1_vel += acc
        paddle1_vel = 2.0
    if key == simplegui.KEY_MAP["up"]:
        #paddle2_vel -= acc
        paddle2_vel = -2.0
    elif key == simplegui.KEY_MAP["down"]:
        #paddle2_vel += acc    
        paddle2_vel = 2.0
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel = 0.0
    paddle2_vel = 0.0    

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
frame.start()
new_game()

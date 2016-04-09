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

ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [-100 / 60,  50 / 60]
paddle1_vel = [0, 0]
paddle2_vel = [0, 0]
score1 = 0
score2 = 0
right = 1
paddle1_pos = [HALF_PAD_WIDTH, ((HEIGHT/2) - (HALF_PAD_HEIGHT))]
point2  = [HALF_PAD_WIDTH, ((HEIGHT/2) + (HALF_PAD_HEIGHT))] 
paddle2_pos = [WIDTH - HALF_PAD_WIDTH, (HEIGHT/2) - (HALF_PAD_HEIGHT)]
point4 = [WIDTH - HALF_PAD_WIDTH, ((HEIGHT/2) + (HALF_PAD_HEIGHT))] 


# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, ball_vel
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if right == True:
        ball_vel = [random.randrange(120, 240)/-60,  random.randrange(60, 180)/-60]
    elif right == False:
        ball_vel = [random.randrange(120, 240)/60, random.randrange(60, 180)/-60]

# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel # these are floats
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    paddle1_vel = [0, 0]
    paddle2_vel = [0, 0] 
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_init(right)
    
    
    
def button_handler():
    new_game()    
    
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, point1, point2, point3, point4, right
 
    # update paddle's vertical position, keep paddle on the screen

    if paddle1_pos[1] >= 0:
        paddle1_pos[1] += paddle1_vel[1]
    elif paddle1_pos[1] <= 0:    
        paddle1_pos[1] = 0
        point2[1] = PAD_HEIGHT
    
    if paddle2_pos[1] >= 0:
        paddle2_pos[1] += paddle2_vel[1]
    elif paddle2_pos[1] <= 0:    
        paddle2_pos[1] = 0
        point4[1] = PAD_HEIGHT
    
    if point2[1] <= HEIGHT:
        point2[1] += paddle1_vel[1]
    elif point2[1] >= HEIGHT: 
        paddle1_pos[1] = HEIGHT - PAD_HEIGHT
        point2[1] = HEIGHT
    
    if point4[1] <= HEIGHT:
        point4[1] += paddle2_vel[1]
    elif point4[1] >= HEIGHT: 
        paddle2_pos[1] = HEIGHT - PAD_HEIGHT
        point4[1] = HEIGHT        
                            
                            
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    c.draw_line(paddle1_pos, point2, PAD_WIDTH, "White")
    c.draw_line(paddle2_pos, point4, PAD_WIDTH, "White")
     
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if ball_pos[1] >= paddle1_pos[1] and ball_pos[1] <= point2[1]:
        if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
            ball_vel[0] = - ball_vel[0] * 1.1
   
    elif ball_pos[1] <= paddle1_pos[1] or ball_pos[1] >= point2[1]:
        if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
            ball_init(right)
            score2 += 1
            right = False
            ball_init(right)
                
    
    if ball_pos[1] >= paddle2_pos[1] and ball_pos[1] <= point4[1]:
        if ball_pos[0] >= (WIDTH - BALL_RADIUS - PAD_WIDTH):
            ball_vel[0] = - ball_vel [0] * 1.1
    
    elif ball_pos[1] <= paddle2_pos[1] or ball_pos[1] >= point4[1]:
        if ball_pos[0] >= (WIDTH - BALL_RADIUS - PAD_WIDTH):    
            score1 += 1
            right = True
            ball_init(right)
    
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
    if ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]     
        
        
    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    c.draw_text(str(score1), (175, 40), 36, "White")
    c.draw_text(str(score2), (400, 40), 36, "White")

    
def keydown(key):
    acc = 4
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["down"]:
        paddle1_vel[1] += acc
    elif key==simplegui.KEY_MAP["up"]:
        paddle1_vel[1] -= acc
    elif key==simplegui.KEY_MAP["s"]:
        paddle2_vel[1] += acc
    elif key==simplegui.KEY_MAP["w"]:
        paddle2_vel[1] -= acc
   
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel[1] = 0
    paddle2_vel[1] = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button("Restart", button_handler)

# start frame
frame.start()

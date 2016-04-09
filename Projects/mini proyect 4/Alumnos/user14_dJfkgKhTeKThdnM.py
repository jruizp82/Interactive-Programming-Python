# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
score1 = 0
score2 = 0
right = ball_vel[0]

paddle1_pos = [PAD_WIDTH, HEIGHT / 2]
paddle2_pos = [WIDTH - PAD_WIDTH, HEIGHT / 2]
paddle1_vel = [0, 0]
paddle2_vel = [0, 0]


# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left

def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    
    ball_pos = [WIDTH / 2, HEIGHT / 2]
       
    if ball_vel[0] <= 0:
        ball_vel = [random.randrange(120, 240) / 60, -random.randrange(60, 180) / 60]
        
    elif ball_vel[0] > 0:
        ball_vel = [-random.randrange(120, 240) / 60, -random.randrange(60, 180) / 60]
        
# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints

    score1 = 0
    score2 = 0
    paddle1_pos = [PAD_WIDTH, HEIGHT / 2]
    paddle2_pos = [WIDTH - PAD_WIDTH, HEIGHT / 2]
    paddle1_vel = [0, 0]
    paddle2_vel = [0, 0]
    ball_init(right)

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[1] += paddle1_vel[1]
    paddle2_pos[1] += paddle2_vel[1]
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    c.draw_polygon([(0, paddle1_pos[1] - 40), (PAD_WIDTH, paddle1_pos[1] - 40), (PAD_WIDTH, paddle1_pos[1] + 40), (0, paddle1_pos[1] + 40)], 2, "Green", "White")
    c.draw_polygon([(WIDTH - PAD_WIDTH, paddle2_pos[1] - 40), (WIDTH, paddle2_pos[1] - 40), (WIDTH, paddle2_pos[1] + 40), (WIDTH - PAD_WIDTH, paddle2_pos[1] + 40)], 2, "Green", "White")
     
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS and (ball_pos[1] < (paddle1_pos[1] - 40) or ball_pos[1] > (paddle1_pos[1] + 40)):
        
        score2 += 1
        ball_init(right)
        
    elif ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:        
        ball_vel[0] = -(ball_vel[0] + ball_vel[0] / 10)
                                
    if ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS and (ball_pos[1] < (paddle2_pos[1] - 40) or ball_pos[1] > (paddle2_pos[1] + 40)):
       
        score1 += 1
        ball_init(right)
        
    elif ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS: 
        ball_vel[0] = -(ball_vel[0] + ball_vel[0] / 10)
        
    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[1] >= (HEIGHT-1) - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    Score_1 = str(score1)
    Score_2 = str(score2)
            
    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    c.draw_text(Score_1, (150, 50), 40, "Red")
    c.draw_text(Score_2, (450, 50), 40, "Red")
     
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_pos, HEIGHT
    
    acc = 2
    
    if key == simplegui.KEY_MAP["w"] and paddle1_pos[1] > 40: 
        paddle1_vel[1] -= acc
        
    elif key == simplegui.KEY_MAP["s"] and paddle1_pos[1] < HEIGHT - 40:
        paddle1_vel[1] += acc
        
    elif key == simplegui.KEY_MAP["up"]and paddle2_pos[1] > 40:
        paddle2_vel[1] -= acc
        
    elif key == simplegui.KEY_MAP["down"]and paddle2_pos[1] < HEIGHT - 40:
        paddle2_vel[1] += acc
 
 
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel[1] = 0
        
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel[1] = 0
        
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel[1] = 0
        
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = 0
 

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)


# start frame
frame.start()
new_game()
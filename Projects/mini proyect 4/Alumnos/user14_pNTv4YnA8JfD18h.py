#Game pong
import simplegui
import random
# initialize pos and vel 
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

ball_pos=[0,0]
ball_vel=[0,0]

paddle1_pos=[[0,0],[0,0],[0,0],[0,0]]
paddle2_pos=[[0,0],[0,0],[0,0],[0,0]]
paddle1_vel=[0,0]
paddle2_vel=[0,0]

score1=0
score2=0
increment_velocity=0


# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos=[WIDTH/2,HEIGHT/2]
    if right==True:
        ball_vel[0]= (random.randrange(120, 240)//60)
        ball_vel[1]= -(random.randrange(60, 180)//60)
    else:
        ball_vel[0]= -(random.randrange(120, 240)//60)
        ball_vel[1]= -(random.randrange(60, 180)//60)
#increment velocity of ball to 10%		
def increment_velocity_ball(vel):
    return vel+((vel/100)*increment_velocity)
#collide and reflect of ball	
def collide_reflect():
    global ball_vel,increment_velocity,score1,score2
    if collide_ball_pad_1():
        increment_velocity+=10
        ball_vel[0] = - ball_vel[0]
        
    elif ball_pos[0] <= BALL_RADIUS:
        score2+=1
        increment_velocity=0
        ball_init(True)
     
    if collide_ball_pad_2():
        increment_velocity+=10
        ball_vel[0] = - ball_vel[0]
    
    elif ball_pos[0] >= ((WIDTH-1)-BALL_RADIUS):
        score1+=1
        increment_velocity=0
        ball_init(False)
        
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
       
    if ball_pos[1] >= ((HEIGHT-1)-BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
        
#update position of paddles		
def update_paddles():
    global paddle1_pos,paddle2_pos
    if paddle1_pos[0][1]>=0 and paddle1_pos[0][1]<=(HEIGHT-PAD_HEIGHT):
        for pos in paddle1_pos:
            pos[0]+=paddle1_vel[0]
            pos[1]+=paddle1_vel[1]
    elif paddle1_pos[0][1]<0:
        paddle1_pos=[[0,0],[PAD_WIDTH,0],[PAD_WIDTH,PAD_HEIGHT],[0,PAD_HEIGHT]]
    elif paddle1_pos[0][1]>(HEIGHT-PAD_HEIGHT):
        paddle1_pos=[[0,HEIGHT-PAD_HEIGHT],[PAD_WIDTH,HEIGHT-PAD_HEIGHT],[PAD_WIDTH,HEIGHT],[0,HEIGHT]]
    if paddle2_pos[0][1]>=0 and paddle2_pos[0][1]<=(HEIGHT-PAD_HEIGHT):
        for pos in paddle2_pos:
            pos[0]+=paddle2_vel[0]
            pos[1]+=paddle2_vel[1]
    elif paddle2_pos[0][1]<0:
        paddle2_pos=[[WIDTH-PAD_WIDTH,0],[WIDTH,0],[WIDTH,PAD_HEIGHT],[WIDTH-PAD_WIDTH,PAD_HEIGHT]]
    elif paddle2_pos[0][1]>(HEIGHT-PAD_HEIGHT):
        paddle2_pos=[[WIDTH-PAD_WIDTH,HEIGHT-PAD_HEIGHT],[WIDTH,HEIGHT-PAD_HEIGHT],[WIDTH,HEIGHT],[WIDTH-PAD_WIDTH,HEIGHT]]
#if collide ball and paddle 1 return true
def collide_ball_pad_1():
    if ball_pos[0] <= BALL_RADIUS+PAD_WIDTH and (ball_pos[1] >= paddle1_pos[1][1] and ball_pos[1] <= paddle1_pos[2][1]):
        return True
    else:
        return False
#if collide ball and paddle 2 return true		
def collide_ball_pad_2():
    if ball_pos[0] >= WIDTH-(BALL_RADIUS+PAD_WIDTH) and (ball_pos[1] >= paddle2_pos[0][1] and ball_pos[1] <= paddle2_pos[3][1]):
        return True
    else:
        return False
        
# define event handlers
#init the game and initialize variables
def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2,increment_velocity  # these are ints
    increment_velocity=0
    ball_init(True)
    paddle1_pos=[[0,(HEIGHT/2)-(PAD_HEIGHT/2)],[PAD_WIDTH,(HEIGHT/2)-(PAD_HEIGHT/2)],[PAD_WIDTH,(HEIGHT/2)+(PAD_HEIGHT/2)],[0,(HEIGHT/2)+(PAD_HEIGHT/2)]]
    paddle2_pos=[[WIDTH-PAD_WIDTH,(HEIGHT/2)-(PAD_HEIGHT/2)],[WIDTH,(HEIGHT/2)-(PAD_HEIGHT/2)],[WIDTH,(HEIGHT/2)+(PAD_HEIGHT/2)],[WIDTH-PAD_WIDTH,(HEIGHT/2)+(PAD_HEIGHT/2)]]
    paddle1_vel=[0,0]
    paddle2_vel=[0,0]
    score1=0
    score2=0
#draw in canvas	
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    # update paddle's vertical position, keep paddle on the screen
    update_paddles()
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    # draw paddles
    c.draw_polygon(paddle1_pos,1,"White","White")
    c.draw_polygon(paddle2_pos,1,"White","White")
    # update ball
    ball_pos[0]+=increment_velocity_ball(ball_vel[0])
    ball_pos[1]+=increment_velocity_ball(ball_vel[1])
    # collide and reflect off of left hand side of canvas
    collide_reflect()
    # draw ball and scores
    c.draw_text(str(score1),[WIDTH/4,HEIGHT/4],40,"Green")
    c.draw_text(str(score2),[(WIDTH/4)*3,HEIGHT/4],40,"Green")
    c.draw_circle(ball_pos,BALL_RADIUS,2,"Red","White")  
#key handler down	
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["W"]:
        paddle1_vel=[0,-10]
    elif key==simplegui.KEY_MAP["S"]:
        paddle1_vel=[0,10]
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel=[0,-10]
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel=[0,10]
#key handler up		
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["W"]:
        paddle1_vel=[0,0]
    elif key==simplegui.KEY_MAP["S"]:
        paddle1_vel=[0,0]
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel=[0,0]
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel=[0,0]
        
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", init, 100)
# start frame
init()
frame.start()
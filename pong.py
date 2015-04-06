
# Implementation of classic arcade game Pong
# Use http://www.codeskulptor.org/#user39_SaKgalEGbw_10.py to play
# Couple of extras like option to increase pad width and change ball velocity
# Uses simplegui library which seems to work only on Codeskulptor

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 10
PAD_WIDTH = 8
PAD_HEIGHT_def = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT_def = PAD_HEIGHT_def / 2
#LEFT = False
#RIGHT = True

#Variables to display game instructions
inst = 0
tcount = 0
#seconds to display intructions
isecs = 2

#Variables to set difficulty (ball velocity)
xvel_high = 4
xvel_low = 2
level=1
diferr=0
dcount=0

#Variables to set difficulty (paddle size)
pmult=1
perr=0
pcount=0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2,HEIGHT/2]
    ball_vel = [-4, 1]
    
    if (direction == "LEFT"):
        ball_vel[0] = random.randrange(xvel_low*level, xvel_high*level)
        ball_vel[1]= random.randrange(1*level, 2*level)
    if (direction == "RIGHT"):
        ball_vel[0] = random.randrange(xvel_low*level, xvel_high*level)*-1
        ball_vel[1]= random.randrange(1*level, 2*level)
        
    
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2, pmult,level,xvel_high, xvel_low
    
    
    paddle1_pos =  HEIGHT / 2
    paddle2_pos =  HEIGHT / 2
    spawn_ball("n")
    
    paddle1_vel = 0
    paddle2_vel = 0
    
    score1 = 0
    score2 = 0
    
    pmult = 1
    level = 1
    xvel_high = 4
    xvel_low = 2
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global HALF_PAD_HEIGHT,PAD_HEIGHT
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]
    
    if (ball_pos[1] <= BALL_RADIUS or  ball_pos[1] >= HEIGHT - BALL_RADIUS):
        ball_vel[1] = ball_vel[1]*-1
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 5, 'Blue', 'White')
    # draw paddles
    PAD_HEIGHT = PAD_HEIGHT_def*pmult
    HALF_PAD_HEIGHT = PAD_HEIGHT/2
   
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos - HALF_PAD_HEIGHT >=0
       and paddle1_pos + HALF_PAD_HEIGHT <= HEIGHT):
        paddle1_pos = paddle1_pos + paddle1_vel
    elif (paddle1_pos - HALF_PAD_HEIGHT <=0):
        paddle1_pos = HALF_PAD_HEIGHT
    elif (paddle1_pos >= HEIGHT- HALF_PAD_HEIGHT):
        paddle1_pos = HEIGHT - HALF_PAD_HEIGHT
        
    if (paddle2_pos - HALF_PAD_HEIGHT >=0
       and paddle2_pos + HALF_PAD_HEIGHT <= HEIGHT):
        paddle2_pos = paddle2_pos + paddle2_vel
    elif (paddle2_pos - HALF_PAD_HEIGHT <=0):
        paddle2_pos = HALF_PAD_HEIGHT
    elif (paddle2_pos >= HEIGHT- HALF_PAD_HEIGHT):
        paddle2_pos = HEIGHT - HALF_PAD_HEIGHT
        
    
    
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT],[HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT],[WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    
    
    
    if (ball_pos[0]<PAD_WIDTH+BALL_RADIUS):
        if (ball_pos[1] - BALL_RADIUS <= paddle1_pos + HALF_PAD_HEIGHT and
        ball_pos[1] + BALL_RADIUS >= paddle1_pos - HALF_PAD_HEIGHT):
            
            ball_vel[0] = ball_vel[0]*-1.1
            if (ball_vel[0]>20):
                ball_vel[0]=20
                
            ball_pos[0] = PAD_WIDTH+BALL_RADIUS
            
    if (ball_pos[0]>WIDTH - (PAD_WIDTH+BALL_RADIUS)):
        if (ball_pos[1] - BALL_RADIUS <= paddle2_pos + HALF_PAD_HEIGHT and
        ball_pos[1]+ BALL_RADIUS  >= paddle2_pos - HALF_PAD_HEIGHT):
            ball_vel[0] = ball_vel[0]*-1.1
            if (ball_vel[0]<-20):
                ball_vel[0]=-20
            ball_pos[0] = WIDTH - (PAD_WIDTH+BALL_RADIUS)
           
    
    if (ball_pos[0]<PAD_WIDTH):
        score2 = score2+1
        spawn_ball("LEFT")
        
    elif (ball_pos[0]>WIDTH-PAD_WIDTH):
        score1 = score1 + 1
        spawn_ball("RIGHT")
    
    # draw scores
    s1 = "Player 1: "  + str(score1)
    s2 = "Player 2: "  + str(score2)
    canvas.draw_text(s1,(WIDTH*.25,80),18,'white')
    canvas.draw_text(s2,(WIDTH*.75,80),18,'white')
    
    #displays game intructions at start
    if (inst==1 and tcount<isecs):
        p1= "Use w/s keys"
        p2 = "Use up/down arrow keys"
        canvas.draw_text(p1,(WIDTH*.10,HEIGHT*.5),20,'red')
        canvas.draw_text(p2,(WIDTH*.60,HEIGHT*.5),20,'green')
    
    if (diferr==1 and dcount<isecs):
        canvas.draw_text("Enter integer 1-5 for velocity!!",(WIDTH*.10,HEIGHT*.5),30,'red')
      
    
    if (perr==1 and pcount<isecs):
        canvas.draw_text("Enter integer 1-5 for pad height!!",(WIDTH*.10,HEIGHT*.5),30,'red')
       
def keydown(key):
    global paddle1_vel, paddle2_vel	
    if (key==simplegui.KEY_MAP["w"]):
        paddle1_vel = -10
    if (key==simplegui.KEY_MAP["s"]):
        paddle1_vel = 10 
        
    if (key==simplegui.KEY_MAP["up"]):
        paddle2_vel = -10
 
    if (key==simplegui.KEY_MAP["down"]):
        paddle2_vel = 10 
       
   
def keyup(key):
    global paddle1_vel, paddle2_vel
        
    if (key==simplegui.KEY_MAP["w"]):
        paddle1_vel = 0
    if (key==simplegui.KEY_MAP["s"]):
        paddle1_vel = 0 
        
    if (key==simplegui.KEY_MAP["up"]):
        paddle2_vel = 0
    if (key==simplegui.KEY_MAP["down"]):
        paddle2_vel = 0
        
def resbutton():
    new_game()

def instbutton():
    global inst, tcount
    inst=1
    tcount=0
    timer.start()

def difbutton(diff):
    global level,dcount,diferr
    try:
        level = int(diff)
        if (level<1):
            level=1
        if (level>5):
            level=1
            dcount=0
            diferr=1
            timer.start()
    except:
        level=1
        dcount=0
        diferr=1
        timer.start()
        
def padbutton(mult):
    global pmult,pcount,perr
    try:
        pmult = int(mult)
        if (pmult<1):
            pmult=1
            
        if (pmult>5):
            pmult=1
            pcount=0
            perr=1
            timer.start()
    except:
        pmult=1
        pcount=0
        perr=1
        timer.start()

def timerhandler():
    global tcount,dcount,pcount,inst,perr,diferr
    if (inst==1):
        tcount=tcount+1
    if (diferr==1):
        dcount=dcount+1
    if (perr==1):
        pcount=pcount+1
    if (tcount>isecs or dcount>isecs or pcount>isecs):
        timer.stop()
        tcount=0
        inst=0
        pcount=0
        perr=0
        dcount=0
        diferr=0
    
 
 

timer = simplegui.create_timer(1000, timerhandler)


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button_rest = frame.add_button("New Game (Reset)",resbutton)
button_instt = frame.add_button("Show Instructions",instbutton)

button_diff = frame.add_input('Control Ball Speed (1-5)', difbutton, 50)
button_pad = frame.add_input('Control Paddle Height (1-5)', padbutton, 50)
# start frame
new_game()
frame.start()

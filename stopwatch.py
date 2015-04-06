#http://www.codeskulptor.org/#user39_XbcXALTeTk_13.py
# Stopwatch using simplegui
# template for "Stopwatch: The Game"
import simplegui
# define global variables
fractime = 0
stopcount = 0
right_stopcount = 0
scond = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    mins = t//600
    secs = (t%600)//10
    msecs = (t%600)%10
    tform = "%02d:%02d.%01d" % (mins,secs,msecs)
    return tform
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def tstart():
    global scond
    clock.start()
    scond = 0
    
def tstop():
    global stopcount, right_stopcount, scond
    clock.stop()
    
    if scond==0:
        stopcount = stopcount+1
    scond = 1
    
    if ((fractime%600)%10) == 0:
        right_stopcount = right_stopcount+1

def treset():
    global fractime, stopcount, right_stopcount
    fractime=0
    stopcount = 0
    right_stopcount = 0

# define event handler for timer with 0.1 sec interval
def clocker():
    global fractime
    fractime = fractime + 1
   
# define draw handler
def message(mess):
    strtime = format(fractime)
    mess.draw_text("Timer:"+strtime,(1,150),30,"red")
    mess.draw_text("Exact Stops:"+str(right_stopcount)+"/"
                   +str(stopcount),(50,50),20,"green")
                     
# create frame
canvas = simplegui.create_frame("Stopwatch",200,200)

button_start = canvas.add_button("Start",tstart,75)
button_stop = canvas.add_button("Stop",tstop,75)
button_reset = canvas.add_button("Reset",treset,75)

# register event handlers
canvas.set_draw_handler(message)
clock = simplegui.create_timer(100,clocker)

# start frame
canvas.start()

# Please remember to review the grading rubric


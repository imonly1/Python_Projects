# template for "Stopwatch: The Game"

import simplegui

# define global variables
t=0
tat=0
sat=0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    if(t<=9):
        tstr="0:00."+str(t)
    elif(t<=99):
        tstr="0:0"+str(int(t/10))+"."+str(t%10)
    elif(t<=599):
        tstr="0:"+str(int(t/10))+"."+str(t%10)
    elif(t%600<=9):
        tstr=str(t/600)+":00."+str(t%10)
    elif(t%600<=99):
        tstr=str(t/600)+":0"+str(int(t%600/10))+"."+str(t%10)
    elif(t%600<=599):
        tstr=str(t/600)+":"+str(int(t%600/10))+"."+str(t%10)
    return tstr
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def startimer():
    timer.start()

def stoptimer():
    global tat,sat
    if(timer.is_running()):
        timer.stop()
        tat+=1
        if(t%10==0):
            sat+=1

def resetimer():
    global t,tat,sat
    timer.stop()
    tat=0
    sat=0
    t=0

# define event handler for timer with 0.1 sec interval
def tick():
    global t
    t+=1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(t), [115, 110], 36, "White")
    canvas.draw_text(str(sat)+"/"+str(tat),[250,20],24,"White")
    
# create frame
frame=simplegui.create_frame("Stop-Watch",300,200)
timer=simplegui.create_timer(100,tick)
frame.add_button("Start",startimer)
frame.add_button("Stop",stoptimer)
frame.add_button("Reset",resetimer)

# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()


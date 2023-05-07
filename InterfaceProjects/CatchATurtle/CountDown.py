import turtle as t 

wn=t.Screen()
timer=5
fontSetup=("Times New Roman",30,"normal")
interval=1000

timekeeper=t.Turtle()
timekeeper.penup()
timekeeper.hideturtle()
timekeeper.goto(-100,200)
timekeeper.pendown()
timekeeper.speed(0)

#functions
def updatetimer():
    #global is to let this function know to go look at a global var
    global timer
    timekeeper.clear()
    if timer<=0:
        timekeeper.write("Times UP!",font=fontSetup)
    else:
        timer-=1
        timekeeper.write(f"timer: {timer}",font=fontSetup)
        #We need to recusively run this function
        #timekeeper gets the screen's ontimer and resets the command and interval
        timekeeper.getscreen().ontimer(updatetimer,interval)
    
#events
wn.ontimer(updatetimer,interval)


wn.mainloop()
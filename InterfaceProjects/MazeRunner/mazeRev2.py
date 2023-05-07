#----import section ----
import turtle as t 
import random as r
#Game Cronfigurations or Global Var
wn=t.Screen()
numberOfWalls=25
pathWidth=15
fontSetup=("Times New Roman",30,"normal")
interval=1000
timer=0
paused =False
#Initialize Object or Turtles 
mazeDrawer = t.Turtle()
mazeDrawer.pensize(5)
mazeDrawer.pencolor("blue")
mazeDrawer.speed(0)

mazeRunner=t.Turtle()
mazeRunner.color("red")
mazeRunner.penup()
mazeRunner.goto(-pathWidth*2,pathWidth*2)
mazeRunner.pendown()

timekeeper=t.Turtle()
timekeeper.penup()
timekeeper.hideturtle()
timekeeper.goto(-100,250)
timekeeper.pendown()
timekeeper.speed(0)

pauseButtonSquare=t.Turtle(shape="square")
pauseButtonSquare.penup()
pauseButtonSquare.goto(-280,300)
pauseButtonSquare.pendown()
pauseButtonSquare.write("Pause Button")
pauseButtonSquare.penup()
pauseButtonSquare.goto(-250,250)
pauseButtonSquare.shapesize(4,4)

enemyRobot=t.Turtle(shape="turtle")
enemyRobot.penup()
enemyRobot.goto(300,300)
enemyRobot.shapesize(.5,.5)
enemyRobot.speed(10)

#Functions
def updatetimer():  #The function to change the time on the screen
    if mazeRunner.xcor()!= -pathWidth*2 and mazeRunner.ycor()!= pathWidth*2 and mazeRunner.color()[0]!="gray":
        #If the paused button is not pressed
        if paused!= True:
            #global is to let this function know to go look at a global var
            global timer
            #Clear timekeeper previous words
            timekeeper.clear()
            timer+=1 #Add one to time
            timekeeper.write(f"timer: {timer}",font=fontSetup)
            #If the time is 0 move the enemyRobot to the middle
            if timer==5:
                enemyRobot.goto(-pathWidth*2,pathWidth*2)
    #We need to recusively run this function
    #timekeeper gets the screen's ontimer and resets the command and interval
    timekeeper.getscreen().ontimer(updatetimer,interval)

#Function to move the enemy Robot and where to move it to if it hits a edge
def enemyMovment():
    #If the robot is in a range of the runner go after it         
    if (abs(mazeRunner.xcor() - enemyRobot.xcor()) < 60) and (abs(mazeRunner.ycor()-enemyRobot.ycor())<60):
        if mazeRunner.pos()[1] >= enemyRobot.pos()[1]:
            YAxis=.5
        elif mazeRunner.pos()[1] < enemyRobot.pos()[1]:
            YAxis=-.5
        if mazeRunner.pos()[0] >= enemyRobot.pos()[0]:
            xAxis=.5
        elif mazeRunner.pos()[0] < enemyRobot.pos()[0]:
            xAxis=-.5
        enemyRobot.goto(enemyRobot.pos()[0] + xAxis, enemyRobot.pos()[1] + YAxis)
    #If it is not 
    else: 
        x,y=enemyRobot.position() #returns both the x and y value
        #Move 4
        enemyRobot.fd(4)
        #Bounce off the top or bottom of the wall
        if y>(220):
            enemyRobot.setheading(r.randint(200,340))  
        elif y<(-190):
            enemyRobot.setheading(r.randint(20,160))  
        #bounce off the left or right wall
        if x>(150):
            enemyRobot.setheading(r.randint(100,250))  
        elif x<(-220):
            enemyRobot.setheading(r.randint(-60,60))  
 
#I got this idea from slack overflow
#Function to unpause
def unpause():
    print("unpause() called")
    #Calls up the variable and assigns it to False and runs the go function 
    global paused
    paused = False
    go()
#Function to pause
def pause():
    print("paused called")
    wn.onkeypress(None,"space") #Disabling the movement
    #Assigning the global variable of paused to true
    global paused
    paused = True
#This checks if it should unpause or pause when the button was hit, and calls up the right functiion, I came up with this secion by myself
def pausingwhat(x,y):
    if mazeRunner.color()[0]!="gray":
        global paused
        if paused == True:
            unpause()
        elif paused == False:
            pause()

def drawDoor(pos):  #pos is the distance we need to travel before placing a door
    mazeDrawer.fd(pos) 
    mazeDrawer.penup()
    mazeDrawer.fd(pathWidth*2)
    mazeDrawer.pendown()
def drawBarrier(pos):
    mazeDrawer.fd(pos)
    mazeDrawer.left(90)
    mazeDrawer.fd(pathWidth*2)
    mazeDrawer.bk(pathWidth*2)
    mazeDrawer.right(90)
def  drawMaze():
    wallLenght=15
    #Draw the number of walls
    for w in range(numberOfWalls):
        wallLenght+=pathWidth
        if w>4:
            mazeDrawer.left(90)
            #where do we draw the doors and barriers inside of a wall lenght
            doorSpot=r.randint(pathWidth*2,(wallLenght-2*pathWidth))
            barrierSpot=r.randint(pathWidth*2,(wallLenght-2*pathWidth))
            #check to make sure a doors and barrers do not render on top each other
            while abs(doorSpot-barrierSpot)<pathWidth:
                doorSpot=r.randint(pathWidth*2,(wallLenght-2*pathWidth))
            #if walls are bigger than 21, just draw number walls with no holes or doors for only one exist
            if w>=21:        
                mazeDrawer.fd(wallLenght)
            #"randomly" assigning which object we draw first
            elif(doorSpot<barrierSpot):
                #draw the door
                drawDoor(doorSpot)
                #draw the barrier
                drawBarrier(barrierSpot-doorSpot-pathWidth*2)
                mazeDrawer.fd(wallLenght-barrierSpot)
            else:
                drawBarrier(barrierSpot)
                drawDoor(doorSpot-barrierSpot)
                mazeDrawer.fd(wallLenght-doorSpot-pathWidth*2)
    mazeDrawer.hideturtle()

#The controls functions for the maze runners
def goUp():
    mazeRunner.setheading(90)
def goLeft():
    mazeRunner.setheading(180)
def goDown():
    mazeRunner.setheading(270)
def goRight():
    mazeRunner.setheading(0)
    
#The main function
def go():
    #If it is not paused
    if paused!= True:
        #If the time is more than 5, turn on the enemy
        if timer>5:
            enemyMovment()
        #If the maze runner hits the enemyRobot
        if (abs(mazeRunner.xcor() - enemyRobot.xcor()) < 10) and (abs(mazeRunner.ycor()-enemyRobot.ycor())<10):
            mazeRunner.color("gray")    
            enemyRobot.color("gray")
            wn.onkeypress(None,"space") #Disabling the movement
            wn.onkeypress(reset,"space")  #Calling reset
            wn.listen()
            return      
        #The mazeRunner goes 1 space
        mazeRunner.fd(1)
        #If the mazeRunner is x.cor is bigger than 200, it wins becuase the ending point is always on the right lower side
        if mazeRunner.xcor()>200:
            print("You win")
            mazeRunner.color("gray")
            wn.onkeypress(None,"space") #Disabling the movement
            wn.onkeypress(reset,"space")
            wn.listen()
            return                
        #determine if it hits a wally
        canvas=wn.getcanvas()
        x,y=mazeRunner.pos() #Get the x and y postion
        margin=1
        items=canvas.find_overlapping(x+margin,-y+margin,x-margin,-y-margin) #building the hitbox
        #if the items variables has overlap
        if(len(items)>0):   #stack of what is overlapping
            canvasColor=canvas.itemcget(items[0],"fill")
            if canvasColor=="blue": #We know we hit a wall
                mazeRunner.color("gray")
                wn.onkeypress(None,"space") #Disabling the movement
                wn.onkeypress(reset,"space")
                wn.listen()
                return                      #shortcut to stop the function
        wn.ontimer(go,15)   #Keeps the go function going
  

def reset():
    mazeRunner.goto(-pathWidth*2,pathWidth*2)   #The maze runner goes to the middle
    mazeRunner.color("red") 
    mazeRunner.clear()  #Clear the previous drawing on mazeRunner
    global timer
    timer=0
    enemyRobot.goto(300,300)    #Enemy goes away
    wn.onkeypress(go,"space")   #To make the game go again
    wn.listen()
    
#Events
#Main Loop Or Game Loop Or Running Code
drawMaze()
#The functions for the conctrols
wn.onkeypress(goUp,"w")
wn.onkeypress(goLeft,"a")
wn.onkeypress(goDown,"s")
wn.onkeypress(goRight,"d")
wn.onkeypress(go,"space")
pauseButtonSquare.onclick(pausingwhat) #If the pause button was clicked
wn.ontimer(updatetimer,interval) #Turn on the timer function
wn.listen()


#Main loop

wn.mainloop()
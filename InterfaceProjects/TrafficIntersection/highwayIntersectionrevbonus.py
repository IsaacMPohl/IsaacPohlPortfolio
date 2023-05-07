import turtle as t
import random
import time

#Initilizing the screen
wn = t.Screen()
wn.bgcolor("grey")
wn.screensize(300,300)
# create two empty lists of turtles, adding to them later
horizontalTurts = []
vert_turtles = []
#Creates the turtle shapes
turtleShapes =["turtle","turtle"]
horizColors=["purple","blue","pink","green"]
vertColors=["yellow","pink","yellow","orange"]
horizontalSpeed=[3.6,3.8,4,4.2,4.4,4.5,4.9,5.3]
verticalSpeed=[3.5,3.7,3.9,4.1,4.3,4.5,4.8,5.2]
collisionDistance =15
timer=10
fontSetup=("Times New Roman",30,"normal")
interval=1000
#Creating the turtles
turt = t.Turtle(shape = "circle")
turt.speed(0)
stopLightHorizontal=t.Turtle(shape="square")
stopLightHorizontal.shapesize(1,2)
stopLightVertical=t.Turtle(shape="square")
stopLightVertical.shapesize(2,1)
#Functions
#Making the cars function
def carMaker(space , heading, heading2,turtlelow,turtlehigh):
    #Goes through each shape in the turtle list
    for shape in turtleShapes:
        #Randomly gerneates a number for the turtle placement can be different at the beggining
        rand=random.randrange(turtlelow,turtlehigh)
        #Creating the turtle based on the given shape
        ht = t.Turtle(shape=shape)
        #Appends the turtle to a list
        horizontalTurts.append(ht)
        #Lift the pen up
        ht.penup()
        #Set the fill color of the turtle and pop it from the list so no repeates
        ht.fillcolor(horizColors.pop())
        #Go to the random place and the space
        ht.goto(rand,space)
        #Set the way the turtle is pointing
        ht.setheading(heading)
        #Creates another random number for the other side
        rand=random.randrange(turtlelow,turtlehigh)
        ht = t.Turtle(shape=shape)
        vert_turtles.append(ht)
        ht.penup()
        ht.fillcolor(vertColors.pop())
        ht.goto(space,rand)
        #Set the second turtle heading
        ht.setheading(heading2)
        #This is how I placed the turtle to the other side of the road
        if space == 20:
            space = 40
        elif space == 40:
            space = 20
        elif space == -20:
            space = -40
        elif space == -40:
            space = -20
    #Returns the turtles
    return(horizontalTurts,vert_turtles)
#Drawing the doted white middle lines function
def whiteLines(x,y):
    y5,x5 = x,y
    #For the left and right lines
    for i in range(2):
        x1=x
        turt.penup()
        turt.goto(x,y)
        turt.pencolor("white")
        for i in range(13):
            turt.pendown()
            x1+=10
            turt.goto(x1,y)
            turt.penup()
            x1+=10
            turt.goto(x1,y)
        y=+30
    #For the up and down lines
    for i in range(2):
        y1=y5
        turt.penup()
        turt.goto(x5,y5)
        turt.pencolor("white")
        for i in range(13):
            turt.pendown()
            y1+=10
            turt.goto(x5,y1)
            turt.penup()
            y1+=10
            turt.goto(x5,y1)
        x5=+30    
#Drawing the two middle yellow lines function
def middleLines(x,y,x1):
    x5,y5,y1 = y,x1,x
    #For the left to right
    for i in range(2):
        turt.penup()
        turt.goto(x,y)
        turt.pencolor("yellow")
        turt.pendown()
        turt.goto(x1,y)
        y +=8
    #For the up and down
    for i in range(2):
        turt.penup()
        turt.goto(x5,y5)
        turt.pencolor("yellow")
        turt.pendown()
        turt.goto(x5,y1)
        x5 +=8
#Drawing the black boards of the roads
def outerLines(x,y):
    x5,y5=y,x
    turt.pencolor("black")
    #For the left to right
    for i in range(2):
        turt.penup()
        turt.goto(x,y)
        turt.pendown()
        x1=x+250
        turt.goto(x1,y)
        y +=110
    #For the up and down
    for i in range(2):
        turt.penup()
        turt.goto(x5,y5)
        turt.pendown()
        y6=y5+250
        turt.goto(x5,y6)
        x5 +=110   
#Drawing the stop light
def stopLight(x,y):
    stopLightHorizontal.penup()
    stopLightVertical.penup()
    stopLightHorizontal.goto(x,0)
    stopLightHorizontal.color("red")
    stopLightVertical.goto(0,y)
    stopLightVertical.color("green")
    stopLightVertical.stamp()

def updatetimer():
    #global is to let this function know to go look at a global var
    global timer
    if timer<=0:
        print(timer)
        stopLightHorizontal.color("green")
        stopLightVertical.color("red")
        #time.sleep(5000)
        timer=10
        wn.ontimer(updatetimer,interval)
    elif timer<=10 and timer>=5:
        print(timer)
        timer-=1
        stopLightHorizontal.color("red")
        stopLightVertical.color("green")
        wn.ontimer(updatetimer,interval)
    else:
        timer-=1
        print(timer)
        stopLightHorizontal.color("green")
        stopLightVertical.color("red")
        #print(time)
        #We need to recusively run this function
        #timekeeper gets the screen's ontimer and resets the command and interval
        wn.ontimer(updatetimer,interval)
        
#events
#Runs the functions to draw the screens
#stopLight(40,40)
stopLight(0,0)

whiteLines(-300,-30)
whiteLines(60,-30)
middleLines(-300,0,-45)
middleLines(45,0,300)
outerLines(-300,-50)
outerLines(60,-50)
#Hides the turtle
turt.hideturtle()
#Runs the functions to make the cars
horizontalTurts,vert_turtles = carMaker(-20,0,90,-250,-50)
horizontalTurt,vert_turtles = carMaker(20,180,270,50,250)

#Moving the turtles
#Randomly shuffles the list for the speeds of the turtles can be different for turtle can collide with each other more
random.shuffle(horizontalSpeed)
random.shuffle(verticalSpeed)
#horizontalSpeed=random.shuffle(horizontalSpeed)
#Keep going through a loop 

wn.ontimer(updatetimer,interval)
while horizontalTurts !=[] and vert_turtles !=[]:
    #This is for the turtle knows what number in the speed list it should go
    hSI=0 #horizontalSpeedIrration
    vSI=0 #verticalSpeedIrration
    #Runs through a nested four loop which runs through each turtle
    for h in horizontalTurts:
        #Sets the verticalSpeedIrration back to 0
        vSI=0 
        for v in vert_turtles:
            #print(stopLightVertical.color()[0])
            if stopLightVertical.color()[0]=="red" and v.xcor()>0 and v.ycor()>-20:
                print("i")
                v.fd(verticalSpeed[vSI])    
                #h.fd(horizontalSpeed[hSI])
            elif stopLightVertical.color()[0]=="red" and v.xcor()<0 and v.ycor()<20:
                print("i")
                v.fd(verticalSpeed[vSI])    
                #h.fd(horizontalSpeed[hSI])
            elif stopLightVertical.color()[0]=="green" and h.xcor()>-20 and v.ycor()>0:
                print("i")
                #v.fd(verticalSpeed[vSI])    
                h.fd(horizontalSpeed[hSI])
            elif stopLightVertical.color()[0]=="green" and h.xcor()<20 and v.ycor()<0:
                print("i")
                #v.fd(verticalSpeed[vSI])    
                h.fd(horizontalSpeed[hSI])
            if stopLightVertical.color()[0]=="green":
                v.fd(verticalSpeed[vSI])   
            elif stopLightHorizontal.color()[0]== "green":
                h.fd(verticalSpeed[vSI])     

            #v.fd(verticalSpeed[vSI])    
            #h.fd(horizontalSpeed[hSI])
            ##The turtle moves forward the number it should base on the loop
            

            #v.fd(verticalSpeed[vSI])    
            #h.fd(horizontalSpeed[hSI])
            #Checks if the turtle move at the outside of the screen  
            if h.xcor()>250:
                #Moves the turtle back at the begginging
                h.goto(-250,h.ycor())
                #Re suffles the loop to change all the car speeds
                random.shuffle(horizontalSpeed)
            #If turtle hits the left side
            if h.xcor()<-250:
                h.goto(250,h.ycor())
                random.shuffle(horizontalSpeed)
            #If turtle hit the bottum
            if v.ycor()<-250:
                v.goto(v.xcor(),250) 
                random.shuffle(verticalSpeed)
            #If turtle hits the top of the screen
            if v.ycor()>250:
                v.goto(v.xcor(),-250) 
                random.shuffle(verticalSpeed)
            #Checks for the collisions if they are in a range of each other
            if (abs(h.xcor() - v.xcor()) < collisionDistance):
                if(abs(h.ycor()-v.ycor())<collisionDistance):     
                    #Fill the car colors to red            
                    h.fillcolor("red")
                    v.fillcolor("red")
                    #Stamp them
                    h.stamp()
                    v.stamp()    
                    #Hide the turtles
                    h.hideturtle()
                    v.hideturtle()
                    #Remove the turtles from the list
                    horizontalTurts.remove(h)  
                    vert_turtles.remove(v)
                    #Removes the spefic speed of the car so the car can always remain constant until one crashes
                    del horizontalSpeed[hSI]
                    del verticalSpeed[vSI]
            #Add 1 to move the turtle speed to the next item in the list
            vSI+=1
        hSI+=1
    






wn = t.Screen()
wn.mainloop()


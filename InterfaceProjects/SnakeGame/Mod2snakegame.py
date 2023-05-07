#import 
import turtle as t 
import time
import random 
#game config and globals
delay=0.1
bodyParts=[]    #The two lists to save the body parts of the snakes
bodyParts2=[]

#object creation
wn=t.Screen()
wn.title("Snake 2 Modifications")
wn.bgcolor("gray")
wn.setup(width=600,height=600)

#This is the first snake
head = t.Turtle(shape="square")
head.speed(1)
head.penup()
head.direction = "stop"

#This is the 2nd player or the anomious snake 
head2 = t.Turtle(shape="square")
head2.speed(1)
head2.penup()
head2.direction = "stop"

#This is the head to go infront of the second head to tell if you are going to collide
head2VI = t.Turtle(shape="square")
head2VI.speed(1)
head2VI.penup()
head2VI.direction = "stop"
head2VI.color("blue")
head2VI.hideturtle()

food=t.Turtle()
food.speed(0)
food.shape("circle")
food.shapesize(.5,.5) #scales the turtle obj by 50%
food.color("red")
food.penup()
food.goto(100,100)

#functions
#The snake movements for the first head
def up():
    #In maze runner we used setheading
    if head.direction != "down":
        head.direction="up"
def left():
    if head.direction != "right":
        head.direction="left"
def right():
    if head.direction != "left":
        head.direction="right"
def down():
    if head.direction != "up":
        head.direction="down"
#The snake movment for the second head when player in pvp mode
def up2():
    #In maze runner we used setheading
    if head2.direction != "down":
        head2.direction="up"
def left2():
    if head2.direction != "right":
        head2.direction="left"
def right2():
    if head2.direction != "left":
        head2.direction="right"
def down2():
    if head2.direction != "up":
        head2.direction="down"

#This moves the heads
def move():
    if head.direction=="up":
        head.sety(head.ycor()+20) 
    elif head.direction=="down":
        head.sety(head.ycor()-20)
    elif head.direction=="right":
        head.setx(head.xcor()+20)
    elif head.direction=="left":
        head.setx(head.xcor()-20)
    if head2.direction=="up":
        head2.sety(head2.ycor()+20) 
    elif head2.direction=="down":
        head2.sety(head2.ycor()-20)
    elif head2.direction=="right":
        head2.setx(head2.xcor()+20)
    elif head2.direction=="left":
        head2.setx(head2.xcor()-20)

#This hides the body parts if the snake hits the edge or the other snake or itself
def hideTheBodyParts():
    global bodyParts
    head.goto(0,0)  #Resets the head back to the middle
    head.direction = "stop"
    #Goes through each snake part and moves it off the screen
    for eachPart in bodyParts:
        eachPart.goto(1000,1000)
    #Resets the bodypart list
    bodyParts=[]
#This hides the 2nd body parts if snake 2 hits the edge or the other snake or itself
def hideTheBodyParts2():
    global bodyParts2
    head2.goto(0,0)
    head2.direction = "stop"
    for eachPart in bodyParts2:
        eachPart.goto(1000,1000)
    bodyParts2=[]

#This is the computer movment for head 2
def CPMovement():
    #Gets the head origional heading before it changes it the first time
    previoushead=head2.heading()
    #Change the heading based on where the food is (Goes up and down first) and then (goes left and right)
    if head2.pos()[1] >= food.pos()[1]+15 and head2.heading()!=90:
        head2.setheading(270)
    elif head2.pos()[1] < food.pos()[1]-15 and head2.heading()!=270:
        head2.setheading(90)
    elif head2.pos()[0] >= food.pos()[0]+15 and head2.heading()!=0:
        head2.setheading(180)
    elif head2.pos()[0] < food.pos()[0]-15 and head2.heading()!=180:
        head2.setheading(0)
    #If non it might be stuck because it is in the middle of +15 and -15 such as 0, so needs to get more precious
    else:
        if head2.pos()[1] >= food.pos()[1] and head2.heading()!=90:
            head2.setheading(270)
        elif head2.pos()[1] < food.pos()[1] and head2.heading()!=270:
            head2.setheading(90)
        elif head2.pos()[0] >= food.pos()[0] and head2.heading()!=0:
            head2.setheading(180)
        elif head2.pos()[0] < food.pos()[0] and head2.heading()!=180:
            head2.setheading(0) 
    #The inviuable head go to the head position and set the heading to the head2 postion and go forward
    head2VI.goto(head2.pos())
    head2VI.setheading(head2.heading())
    head2VI.fd(20)

    #Goes through each body part of snake two
    for bodyPart2 in bodyParts2: 
        #Check if the body part is going to be collided with the invsible head2 and not the first and second body part because it is inposible to hit and for no errors
        if head2VI.distance(bodyPart2)<20 and bodyPart2!=bodyParts2[0 ] and bodyPart2!=bodyParts2[1]:
            #If it does hit, move the invible head to head2 postion and check if it can go right
            head2VI.goto(head2.pos())
            head2VI.setheading(previoushead+90)
            head2VI.fd(20)
            #If it can go right set head2 heading to the right
            if head2VI.distance(bodyPart2)>=20 and bodyPart2!=bodyParts2[0 ] and bodyPart2!=bodyParts2[1] :
                head2.setheading(head2VI.heading())
            #Checking if the heading can go left
            head2VI.goto(head2.pos())
            head2VI.setheading(previoushead-90)
            head2VI.fd(20)
            if head2VI.distance(bodyPart2)>=20  and bodyPart2!=bodyParts2[0 ] and bodyPart2!=bodyParts2[1]:
                head2.setheading(head2VI.heading())
            #Check if the head can go the previous head forward
            head2VI.goto(head2.pos())
            head2VI.setheading(previoushead)
            head2VI.fd(20)
            if head2VI.distance(bodyPart2)>=20  and bodyPart2!=bodyParts2[0 ] and bodyPart2!=bodyParts2[1]:
                head2.setheading(head2VI.heading())
    #Move head2 forward
    head2.fd(20)

#events
#Ask the user if they want to do player vs player or player vs computer
ui=input("Type in (PVP) if you want to play with someone, type in (PVC) if you want to play with the computer, type in (Auto) for just a autonomous snake, or type in (Normal) if you want to play by yourself?")
if ui != "Auto":
    #The keybinds for player 1
    wn.onkeypress(up,"w")
    wn.onkeypress(left,"a")
    wn.onkeypress(right,"d")
    wn.onkeypress(down,"s")
#If the user wants to player player vs player, unlock key binds
if ui=="PVP":
    wn.onkeypress(up2,"Up")
    wn.onkeypress(left2,"Left")
    wn.onkeypress(right2,"Right")
    wn.onkeypress(down2,"Down")
wn.listen()

#mainloop 
while True:
    wn.update() #updates or refreshes the screen
    #Border Collision FOR THE heads
    if head.xcor()<-290 or head.xcor()>290 or head.ycor()<-290 or head.ycor()>290:
       hideTheBodyParts()
    if head2.xcor()<-290 or head2.xcor()>290 or head2.ycor()<-290 or head2.ycor()>290:
       hideTheBodyParts2() 
    #If the heades collides with the food
    if head.distance(food)<20: #returns the distance between the objects
        #food moves
        food.goto(random.randint(-290,290),random.randint(-290,290))
        #grow a body part 
        part=t.Turtle(shape="square")
        part.speed(0)
        part.penup()
        bodyParts.append(part)
    if head2.distance(food)<20: #returns the distance between the objects
        #food moves
        food.goto(random.randint(-290,290),random.randint(-290,290))
        #grow a body part 
        part=t.Turtle(shape="square")
        part.speed(0)
        part.penup()
        bodyParts2.append(part)

    #Move the body parts - follow the leader  
    #move the butt to the neck  
    for i in range(len(bodyParts)-1,0,-1):
        x=bodyParts[i-1].xcor()
        y=bodyParts[i-1].ycor()
        bodyParts[i].goto(x,y)
    #move the neck to the head
    if len(bodyParts)>0:
        x=head.xcor()
        y=head.ycor()
        bodyParts[0].goto(x,y)
    #move the butt to the neck  
    for i in range(len(bodyParts2)-1,0,-1):
        x=bodyParts2[i-1].xcor()
        y=bodyParts2[i-1].ycor()
        bodyParts2[i].goto(x,y)
    #move the neck to the head
    if len(bodyParts2)>0:
        x=head2.xcor()
        y=head2.ycor()
        bodyParts2[0].goto(x,y)
    #Calles up the move function to move the heads based on the headings
    move()
    #If the user wants to player player vs computer, calls up the function
    if ui=="PVC" or ui == "Auto":
        CPMovement()
    #Checks if the snake hits itself
    for bodyPart in bodyParts:
        if head.distance(bodyPart)<10:
            hideTheBodyParts()
        for bodyPart2 in bodyParts2:
            if head.distance(bodyPart2)<10:
                hideTheBodyParts()
            if head2.distance(bodyPart)<10:
                hideTheBodyParts2()
    for bodyPart2 in bodyParts2:
            if head2.distance(bodyPart2)<10:
                hideTheBodyParts2()
    #Delays the function 
    time.sleep(delay)
#   a115_robot_maze.py
import turtle as trtl
import math
#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5
total = 0
#------ robot commands
def move():
  robot.dot(10)
  robot.fd(50)

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

def moveBack(oldrobot): 
    
    if int(robot.position()[0]) == -50  and int(robot.position()[1]) ==-50:
        robot.goto(int(oldrobot[0]),int(oldrobot[1]))
    elif int(robot.position()[0]) == 50  and int(robot.position()[1]) == -100:
        robot.goto(int(oldrobot[0]),int(oldrobot[1]))
    elif int(robot.position()[0]) == 0  and int(robot.position()[1]) == 0 :
        robot.goto(int(oldrobot[0]),int(oldrobot[1]))
    elif int(robot.position()[0]) == 100  and int(robot.position()[1]) == 0:
        robot.goto(int(oldrobot[0]),int(oldrobot[1])) 
    elif int(robot.position()[0]) == 0  and int(robot.position()[1]) == 100 or int(robot.position()[0]) == -0  and int(robot.position()[1]) == 100 :
        robot.goto(int(oldrobot[0]),int(oldrobot[1])) 
    elif int(robot.position()[0]) == -100  and int(robot.position()[1]) == 100:
        robot.goto(int(oldrobot[0]),int(oldrobot[1]))  
        
def winFunction():
    if int(robot.position()[0]) == -50  and int(robot.position()[1]) == 0:
        robot.stamp()
    elif int(robot.position()[0]) == 100  and int(robot.position()[1]) == 100:
        robot.stamp()
    elif int(robot.position()[0]) == 100  and int(robot.position()[1]) == -100:
        robot.stamp()
    


def moveUP():
  oldrobot = robot.position()
  robot.setheading(90)
  
  robot.fd(50)
  robot.setposition((round(robot.position()[0]  /5)*5),(round(robot.position()[1]  /5)*5))
  print(robot.position())
  winFunction()
  moveBack(oldrobot)
def moveDown():
  oldrobot = robot.position()
  robot.setheading(270)
  robot.fd(50)
  robot.setposition((round(robot.position()[0]  /5)*5),(round(robot.position()[1]  /5)*5))
  print(robot.position())
  winFunction()
  moveBack(oldrobot)
def moveLeft():
  oldrobot = robot.position()
  robot.setheading(180)
  robot.fd(50)
  robot.setposition((round(robot.position()[0]  /5)*5),(round(robot.position()[1]  /5)*5))
  print(robot.position())
  winFunction()
  moveBack(oldrobot)

def moveRight():
  oldrobot = robot.position()
  robot.setheading(0)
  robot.fd(50)
  robot.setposition((round(robot.position()[0]  /5)*5),(round(robot.position()[1]  /5)*5))
  print(robot.position())
  winFunction()
  moveBack(oldrobot)



#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "robot.gif"
wn.addshape(robot_image)

#----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

#---- TODO: change maze here
wn.bgpic("maze4.png") # other file names should be maze2.png, maze3.png

#   1st loop
'''
def left():
  robot.goto(robot.xcor(),-10)
def right():
  robot.goto(robot.xcor(),10)
def up():
  robot.goto(robot.xcor(),10)
def down():
  robot.goto(robot.xcor(),-10)
'''
#robot.goto(-50,-50)
wn.onkeypress(moveLeft,"a")
wn.onkeypress(moveRight,"d")
wn.onkeypress(moveUP,"w")
wn.onkeypress(moveDown,"s")

#print(robot.getscreen)
print(robot.position()[0])
print(robot.position()[1])

wn.listen()

#---- end robot movement 
wn.mainloop()

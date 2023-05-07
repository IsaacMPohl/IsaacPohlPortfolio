#   a115_robot_maze.py
import turtle as trtl

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move():
  robot.dot(10)
  robot.fd(50)

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

def moveUP():
  robot.setheading(90)
  robot.fd(50)
def moveDown():
  robot.setheading(270)
  robot.fd(50)
def moveLeft():
  robot.setheading(180)
  robot.fd(50)
def moveRight():
  robot.setheading(0)
  robot.fd(50)



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
wn.bgpic("maze1.png") # other file names should be maze2.png, maze3.png

#   1st loop
#for step in range(4): # forward 3
#  move()
#for i in range(3):
#  turn_left()
#for i in range(4):
#  move()

#   1st loop 2nd version
for i in range(4):
  move()
  for i in range(3):
    turn_left()
  move()
  turn_left()

#   self control loops
#actions={"w":moveUP(),
#         "a":moveLeft(),
#         "s":moveDown(),
#         "d":moveRight()
#}

#while True:
#  ui=input("w,a,s,d")
#  #obviously, check for user input
#  #actions[ui]
#  if ui == "w":
#    moveUP()
#  elif ui == "a":
#    moveLeft()
#  elif ui == "s":
#    moveDown()
#  elif ui == "d":
#    moveRight()


#2nd loop

#---- end robot movement 
wn.mainloop()

import turtle as t
from turtle import *
import random as r


tree = t.Turtle()
wn = t.Screen()
wn.screensize(250, 250)
wn.bgcolor('black')
pen1 = Pen()
ornaments = t.Turtle() 
snowman = t.Turtle()
snowFalling = t.Turtle()
star = t.Turtle()
present = t.Turtle()
otherObjects = t.Turtle()
picture = t.Turtle()


#Snow falling from the sky
def snow(numberOfFakes,colorOfSnow,farLeft,farRight,upper,lower,speed,variation,ground):
    snowFlakes = []
    for i in range(numberOfFakes):
        s = t.Turtle(shape="circle")
        s.color(colorOfSnow)
        s.speed(0)
        s.penup()
        s.goto(r.randint(farLeft,farRight), r.randint(lower,upper)) #r->random module
        #s.goto(r.randint(-wn.window_width()/2,wn.window_width()/2),r.randint(250,400)) #r->random module

        snowFlakes.append(s)

    #runningcode
    while True:
        for s in snowFlakes:
            newX=s.xcor()+r.randint(-variation,variation)
            newY=s.ycor()+r.randint(-speed,0)
            s.goto(newX,newY)
            if s.ycor()<-ground:
         #       s.stamp()
                s.sety(r.randint(lower,upper))


#Adding images
#wn.addshape('Merry-Christmas-Gif-10-wordsjustforyou-191220.gif')
#picture.shape('Merry-Christmas-Gif-10-wordsjustforyou-191220.gif')
wn.addshape('1839598395christmas-tree-animated-gif-14.gif')
picture.shape('1839598395christmas-tree-animated-gif-14.gif')
picture.up()
picture.goto(180,140)

#Making the text
pen1.up()
pen1.goto(0,140)
pen1.down()
pen1.color('red')
pen1.write("Merry Christmas",move = False, align="center" , font=("Verdana", 30, "normal"))
pen1.hideturtle()

#Making the tree base
l = 12.5
h = 2
f = 0
tree.shape('square')
tree.color('brown')
tree.right(90)
tree.shapesize(2,2)
tree.forward(80)
tree.right(180)
t1 = tree.clone()
tree.forward(40)

#Making the tree
for i in range(3):
  t1 = tree.clone()
  tree.shapesize(l, h)
  tree.color('green')
  tree.forward(f)
  l -= 4
  f = 40

#Making the Star
star.color('yellow')
star.up()
star.goto(-40,110)
star.down()
star.pensize(20)
f=80
r=144
for i in range(8):
  star.forward(f)
  star.right(r)
star.goto(-5,90)
  
    
#Making the ornaments
ornaments.shape('circle')
ornaments.color('red')
ornaments.up()
ornaments.goto(5,30)
o1 = ornaments.clone()
ornaments.goto(-10,-20)
o1 = ornaments.clone()
ornaments.goto(40,0)
o1 = ornaments.clone()
ornaments.goto(-80,-45)
o1 = ornaments.clone()
ornaments.goto(70,-40)
o1 = ornaments.clone()
ornaments.goto(-35,20)
o1 = ornaments.clone()
ornaments.goto(15,-50)
o1 = ornaments.clone()
ornaments.goto(-40,-15)
o1 = ornaments.clone()

#making the snowman
snowman.shape('circle')
snowman.up()
snowman.color("white")
l = 3
h = 3
f = -50
for i in range(3):
  snowman.shapesize(l,h)
  snowman.goto(-190,f)
  s1 = snowman.clone() 
  l2 = l
  l-=.75
  h-=.75
  #f -=.75
  f += ((l*10) + (l2*10))
l = .80
h = .80
f = -35
for i in range(3):
  snowman.shapesize(l,h)
  snowman.color('grey')
  snowman.goto(-190,f)
  s1 = snowman.clone() 
  f += (20)

snowman.goto(-195,40)
snowman.shapesize(.25,.25)
s1 = snowman.clone() 
snowman.goto(-185,40)
snowman.shapesize(.25,.25)
s1 = snowman.clone()

snowman.shape('triangle')
snowman.color('orange')
snowman.goto(-188,32)
snowman.shapesize(.30,.60)
#snowman.right(90)
s1 = snowman.clone() 


#Present 
present.shape('square')
present.color('red')
present.up()
present.goto(-100,-100)
present.shapesize(3,3)
s1 = present.clone()
present.shapesize(1,3)
present.color('yellow')
s1 = present.clone()

present.goto(-100,-65)
present.shapesize(1,1)
s1 = present.clone()

#Porson Sleding
otherObjects = t.Turtle()
otherObjects.shape('square')
otherObjects.color('brown')
otherObjects.up()
otherObjects.goto(80,-200)
otherObjects.shapesize(1,4)
s1 = otherObjects.clone()
otherObjects.shapesize(2,.5)
otherObjects.goto(110,-190)
s1 = otherObjects.clone()
otherObjects.goto(40,-200)
otherObjects.down()
otherObjects.right(180)
otherObjects.color("red")
otherObjects.forward(300)
otherObjects.up()
otherObjects.goto(80,-170)
otherObjects.shapesize(2,1)
s1 = otherObjects.clone()
otherObjects.shape('circle')
otherObjects.shapesize(1,1)
otherObjects.goto(80,-140)
otherObjects.color('yellow')
s1 = otherObjects.clone()


#Cookie plate
otherObjects.goto(120,-90)
otherObjects.shapesize(1.5,3)
otherObjects.color('white')
s1 = otherObjects.clone()
otherObjects.goto(120,-90)
otherObjects.shapesize(.5,.5)
otherObjects.color('brown')
s1 = otherObjects.clone()
otherObjects.goto(130,-85)
s1 = otherObjects.clone()
otherObjects.goto(110,-80)
s1 = otherObjects.clone()
otherObjects.goto(135,-95)
s1 = otherObjects.clone()

#snow pile
otherObjects.color('white')
otherObjects.goto(140,-205)
s1 = otherObjects.clone()
otherObjects.goto(150,-205)
s1 = otherObjects.clone()
otherObjects.goto(160,-205)
s1 = otherObjects.clone()
otherObjects.goto(140,-195)
s1 = otherObjects.clone()
otherObjects.goto(150,-195)
s1 = otherObjects.clone()
otherObjects.goto(160,-195)
s1 = otherObjects.clone()

#fire place 
otherObjects.shape('square')
otherObjects.shapesize(9,3)
otherObjects.goto(220,0)
otherObjects.color('grey')
s1 = otherObjects.clone()
otherObjects.shapesize(5,.25)
otherObjects.color('red')
otherObjects.goto(210,-40)
s1 = otherObjects.clone()
otherObjects.color('brown')
otherObjects.goto(220,-80)
otherObjects.shapesize(1,2)
s1 = otherObjects.clone()

#Snow on buttom 
otherObjects.color('white')
otherObjects.goto(0,-250)
otherObjects.shapesize(3.40,25)
  #3.5,25)
s1 = otherObjects.clone()


import random as r 

snow(15,"white",-(230),(250),330,210,30,5,280)


#closing the loop
wn.mainloop()
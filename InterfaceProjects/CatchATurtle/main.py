#----inport statments----
import turtle as t
import random as r
import leaderboard as lb 

#----game configurations----- (global variables)
wn=t.Screen()
timer=5
fontSetup=("Times New Roman",30,"normal")
interval=1000
score=0
FILENAME="Database.txt"     #constant variable, don't change it 

#----inialize turtles----- (initialize objects)
bob = t.Turtle()
bob.shape("turtle")
bob.shapesize(2)
bob.fillcolor("purple")
bob.speed(0)
bob.penup()

timekeeper=t.Turtle()
timekeeper.penup()
timekeeper.hideturtle()
timekeeper.goto(-100,200)
timekeeper.pendown()
timekeeper.speed(0)

scorekeeper=t.Turtle()
scorekeeper.penup()
scorekeeper.hideturtle()
scorekeeper.goto(100,200)
scorekeeper.pendown()
scorekeeper.speed(0)

#----functions-----
#the command to run when there is an event
def updatetimer():
    #global is to let this function know to go look at a global var
    global timer
    timekeeper.clear()
    if timer<=0:
        manageLeaderboard()
        timekeeper.write("Times UP!",font=fontSetup)
        bob.stamp()
        bob.hideturtle()
        
    else:
        timer-=1
        timekeeper.write(f"timer: {timer}",font=fontSetup)
        #We need to recusively run this function
        #timekeeper gets the screen's ontimer and resets the command and interval
        timekeeper.getscreen().ontimer(updatetimer,interval)
    
def updateScore():
    #global is to let this function know to go look at a global var
    global score
    score+=1
    scorekeeper.clear()
    #object.write("message",options)         ("font type       ",size,"style")
    scorekeeper.write(f"Score: {score}",font=fontSetup)
    
#WHEN YOU USE onClick  EVENT, YOU MUST GIVE THE FUNCTION THE x,y
def bobClick(x,y):
    print("bob was clicked")
    print(x,y)
    moveBob()
    updateScore()
    
    
def moveBob():
    #randomly moving bob
    newX=r.randint(-300,300)
    newY=r.randint(-300,300)
    bob.goto(newX,newY)

#Game over function
def manageLeaderboard():
    global score
    #get the data from the txt file 
    namesList=lb.getNames(FILENAME)
    scoresList=lb.getScores(FILENAME)
    
    #check to see if you made the leaderboard
    
    #update the leaderboard
    if (len(scoresList)<5 or score>=int(scoresList[-1])): 
        name=input("Congrats, you're on the board! \n\tName Please:")
        lb.updateLeader(FILENAME,namesList,scoresList,name,score)
    else:
        print("Did not make leaderboard")
    #display the leaderboard
    lb.draw_leaderboard(False,namesList,scoresList,scorekeeper,10)
    
    
    
#----events-----
#object.onclick(command)->we can reset this anytime we want
wn.ontimer(updatetimer,interval)
bob.onclick(bobClick)

#-----main loop-----(running code)
wn.mainloop()

'''
    1. Click the turtle
    2. move the turtle
    3. Update Score
    4. Countdonwn
'''
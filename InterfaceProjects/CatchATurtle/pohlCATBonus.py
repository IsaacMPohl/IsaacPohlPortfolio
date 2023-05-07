#----inport statments----
import turtle as t
import random as r
import leaderboard as lb 


#song = AudioSegment.from_wav("gameclickmusic.wav")
#wav_file = AudioSegment.from_file(file = "gameclickmusic.wav", format = "wav")
#play(wav_file)

#----game configurations----- (global variables)
wn=t.Screen()
timer=5
fontSetup=("Times New Roman",30,"normal")
interval=1000 #The interval for the timer
score=0
FILENAME="Database.txt"     #constant variable, don't change it 
#This variable is how we check if the screen click is the same as the turtle click to find the accuracy
x1=10000
y1=10000
totalOffClicks=0 #To find the accurary
turtle_image2 = "turtle3.gif"

#----inialize turtles----- (initialize objects)


#Bob is the turtle which the player clicks on
bob = t.Turtle()
bob.shape("turtle")
bob.shapesize(5)
bob.fillcolor("purple")
bob.speed(0)
bob.penup()

wn.addshape(turtle_image2)

turtleGif = t.Turtle()
turtleGif.shape(turtle_image2)
turtleGif.speed(0)
turtleGif.penup()

#Time keeper draws the time on the screen
timekeeper=t.Turtle()
timekeeper.penup()
timekeeper.hideturtle()
timekeeper.goto(-100,200)
timekeeper.pendown()
timekeeper.speed(0)

#The scorekeeper draws the score on the screen
scorekeeper=t.Turtle()
scorekeeper.penup()
scorekeeper.hideturtle()
scorekeeper.goto(100,200)
scorekeeper.pendown()
scorekeeper.speed(0)

#The accuracy keeper draws the accuracy percantage on the screen
accuracyKeeper=t.Turtle()
accuracyKeeper.penup()
accuracyKeeper.hideturtle()
accuracyKeeper.goto(100,150)
accuracyKeeper.pendown()
accuracyKeeper.speed(0)

#----functions-----
#the command to run when there is an event
def updatetimer():
    #global is to let this function know to go look at a global var
    global timer
    #Clear the previous time
    timekeeper.clear()
    #If the time is less or equal to 0
    if timer<=0:
        #Print out the leaderboard
        manageLeaderboard()
        timekeeper.write("Times UP!",font=fontSetup)
        #Stamp and hide the turtle for no future clicks
        bob.stamp()
        bob.hideturtle()
        turtleGif.hideturtle()
        
    #If the time is not over
    else:
        #Minus one from time
        timer-=1
        timekeeper.write(f"timer: {timer}",font=fontSetup)
        #We need to recusively run this function
        #timekeeper gets the screen's ontimer and resets the command and interval
        timekeeper.getscreen().ontimer(updatetimer,interval)


def updateScore():
    #global is to let this function know to go look at a global var
    global score
    #Add one to the score
    score+=1
    #Clear the previous score
    scorekeeper.clear()
    #object.write("message",options)         ("font type       ",size,"style")
    scorekeeper.write(f"Score: {score}",font=fontSetup)

def updateBobSize():
    #If bob is not the smallest size, make it 2x as small
    if bob.shapesize()[0] != .625:
        bob.shapesize(bob.shapesize()[0]/2)
    else:
        #If it is that size, reset to normal size
        bob.shapesize(5)
        
#WHEN YOU USE onClick  EVENT, YOU MUST GIVE THE FUNCTION THE x,y
def bobClick(x,y):
    #If the score is 0, turn on the timer which will allow only when the turtle is click start the game
    if score == 0:
        wn.ontimer(updatetimer,interval)
    print("bob was clicked")
    #Sets the x1 and y1 to global and assigns it to the x,y to compare it later on to find the hits on the turtle compare to the hits on the screen
    global x1
    global y1
    x1=x
    y1=y
    #Stamps bob with red color 
    bob.fillcolor("red")
    bob.stamp()
    
    #Makes bob back to purple
    bob.fillcolor("purple")
    #Update bob size
    updateBobSize()
    #Move bob
    moveBob()
    updateScore()
    #Sets the background color back to white
    wn.bgcolor("white")
    
    
def moveBob():
    #randomly moving bob
    newX=r.randint(-280,280)
    newY=r.randint(-280,280)
    #Swicht the screen to red for a moment to let users know bob has been hit 
    wn.bgcolor("red")
    #If bob is touching the text for the score display, time display, or accurary display
    while newX>-200 and newX<300 and newY>100 and newY<275:
        newX=r.randint(-280,280)
        newY=r.randint(-280,280)
    #Bob goes to the new generated number
    turtleGif.goto(newX,newY)
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

#Runs everytime the screen gets click
def postion(x,y):
    #As long as time is not 0, so the game is going on
    if timer>0:
        global totalOffClicks
        #If the x and y is not eqall to the x1 and y1 which is when the turtle was clicked, then the player missed
        if x!=x1 and y!=y1:
            totalOffClicks+=1
        #Finding the accuracy by taking the (score/ the total clicks) times 100
        accuracy=((score/(totalOffClicks+score))*100)
        #Clear the previus accuracy text
        accuracyKeeper.clear()
        #object.write("message",options)         ("font type       ",size,"style")
        accuracyKeeper.write(f"Accuracy: {accuracy}",font=fontSetup)
        
#----events-----
#object.onclick(command)->we can reset this anytime we want
#Everytime which bob is click
bob.onclick(bobClick)
#Everytime the screen is click
t.onscreenclick(postion)
wn.listen()

#-----main loop-----(running code)
#Print instructions
print("Click the small purple unantimated turtle, in the center of the outer turtle")
wn.mainloop()

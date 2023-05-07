import turtle as t
import Generation as g
import inputChecker as C
import time 
import random as r
print(r.randint(0,3))
wn=t.Screen()
screenHeight = 300
screenWidth = 300
wn.screensize(screenWidth,screenHeight)
fontSetup=("Times New Roman",40,"normal")
fontSideSetup=("Times New Roman",20,"normal")
fontMiniSetup=("Times New Roman",10,"normal")
numberOfTurts = 9
listColor = ["","blue","red","yellow","yellow","blue","red","red","yellow","blue","blue","red","yellow","yellow","blue","red","red","yellow","blue"]
rightfull=False
itemCoords=[[0,0],[0,0]]
gamemode = 0
lineNumbers=4
total= 0
gameBoardSoFar=['','','','','','','','','','','','']

def drawHomeScreen():
    turt = t.Turtle(shape="square")
    wn.bgpic("mainMenu.png")
    turt.hideturtle()
    turt.penup()
    turt.goto(-screenWidth+40,screenHeight-100)
    turt.pendown()
    turt.pencolor('Black')
    turt.write("Welcome to Memory!",font=fontSetup)
    turt.penup()
    turt.goto(-screenWidth,70)
    turt.pendown
    turt.pencolor("Blue")
    turt.write("Click Me For Intructions!", font=("Times New Roman",15,"normal"))
    turt.penup()
    turt.goto(-screenWidth,-70)
    turt.pendown()
    turt.pencolor("Red")
    turt.write("Click Me For Credits!", font=("Times New Roman",15,"normal"))
    turt.penup()
    turt.goto(20,70)
    turt.pendown()
    turt.pencolor("Green")
    turt.write("Click Me To Play Two Player!", font=("Times New Roman",15,"normal"))
    turt.penup()
    turt.goto(20,-70)
    turt.pendown()
    turt.pencolor("Yellow")
    turt.write("Click Me To Play One Player!", font=("Times New Roman",15,"normal"))
    turt.penup()
    turt.pencolor("Black")

    turt.pensize(5)
    turt.goto(0,screenHeight-150)
    turt.pendown()
    turt.goto(0,-screenHeight+150)
    turt.penup()
    turt.pensize(5)
    turt.goto(-screenWidth , 0)
    turt.pendown()
    turt.goto(screenWidth,0)

def instructions():
    turt2 = t.Turtle()
    memoryimg = "memoryGame.gif"
    wn.addshape(memoryimg)
    turt2.shape(memoryimg)
    turt = t.Turtle(shape="square")
    turt.hideturtle()
    turt.penup()
    turt.goto(-screenWidth+40,screenHeight-100)
    turt.pendown()
    turt.write("How To Play Memory!",font=fontSetup)
    turt.penup()
    turt.goto(-screenWidth,40)
    turt.pendown()
    turt.write("The goal of memory is to find and remember the numbers by selecting 2 per turn.",font=fontMiniSetup)
    turt.penup()
    turt.goto(-screenWidth,20)
    turt.pendown()
    turt.write("Each turn you will have to select the coordinates of the card you wish to guess.",font=fontMiniSetup)
    turt.penup()
    turt.goto(-screenWidth,0)
    turt.pendown()
    turt.write("Every card has a match to make sure to remember what you find!",font=fontMiniSetup)
    turt.penup()
    turt.goto(-screenWidth,-20)
    turt.pendown()
    turt.write("The goal of memory is to find and remember the numbers by selecting 2 per turn.",font=fontMiniSetup)
    turt.penup()
    turt.goto(-screenWidth,-40)
    turt.pendown()
    turt.write("When a player makes a match, they score a point! The game is over when all cards have been Matched.",font=fontMiniSetup)
    turt.penup()
    turt.goto(-screenWidth,-60)
    turt.pendown()
    turt.write("The player with the most points wins! good luck!",font=fontMiniSetup)
    turt.penup()
    turt.goto(-screenWidth+10,-screenHeight+50)
    turt.pendown()
    turt.write("Click Any Where On The Screen To Go Back", font= fontSideSetup)
    turt.penup()

    

    wn.onclick(homeScreen)

def winningScreen(winningPlayer):
    wn.clearscreen()
    turt = t.Turtle(shape="square")
    turt.hideturtle()
    turt.penup()
    turt.goto(-screenWidth,screenHeight-100)
    turt.pendown()
    turt.write(f"{winningPlayer} Wins!", font=fontSetup)
    turt.penup()
    turt.goto(-screenWidth+10,-screenHeight+50)
    turt.pendown()
    turt.write("Click Any Where On The Screen To Go Back To The Main Menu", fontSideSetup)
    wn.onclick(homeScreen)
    wn.listen()


def homeScreenControls(x,y):
    wn.clearscreen()
    if x>0 and y>=0:
        gameBoardTurts()
        wn.onclick(checker)
        wn.listen()
        wn.mainloop()
    elif x<-0 and y>=0: 
        instructions()
    elif x>0 and y<=0: 
        global gamemode 
        gamemode = "CP"
        gameBoardTurts()
        wn.onclick(checker)
        wn.listen()
        wn.mainloop()
    else:
        credits()

def credits():
    wn.clearscreen()
    wn.bgcolor('grey')
    turt = t.Turtle(shape="square")
    turt.hideturtle()
    turt.penup()
    turt.goto(-50,screenHeight-100)
    turt.pendown()
    turt.write("Creditis", font=fontSetup)
    turt.penup()
    turt.goto(-screenWidth+10,20)
    turt.pendown()
    turt.write("Isaac Pohl - 1st and 2nd addition", font=fontSideSetup)
    turt.penup()
    turt.goto(-screenWidth+10,0)
    turt.pendown()
    turt.write("Mathew Diekume - 1st addition", font=fontSideSetup)
    turt.penup()
    turt.goto(-screenWidth+10,-20)
    turt.pendown()
    turt.write("Sources Used", font=fontSideSetup)
    turt.penup()
    
    turt.goto(-screenWidth+10,-13)
    turt.pendown()
    turt.goto(-screenWidth+170,-13)
    turt.penup()
    
    turt.goto(-screenWidth+10,-40)
    turt.pendown()
    turt.write("Slack-Overflow", font=fontSideSetup)
    turt.penup()
    turt.goto(-screenWidth+10,-60)
    turt.pendown()
    turt.write("Images Sources", font=fontSideSetup)
    turt.penup()
    
    turt.goto(-screenWidth+10,-52)
    turt.pendown()
    turt.goto(-screenWidth+190,-52)
    turt.penup()
    
    turt.goto(-screenWidth+10,-80)
    turt.pendown()
    turt.write("Xiomara7 github", font=fontSideSetup)
    turt.penup()
    turt.goto(-screenWidth+10,-160)
    turt.pendown()
    turt.write("Click Any Where On The Screen To Go Back To The Main Menu", font=fontMiniSetup)
    wn.onclick(homeScreen)
def gameBoardTurts():
    global gameBoard
    gameBoard =["1","2","3","4","5","6"]
    gameBoard = g.Generation(gameBoard,lineNumbers).__str__()
    print(gameBoard)
    global turtles
    turtles = [[]]
    x = -screenWidth+100
    y= screenHeight-80
    stage=0
    stagexcor = 0
    wn.clearscreen()
    
    for i in range (1,13):
        bob = t.Turtle()
        bob.shape("square")
        bob.shapesize(7.5,10)
        bob.fillcolor("black")
        bob.speed(0)
        bob.penup()
        bob.goto(x,y)
        bob.color("black")
        bob.write(gameBoard[stage][stagexcor])
        bob.penup()
        bob.color(listColor[i])
        x+=200
        turtles[stage].append(bob)
        stagexcor+=1
        if i%3==0 and i!=0:
            y-=150
            x= -screenWidth+100
            turtles.append([])
            stage+=1
            stagexcor=0





player1Score = 0
player2Score = 0
nextPlayerTurn= 1
switch = 1

gameOver = '''
███▀▀▀██    ███▀▀▀██    ███▀█▄█▀███      █████
██    ██    ██    ██    ██    █    ██    ██    
██  ▄▄▄     ██▄▄▄▄▄█    ██    █    ██    ████
██    ██    ██    ██    ██    ██    ██   ██
███▄▄▄██    ██    ██    ██    ██    ██   █████

██▀▀▀▀██    ▀█    ██▀   ██▀▀▀    ██▀▀▀▀██    
██    ██    ██    ██    ██       ██    ██    
██    ██    ██    ██    ██▀▀▀    ██▄▄▄▄▄    
██    ██    ██    █▀    ██       ██    ██    
██▄▄▄▄██    ─██████     ██▄▄▄    ██    ██
'''




def cardAnylzer(itemCoords,secondPlayerName):
    global player1Score
    global player2Score
    global switch
    global gameBoardSoFar

    card1,card2 = gameBoard[itemCoords[0][0]][itemCoords[0][1]],gameBoard[itemCoords[1][0]][itemCoords[1][1]]
    print(card1,card2)
    if switch==2:
        nextPlayerTurn = "One"
        switch=1
    elif switch==1 :
        nextPlayerTurn= secondPlayerName
       

        switch=2
    time.sleep(1)
    print(card1,card2)
    if card1==card2:
        turtles[itemCoords[0][0]][itemCoords[0][1]].fillcolor("grey")
        turtles[itemCoords[1][0]][itemCoords[1][1]].fillcolor("grey")
        turtles[itemCoords[0][0]][itemCoords[0][1]].showturtle()
        turtles[itemCoords[1][0]][itemCoords[1][1]].showturtle()
        gameBoardSoFar[(itemCoords[0][0]*3)+itemCoords[0][1]] = ''
        print("this is total for removal",[(itemCoords[0][0]*3)+itemCoords[0][1]])
        gameBoardSoFar[(itemCoords[1][0]*3)+itemCoords[1][1]] = ''
        if switch==2:
            player1Score+=1
            switch=1
            nextPlayerTurn = "One"
            print(player1Score)
        else:
            player2Score+=1
            switch=2
            nextPlayerTurn = secondPlayerName
            print(player2Score)

    else: 
        turtles[itemCoords[0][0]][itemCoords[0][1]].showturtle()
        turtles[itemCoords[1][0]][itemCoords[1][1]].showturtle()

    bob = t.Turtle(shape="square")
    bob.hideturtle()
    bob.color("black")
    bob.pensize(3)
    bob.penup()
    bob.goto(-150,0)
    bob.pendown()
    bob.write(f"Player {nextPlayerTurn} Turn", font=fontSetup)    
    bob.penup()
    bob.goto(-150,-50)
    bob.pendown()
    bob.write(f"Player 1 Score = {player1Score}", font=fontSideSetup)  
    bob.penup()
    bob.goto(-150,-100)
    bob.pendown()
    bob.write(f"{secondPlayerName} score= {player2Score}", font=fontSideSetup)  
 

    

    time.sleep(2)



    bob.clear()
    

    if (player1Score+player2Score)==6:
        
        if player1Score>player2Score:
            winningPlayer = "One"
        elif player2Score>player1Score:
            winningPlayer=secondPlayerName
        elif player1Score==player2Score:
            winningPlayer="No One"
        player1Score= 0
        player2Score=0
        winningScreen(winningPlayer)

    print(itemCoords)

  



def checker(x,y):
    global rightfull
    global itemCoords
    if y>(screenHeight/2)+5: 
        if x>(screenWidth/3):
            turtles[0][2].hideturtle()
            col,row = 0,2
        elif x < - (screenWidth/3):
            turtles[0][0].hideturtle()
            col,row = 0,0
        else:
            turtles[0][1].hideturtle()
            col,row = 0,1
    elif y<-(screenHeight/2):
        if x>(screenWidth/3):
            turtles[3][2].hideturtle()
            col,row = 3,2
        elif x < - (screenWidth/3):
            turtles[3][0].hideturtle()
            col,row = 3,0
        else:
            turtles[3][1].hideturtle()
            col,row = 3,1
    elif y>(-5):
        if x>(screenWidth/3):
            turtles[1][2].hideturtle()
            col,row = 1,2
        elif x < - (screenWidth/3):
            turtles[1][0].hideturtle()
            col,row = 1,0
        else:
            turtles[1][1].hideturtle()
            col,row = 1,1
    else:
        if x>(screenWidth/3):
            turtles[2][2].hideturtle()
            col,row = 2,2
        elif x < - (screenWidth/3):
            turtles[2][0].hideturtle()
            col,row = 2,0
        else:
            turtles[2][1].hideturtle()
            col,row = 2,1

    if turtles[col][row].fillcolor() == "grey":
        turtles[col][row].showturtle()
    else:
        if rightfull == True :
            wn.onscreenclick(None) 
            wn.listen()
            itemCoords[1][0] = (col)
            itemCoords[1][1] = (row)         
            rightfull=False
            #send
            if gamemode=="CP":
                global gameBoardSoFar
                if switch==1:
                    print("This is player going for one player then  2 = player 1, else(1) = cp", switch)
                    print('Test')
                    gameBoardSoFar[(itemCoords[1][0]*3)+(itemCoords[1][1])] = (gameBoard[itemCoords[1][0]][itemCoords[1][1]])
                    gameBoardSoFar[(itemCoords[0][0]*3)+(itemCoords[0][1])] = (gameBoard[itemCoords[0][0]][itemCoords[0][1]])
                    cardAnylzer(itemCoords,"CP")
                    print("This is player going for one player then  2 = player 1, else(1) = cp", switch)
                if switch==2:
                    while switch==2:
                        itemCoords,gameBoardSoFar = g.Generation.cpMove(3, gameBoardSoFar, itemCoords,gameBoard,turtles)
                        # col,row = r.randint(0,2),r.randint(0,2)
                        # print(f"{col}{row} for cp")
                        # itemCoords[1][0] = col
                        # itemCoords[1][1] = row
                        print("Yep",itemCoords)
                        turtles[itemCoords[0][0]][itemCoords[0][1]].hideturtle()
                        # col,row = r.randint(0,2),r.randint(0,2)
                        # print(f"{col}{row} for cp")
                        # itemCoords[0][0] = col
                        # itemCoords[0][1] = row
                        turtles[itemCoords[1][0]][itemCoords[1][1]].hideturtle()
                        time.sleep(2)

                        cardAnylzer(itemCoords,"CP")
                        print("This is player going for cp player then  2 = player 1, else(1) = cp", switch)

            else:
                cardAnylzer(itemCoords,"Two")
                print("test2")

            # endGameAnylyser(bob)
            wn.onscreenclick(checker)
            wn.listen()

        else:
            #append
            itemCoords[0][0] = (col)
            itemCoords[0][1] = (row)
            rightfull=True

def homeScreen(x,y):
    wn.clearscreen()
    drawHomeScreen()
    #gameBoardTurts()
    wn.onclick(homeScreenControls)
    wn.listen()
    wn.mainloop()


homeScreen(0,0)
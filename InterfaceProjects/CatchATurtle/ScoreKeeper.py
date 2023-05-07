import turtle as t 

wn=t.Screen()
score=0 
fontSetup=("Times New Roman",30,"normal")

scorekeeper=t.Turtle()
scorekeeper.penup()
scorekeeper.hideturtle()
scorekeeper.goto(100,200)
scorekeeper.pendown()
scorekeeper.speed(0)

#functions
def updateScore(x,y):
    #global is to let this function know to go look at a global var
    global score
    score+=1
    scorekeeper.clear()
    #object.write("message",options)         ("font type       ",size,"style")
    scorekeeper.write(f"Score: {score}",font=fontSetup)
    

#events
wn.onscreenclick(updateScore)


wn.mainloop()
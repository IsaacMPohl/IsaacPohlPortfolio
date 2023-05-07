
def getNames(FILENAME):
    #open the file 
    file1 = open(FILENAME , "r")
    #loop through each line of the file
    names=[]
    for line in file1:
        index=0
        leaderName=""
        #get the information up to the commma
        while(line[index]!=","):
            leaderName+=line[index]
            index+=1
        names.append(leaderName)
    
    #return that information 
    return names


def getScores(FILENAME):
    #open the file 
    file1 = open(FILENAME , "r")
    
    #loop through each line of the file
    scores=[]
    for line in file1:
        index=0
        leaderScore=""
        #find the comma
        #index=line.rfind(",")
        #index+=1
        while(line[index]!=","):
            index+=1
        index+=1
        #find information up to the end of the line
        while(line[index]!="\n"):
            leaderScore+=line[index]
            index+=1
        scores.append(leaderScore)
    
    #return that information 
    return scores

#For updating the database
def updateLeader(FILENAME,leaderNames,leaderScores,playerName,playerScore):
    #loop through all the scores in the current leaderboard
    index=0 
    while (index<len(leaderScores)): 
        #Check if the score can be inserted into this position
        if(playerScore>=int(leaderScores[index])):
            break
        else:
            index+=1
    #Insert player info
    leaderNames.insert(index,playerName)
    leaderScores.insert(index,playerScore)
    
    #Ensure only 5 players in the leaderboard
    if(len(leaderNames)>5):
        leaderNames.pop()   #remove last item or lowest score
        leaderScores.pop()   
    
    #Save the data back into the data base
    file1=open(FILENAME,"w")
    
    #loop through the lists and save each list to the file
    for i in range(len(leaderNames)):
        file1.write(f"{leaderNames[i]},{leaderScores[i]}\n")
    
    file1.close()
        

#not best habit
def draw_leaderboard(high_scorer, leader_names, leader_scores, turtle_object, player_score):
    #high_scorer is a boolean to tell if the current user is a high_scorer

    # clear the screen and move turtle object to (-200, 100) to start drawing the leaderboard
    font_setup = ("Arial", 20, "normal")
    turtle_object.clear()
    turtle_object.penup()
    turtle_object.goto(-160,100)
    turtle_object.hideturtle()
    turtle_object.down()

    index = 0
    # loop through the lists and use the same index to display the corresponding name and score, separated by a tab space '\t'
    while (index < len(leader_scores)):
        turtle_object.write(str(index + 1) + "\t" + leader_names[index] + "\t" + str(leader_scores[index]), font=font_setup)
        turtle_object.penup()
        turtle_object.goto(-160,int(turtle_object.ycor())-50)
        turtle_object.down()
        index = index + 1

    # move turtle to a new line
    turtle_object.penup()
    turtle_object.goto(-160,int(turtle_object.ycor())-50)
    turtle_object.pendown()

    #TODO: Display message about player making the leaderboard or not

    # move turtle to a new line
    turtle_object.penup()
    turtle_object.goto(-160,int(turtle_object.ycor())-50)
    turtle_object.pendown()
    #TODO: Displat a gold/silver/brownse message if player earned a medal
    gold=int(leader_scores[0])
    silver=int(leader_scores[1])
    bronze=int(leader_scores[2])
    if(player_score>=gold):
        turtle_object.write("You earned a gold metal!", font=("Times New Roman",10,"bold"))
    elif(player_score>=silver):
        turtle_object.write("You earned a silver metal!", font=("Times New Roman",10,"bold"))
    elif(player_score>=bronze):
        turtle_object.write("You earned a bronze metal!", font=("Times New Roman",10,"bold"))

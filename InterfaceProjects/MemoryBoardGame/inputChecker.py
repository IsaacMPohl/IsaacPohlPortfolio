class InputChecker:
  @staticmethod
  def getCorrectInput(question,question2,rows,col, gameBoard):
    userInput = ""
    userInput2= ""
    checkIfAlreadyPlayed = True

    while checkIfAlreadyPlayed==True:
        userInput = ""
        userInput2= ""
        #This keeps going through the loop until the right answer is typed in which was in the list of answers
        while userInput.isdigit() == False:
            userInput = input(question)
            if userInput.isdigit() == False:
                print("Please Enter a digit")
            else:
                if int(userInput)>col:
                    print("Re-enter a digit because out of range")
                    userInput =""
        userInput= int(userInput)

        while userInput2.isdigit() == False:
            userInput2 = input(question2)
            if userInput2.isdigit() == False:
                print("Please Enter a digit")
            else:
                if int(userInput2)>rows:
                    print("Re-enter a digit because out of range")
                    userInput2 =""
        userInput2=int(userInput2)
        if gameBoard[(userInput2-1)][(userInput-1)]=='X':
            checkIfAlreadyPlayed = False
        else:
            print("Already used one of the values")
    return userInput2,userInput


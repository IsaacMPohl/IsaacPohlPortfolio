class InputChecker:
  @staticmethod
  def getCorrectInput(listOfAnswers, question):
    userInput = ""
    #This keeps going through the loop until the right answer is typed in which was in the list of answers
    while not (userInput in listOfAnswers):
      userInput = input(question)
      #lower case everything for similicity
      userInput = userInput.lower()
  
      return userInput

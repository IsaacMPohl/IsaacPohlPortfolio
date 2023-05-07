import os
import string
from generator import *
from basicStatic import changeFile
from InputChecker import InputChecker
from DocumentAddInformation import documentAddInfo
from UserPasswordInput import UserPasswordInput
#from checkPass import CheckPossiblePass

def accountLogAndCreate():
  wrongAnswer = 3
  keepGoing = False
  print("You have 3 tries to get your password right before the program shuts down.")

  while keepGoing != True:
    userName = input("Enter your username (If you want to create a new username, type in 'new') ")
    #If the user types in a username
    if userName.lower() != "new":
      #Ask the password
      password = input("What is your password? ")
      #Open the file and read the lines
      fileToRead = open("dataBase_Secured.txt ", "r")
      lines = fileToRead.readlines()
      #Runs throught each line
      for line in lines:
        #Get each line assign valuables by spliting them
        officalLast, officalFirst, officalPassword, officalUser = line.rstrip().split(",")
        #if what the user type in for username and password is found in the line
        if officalUser == userName and officalPassword == password:
          #Stops the loop from repeating
          keepGoing = True
      #If user would have not type the right info
      if (keepGoing != True):
        #-1 from the wrong answer
        wrongAnswer -= 1
        print(f'''The username or password is wrong. You only have {wrongAnswer} attempts left.''')

    #If the user wants to create a account
    elif userName == "new":
      #Ask the users information
      userName = input("What username do you want to add? ")
      firstName = input("What is your first name? ")
      lastName = input("What is your last name? ")
      #Ask the user if they want a random generated password
      ui = input("Do you want a randomly generated password? (yes/no) ")
      ui = ui.lower()
      #If the user want a random generated password
      if ui == "yes":
        #Goes into a loop until the user says yes to the password
        while ui != "no":
          #Opens a class to generate passwords
          password = Generator(password="")
          print(f"Your password is {password}")
          ui = input("Do you want to regenerate a random password? (yes/no) ")
          print()
      #If the user doesn't want a random generated password
        
      elif ui == "no":
        goingOn = "No"
        #Loops until password meets requriments
        while goingOn != "yes":
          password = input("What is your password? ")
          #This is what Hudson came up with
          #Sets the variables
          num = False
          special = False
          cap = False
          count = len(password)>=8
          #Breaks down eact character in the password
          for character in password:
            #If a comma is in password breaks the loop
            if character == ",":
              character = len(password)
            #If a capital letter is in turn true
            elif (character in string.ascii_uppercase):
              cap = True
            #If a number is in the string return true
            elif (character in string.digits):
              num = True
            #If a special character is in the password return true
            elif (character in string.punctuation):
              special = True
          #If all are true move on
          if num and cap and special and count == True:
            goingOn = "yes"
          #If not then goes through loop again
          else:
            print("Password does not meet requirements. Please try again. Must have 1 capital letter, 1 special character, at least 8 characters, and no commas")
          
      #This is the class that concatnates the 4 items and then writes them in the data base
      add = documentAddInfo(userName,firstName,lastName,password,1)
      documentAddInfo.write(add,"dataBase_Secured.txt ")


    #Checks if the user has no more gusess left
    if wrongAnswer == 0:
      #Closes out the program
      exit()
      
  #Returns the user UserName
  return (userName)

#This function allows users to create categories
def createCategories(userName):
  #Ask the user what category they want to add
  category = input("What category do you want to add? ")
  #Creates a new txt file with their information and C at the begging so it can be eaily trace back later
  documentAddInfo.createName(category,userName)
  print(f"{category} was created")
  #Returns the category
  return (category)

#This functions prints all the available categories
def printOutAviable(userName):
  #Saves all the files in the folder under files (used geeks for geeks for this)
  files = os.listdir()
  #Runs through each file
  for i in range(len(files)):
    #If the file beggings with c and has your username in it 
    if files[i][0] == "C" and files[i][(len(files[i])-(len(userName))-4):(len(files[i]) - 4)] == userName :
      #Prints the file name and not the other bulk on the file name
      print(files[i][1:((len(files[i]) - (len(userName) + 4)))])
#This function allows users to delect categories
def delect(userName):
  removeFile = None
  #Ask the user what category they want to delect
  category = input("What category do you want to delete? ")
  files = os.listdir()
  #Runs through each file
  for i in range(len(files)):
    #If what the user category which they entered is in the directory
    if (f"C{category}{userName}.txt") in files[i] and files[i][(len(files[i])-(len(userName))-4):(len(files[i]) - 4)] == userName:
      #Make sure they want to delect the file
      notifer =  InputChecker.getCorrectInput(["yes","no"], f"Are you sure you want to delete {category}? (yes/no) ")
      if notifer == "yes":
        #Remove the file (Used geeks for geeks for this)
        removeFile = os.remove(f"C{category}{userName}.txt ")
        #Kicks out of the loop
        i = len(files)
        #Assigns remove file to something
        removeFile = ""
  #If removeFile has something it equal to prints that it was successfull
  if removeFile is not None:
    print(f"{category} was deleted")
  #If it has noting print the file was not found
  else:
    print("The file was not found")

#This allows the users to go to a specific category file
def goTo(userName):
  goingOn = "yes"
  #Loop only breaks if equal to No
  while goingOn != "no":
    filesAdded = None
    #Ask the user what category they want to create
    category = input("What category do you want to go to?")
    #used geeks for geeks for this
    files = os.listdir()
    #Runs through each file 
    for i in range(len(files)):
      #If the category they entered is in the directory
      if (f"C{category}{userName}.txt") in files[i]:
        #Print that it was found and ask the user if they want to add or print or edit
        userInputForC = input("File was found, what do you want to? (add, print, edit) ")
        #If they want to add ask what all the informations they want to add
        if userInputForC == "add":
          title = input("What title do you want to add this under? ")
          userNameForTitle = input(f"What is you username do you want to assign to {title}? ")
          #Ask the user if they want a random generated password
          ui = input("Do you want a randomly generated password? (yes/no) ")
          ui = ui.lower()
          #If the user want a random generated password
          if ui == "yes":
            #Goes into a loop until the user says yes to the password
            while ui != "no":
              #Opens a class to generate passwords
              passwordForTitle = Generator(password="")
              print(f"Your password is {passwordForTitle}")
              ui = input("Do you want to regenerate a random password? (yes/no) ")
              print()
          elif ui == "no":
            passwordForTitle = input(f"What password do you want to assign to {title}? ")


          #Ask the user if this information was correct
          print(f"Title: {title}\nPassword: {passwordForTitle}\nUsername: {userNameForTitle}")
          goingOn = input("Is this the right information? (yes/no) ")
          #If it was open the category file and write all the information in it
          if goingOn == "yes":
            #This contanates the 3 items into 1 line and then add them into the file
            add = documentAddInfo(title,passwordForTitle,userNameForTitle,"",2)  
            documentAddInfo.write(add, (f"C{category}{userName}.txt "))
        #If the user wants to print all the information
        elif userInputForC == "print":
          #Open up the category file and read the lines
          fileToRead = open(f"C{category}{userName}.txt ", "r")
          lines = fileToRead.readlines()
          #Runs through each line
          for line in lines:
            #Saves the data to variables in each line
            title, passwordForTitle, userNameForTitle = line.rstrip().split(",")
            #Prints the data out
            print(f"title- {title} password- {passwordForTitle} userName - {userNameForTitle}")
        #If the user wants to edit
        elif userInputForC == "edit":
          #Ask the user want they want to edit
          accountName = input(f"What {category} name do you want to edit? ")
          #Runs the edit proceess saved in a class
          changeFile.changeFiles(userName,accountName, category)
        #This is for the user knows the file was found
        filesAdded = ""
        #Goes out of the loop
        i = len(files)
    #If filesAdded save something it means the file was found, ask if they want to continue
    if filesAdded is not None:
      goingOn = InputChecker.getCorrectInput(["yes","no"],"Do you want to continue to add information? (yes/no)")
      print()
    #If the file was not found
    else:
      goingOn = InputChecker.getCorrectInput(["yes","no"],"File not found, do you want to try again? (yes/no)")
      print()


#Saves this variable for the main loop
exitOut = ""
#Assign the navigation print out
navigation = '''
    Add a Category (add)
    Print out all of your Category (print)
    Go to your category (go to)
    Delete a category (delete)
    Exit out of program (quit)
    
'''
#beggines the account login and create function
userName = accountLogAndCreate()

while exitOut != "quit":
  #Prints out the navigation and ask the user what they would like to do
  userInput = InputChecker.getCorrectInput(["add","print","go to", "delete", "quit"] , navigation)
  #Makes it lower case to try to eleminate human error
  userInput= userInput.lower()
  if userInput == "add":
    createCategories(userName)
  elif userInput == "print":
    printOutAviable(userName)
  elif userInput == "delete":
    delect(userName)
  elif userInput == "go to":
    goTo(userName)
  elif userInput == "quit":
    exitOut = "quit"

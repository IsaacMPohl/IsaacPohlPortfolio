from InputChecker import InputChecker


class changeFile:
  @staticmethod
  def changeFiles(userName, accountName, category):
    list = []
    #Ask the user what they want to edit in this location
    ui = InputChecker.getCorrectInput(["title","username","password, delect"] ,"Do you want to edit the title, username, or password or delect this?")
    if ui != "delect":
      #Ask the user what they want to change it to
      whatTo = input("What do you want to change it to?")
      #opens the file, the r+ allows the program to read and write
    fileToRead = open(f"C{category}{userName}.txt ", "r+")
    lines = fileToRead.readlines()
    a = 0
    #lenght = len(lines)
    #Goes through each line
    for line in lines:
      #appends a new list inside the list for the info can be save under
      list.append([])
      t, p, u = (line.rstrip().split(","))
      list[a].append(t)
      list[a].append(p)
      list[a].append(u)
      #This variable allows the list append to move on to the next list that was created
      a += 1
    
  
    #used python for biggers for this (This erreas the file)
    fileToRead.truncate(0)
    #Open the file again
    fileToRead = open(f"C{category}{userName}.txt ", "r+")
    lines = fileToRead.readlines()
    #Goes through the list that was created that has all the old file information saved in it
    for i in range(len(list)):
      #Picks up the variables saved in each order in the list
      title = list[i][0]
      passwordForTitle = list[i][1]
      userNameForTitle = list[i][2]
      #This raises if the user title was found which they want to change the information under and what the user wants to change and changes it based on that
      if title == accountName and ui == "title":
        fileToRead.write(f"{whatTo},{passwordForTitle},{userNameForTitle} \n")  
      elif title == accountName and ui == "username":
        fileToRead.write(f"{title},{passwordForTitle},{whatTo} \n")  
      elif title == accountName and ui == "password":
        fileToRead.write(f"{title},{whatTo},{userNameForTitle} \n")  
      #If the title was not found in that section of the list write the basic info
        #This doesn't replace the line so delects it 
      elif title == accountName and ui == "delect":
        "nothing"
      else:
        fileToRead.write(f"{title},{passwordForTitle},{userNameForTitle} \n")
      a += 1

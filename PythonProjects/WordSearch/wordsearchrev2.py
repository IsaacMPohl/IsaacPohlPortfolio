#Importing os
import os
#Reading the files
fileToRead = open("Book2.csv " , "r")
lines = fileToRead.readlines()
#This is the list which the crossword puzzel words are saved under
list = [] 
#Assigning the variables
n = 0 
p=0
add = 0
#These are what the program saves the formated words under
words=[]
words2=[]
#This is what the lenght of the characters in the file is saved uder
lenght=[]
#These are the list of words which the program finds
word = ["mouse","cow","monkey","elephant","tiger","donkey","rabbit","turtle","swan","duck","beaver","fish","shark","lion","cat","dog","horse","mouse","frog"]
#Goes through each word
for w in word:
    #Replaces with a non space like computer science
    w=(w.replace(" ",""))
    #Appends the uppercase version of the word
    #This is the origonal uppercase verison so we can show the player the words at the very end as well
    words.append(w.upper())
    #This is the next list of the uppercase version, this is the list where we can delect from the list once the item was found
    words2.append(w.upper())
#Goes through each line in the cross word file
for line in lines:
    #Appends the lenght of the line to a list, so we can make sure all of the lines leghts are the same
    lenght.append(len(line))
    print(lenght)
    #Makes a newlist
    list.append([])
    #Assigns t, so we can only append the characters and not the commas
    t=0
    #Replaces the new line of \n to a empty value
    newLine = line.replace("\n","")
    #This only appends the non comas and only goes tell the end of the list
    while t<((len(newLine))):
        list[n].append((newLine[t].upper()))
        t+=2
    n+=1

#print("hey")
#Thanks to slack-over flow for this if statment idea to check if the data is right
if len(set(lenght)) != 1:
    #print("Your data is not right")
    #os exit is what I learned from slack-over flow on one of are last projects, it closes out of the program
    os._exit(0)


#This is the function that checks for the horizonal number
#You can think of the irration as of the x axis and l as the line number
def checkHorizontalNumber(irration,l):
    #Assigns irration to another valuable so we can use it later going the other way
    irration2=irration
    #This so we can tell the user what line number it occured on
    iO=irration
    #Assigns two empty string values
    string=""
    string2=""
    #Goes through a loop until it reaches the border
    while irration<(len(list[l])):
        #Adds the to the string the value
        string= string+list[l][irration]
        #Adds one to the irration which makers it go right
        irration+=1
        #If the string is contained in the word list
        if string in words2:
            list[l][iO]=" "
            #Print the data
            print(string)
            print(l+1,iO+1)
            print(l+1,irration)
            #Remove it from list to prevent repeting values
            words2.remove(string)
            #Break the list
            break
    #This does the same thing but goes left
    while irration2>=0: 
        string2= string2+list[l][irration2]
        #print(irration2)
        irration2-=1
        #print(string2)
        if string2 in words2:
            list[l][iO]=" "
            print(string2)
            print(l+1,iO+1)
            print(l+1,irration2+2)
            words2.remove(string2)
            break
        
#This checks for the same numbers going vertical
def checkNumberVert(irration,l):
    #Changes l which is the line, and not the irration
    lO=l
    l2=l
    string=""
    string2=""
    #This goes up
    while l<(len(list)):
        string= string+list[l][irration]
        l+=1
        if string in words2:
            list[lO][irration]=" "
            print(string)
            print(lO+1,irration+1)
            print(l,irration+1)
            words2.remove(string)
            break
    #This goes down
    while l2>=0:
        string2= string2+list[l2][irration]
        l2-=1
        if string2 in words2:
            list[lO][irration]=" "
            print(string2)
            print(lO+1,irration+1)
            print(l2+2,irration+1)
            words2.remove(string2)
            break

#This check if the diagnal contains the words
def checkDiagnal(irration,l):
    #Need to assign 4 different string because we need to check for all four ways
    lO=l
    iO=irration
    string=""
    string2=""
    l1=l
    irration2=irration
    string3=""
    irration3=irration
    l3=l
    string4=""
    irration4 = irration
    l4 = l
    #This checks down and right
    while irration<(len(list[lO])) and l<len(list): 
        string= string+list[l][irration]
        #Changes bother the line and number
        irration+=1
        l+=1
        if string in words2:
            list[lO][iO]=" "
            print(string)
            print(iO+1,lO+1)
            words2.remove(string)
            break     
    #This goes up and right
    while irration2<(len(list[lO])) and l1>=0: 
        string2= string2+list[l1][irration2]
        irration2+=1
        l1-=1
        if string2 in words2:
            list[lO][iO]=" "
            print(string2)
            print(iO+1,lO+1)
            words2.remove(string2)
            break       
    #This goes up and left
    while irration3>=0 and l3 <len(list): 
        string3= string3+list[l3][irration3]
        irration3-=1
        l3+=1
        if string3 in words2:
            list[lO][iO]=" "

            print(string3)
            print(iO+1,lO+1)
            words2.remove(string3)
            break   
    #This goes left and down
    while irration4>=0 and l4>=0: 
        #print(irration)
        string4= string4+list[l4][irration4]
        irration4-=1
        l4-=1
        if string4 in words2:
            list[lO][iO]=" "

            print(string4)
            print(iO+1,lO+1)
            words2.remove(string4)
            break                
    
#Assigns the irration variable
irration = 0 

#Loops until the end of the list to change l which is used for the line
for l in range(len(list)):
    #Loops until the end of the range of the words, so changes i which is used to go to each word or answer to the cross word puzzel
    for i in range(len(words)):
        irration = 0 
        #While irration does not equal to the lenght of the list row
        while  irration!= (len(list[0])):
            #If the first lettle in the answer list is found in the puzzel 
            if (list[l][irration]==words[i][0]): 
                #Calls up each function to check if it the right word
                checkHorizontalNumber(irration,l)
                checkNumberVert(irration,l)
                checkDiagnal(irration,l)
            irration+=1

for characters in list:
    print(characters)
#Prints the words again
print(words)
print("")
print("")
print(words2)
    


        
    
    
        
#for line in list:
#    #print(line)
#    for n in range (len(words)):
#        for character in words[n]:  
#            print(character.upper())
#            print(line, character)
#            print(line.rfind((character.upper)))
#    irration!=1
#    
        
   # for p in range(len(list[0])):
   #     if words[i][n]==list[i][p]:
   #         add+=1 
            
   # n+=1

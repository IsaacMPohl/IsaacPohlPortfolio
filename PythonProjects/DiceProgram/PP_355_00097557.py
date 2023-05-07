#00097557

#Importing random
import random as r 
#Initializing variables
combination_list_storage=[]

#Function to allow users to enter how many dials they want
def get_number_in_dials():
    #Initializing a local variable
    number_dials = 0
    #Assign loop to True
    loop = True
    #While the loop is True
    while(loop == True):
        number_dials = input("How many dials do you want? (At least three must be used) ")
        #If the number entered is a int 
        if str.isdigit(number_dials):
            #Change that number to a int
            number_dials = int(number_dials)
            #If it bigger than or equal to 3 stop the loop 
            if number_dials >= 3:
                loop = False
            #Continue the loop
            else:
                loop = True
        #Continue the loop
        else:
            loop = True
    #return the number of dials
    return(number_dials)
#Function to get how many combinations the user wants to display
def get_how_many_to_list():
    #Assigns the loop to true
    loop = True
    #While the loop is true
    while(loop == True):
        number_of_generations = input("How many combinations do you want to display? ")
        #Checks to see if what the user entered is a digit
        if str.isdigit(number_of_generations):
            #If it is change it to a int
            number_of_generations = int(number_of_generations)
            #If it is bigger or equal to 3 ends the loop
            if number_of_generations >= 3:
                loop = False
            else:
                loop = True
        else:
            loop = True
    #Returns the number of combinations 
    return(number_of_generations)
#Function to pick a random number
def get_number(minumium,maxiumum):
    #Randrange picks a random number between 0-9, the r is calling the random module
    #It goes through 10 because python stops counting once it reaches 9
    random_number = r.randrange(minumium,maxiumum)
    #Returns the random number value
    return(random_number)
#This function assigns the values of random number to combo numbers
def next_combo_number(number_dials,n):
    #Takes in number of dials to find out how many times to loop/generate a random number
    #This also takes in n to switch up the list that is assigning the variables
    #Appends a new list inside the initial list to store the new combination line
    combination_list_storage.append([])
    #Loops through the number of dials wanted to generate
    for i in range(number_dials):
        #Calls the get_number function which generates a random number and puts it in a list
        combination_list_storage[n].append(get_number(0,10))
    #Returns the list
    return(combination_list_storage)
#This is the main loop to exucute the program 
def main():
    #This is a block string to print the instructions of this program
    print('''This application generates posible lock combinations; assuming that the number will be from 0 to 9
(inclusive). Please first enter the quantity of dials on the combination locks. And the enter
how many combinations you would like to generate.''')
    #The prints are spaces for the program can be easily read 
    print()
    #Gets the number of dials and number to generate from the functions
    number_dials = get_number_in_dials() 
    number_of_generations = get_how_many_to_list()
    print()
    #Goes through a loop to generate a new combo for each number of generations
    for n in range(number_of_generations):
        #gets the new list after going through the next combo number list
        list = next_combo_number(number_dials,n)
        #Prints out using a fancy string the number of generations and the combination numbers assigned to that number
        #This also add 1 to iration of the loop because python starts counting at 0 
        print(f"Number {n+1}: {list[n]}")
        
#This runs the main function
main()

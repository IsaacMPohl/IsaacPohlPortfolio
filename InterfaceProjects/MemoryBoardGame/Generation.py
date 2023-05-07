#Importing random
import random as r 
#Importing generation
class Generation: 
    def __init__(self,board,rows):
        #Takes in the board to randimize and how many rows to assign to 
        self.board = board
        self.rows = rows
    def __str__(self):
        #Making a newBoard list
        newBoard = []
        #Duplicating the board so we have two of everything
        self.board = self.board*2    
        #shuffle the board
        r.shuffle(self.board)
        #Decide how many cards will be per row
        perRow = len(self.board)/self.rows
        #The lower and upper will be used to determine when to create new list/ rows to save the cards under
        lower=0
        upper=perRow
        #Goes through each row
        for i in range(self.rows):
            newBoard.append([])
            #Goes through each lettle in the range
            for lettle in self.board[int(lower):int(upper)]:
                #Appends the lettle in the right location
                newBoard[i].append(lettle)
            #Move the list over so it can be saved in a new row
            lower+=perRow
            upper+=perRow
        #Returns the newBoard
        return newBoard
    #Returns the game of the x list so the players can't see the answers
    def cpMove(rowAmountNum,gameboardSoFar,itemCoords,gameBoard,turtles):
        print("this is gameso far", gameboardSoFar)
        double = [number for number in gameboardSoFar if gameboardSoFar.count(number)>1 and number!='']
        print("this is a double" , double)
        if len(double)>1:
            oneIndex= gameboardSoFar.index(double[0])
            print("this is the index of a double",oneIndex)
            amountOfRows = 0
            rowAmount=rowAmountNum
            while oneIndex>2:
                amountOfRows+=1
                oneIndex-=(rowAmount)
            gameboardSoFar[amountOfRows*rowAmountNum+oneIndex] = ""
            itemCoords[0][0]=amountOfRows
            itemCoords[0][1]=oneIndex
            twoIndex = gameboardSoFar.index(double[0])
            print("this is the index of the second double",twoIndex)
            amountOfRows = 0
            while twoIndex>2:
                amountOfRows+=1
                twoIndex-=(rowAmount)
            itemCoords[1][0]=amountOfRows
            itemCoords[1][1]=twoIndex
        else:
            bothRight = False
            while bothRight == False:
                col = r.randint(0,3)
                row=r.randint(0,2)
                itemCoords[1][0] = col
                itemCoords[1][1] = row
                if turtles[col][row].fillcolor()!="grey":
                    bothRight=True
                    gameboardSoFar[col*rowAmountNum+row] = (gameBoard[col][row])
            print(col,row)
            bothRight = False
            while bothRight == False:
                col = r.randint(0,3)
                row=r.randint(0,2)

                if turtles[col][row].fillcolor()=="grey" or col== itemCoords[1][0] and row==itemCoords[1][1] :
                    print()
                else:
                    itemCoords[0][0] = col
                    itemCoords[0][1] = row
                    print("YOU GOT IT")
                    bothRight=True
                    gameboardSoFar[col*rowAmountNum+row] = (gameBoard[col][row])
                print()
                print(itemCoords[1][0],itemCoords[1][1])
                print(col,row)

        print()
        print()

        return(itemCoords,gameboardSoFar)
      
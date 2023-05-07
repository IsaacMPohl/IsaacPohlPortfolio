file = open("file.txt","r")
lines = file.readlines()
'''
total = 0
for line in lines:
  first,blank,second  = (line.strip())
  if second == "Z":
    #"Scissors"
    total += 3
  elif second == "Y":
    #"Paper"
    total +=2
  elif second == "X":
    #"Rock"
    total += 1
  if first == "A" and second == "X" or first == "B" and second == "Y" or first == "C" and second == "Z":
    total += 3
  elif first == "A" and second == "Y" or first == "B" and second == "Z" or first == "C" and second == "X":
    total += 6
'''

total = 0
for line in lines:
  first,blank,second  = (line.strip())
  if first == "C":
    if second == "Z":
      total += 7
    elif second == "X":
      total += 2
    elif second == "Y":
      total += 6

  if first == "B":
    if second == "X":
      total += 1
    elif second == "Y":
      total += 5
    elif second == "Z":
      total += 9
      
  if first == "A":
    if second == "Y":
      total += 4
    elif second == "Z":
      total += 8
    elif second == "X":
      total += 3

    
 
print(total)
  #'''A for Rock, B for Paper, and C for Scissors'''
  #X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
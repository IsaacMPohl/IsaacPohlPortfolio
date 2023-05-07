


last = []
first = 0
total = 0
v = 0
previous = 0 
fileToRead = open("ReinDeerFood.txt " , "r")
lines = fileToRead.readlines()
listofScores = []

last.append([])
for line in lines:
    #print(line)
    if line in["\r\n" , "\n"]:
        #used stackover flow for this
        listofScores.append(total)
        if total > previous:
            previous = total
        total = 0
        

    else:
        total += int(line)

print(previous)
listofScores.sort(reverse=True)
#used geeks for geeks for this
totalTotal = listofScores[0] +listofScores[1] + listofScores[2]
print (totalTotal)

        

   
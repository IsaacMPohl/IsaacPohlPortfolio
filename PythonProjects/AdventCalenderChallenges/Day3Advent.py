
list = []
i = 0 
newList = []
total = 0

fileToRead = open("rucksacksRepeat.txt " , "r")
lines = fileToRead.readlines()

for i,line in enumerate(lines):
    list.append([])
    halfLength = int(len(line)/2)
    list[i].append((line[0:halfLength]))
    list[i].append(line[halfLength:(len(line)-1)])

for i in range(len(list)):
    #for n in range (len(list[i])):
    for a in range (len(list[i][0])):
        #list[i][n][a].ord()
        if list[i][0][a] in list[i][1] :#[int(len(list[i][n])/2):(int(len(list[i][n])))]:
            #print(list[i][0][a])
            if list[i][0][a].isupper():
                #print((ord(list[i][0][a])-38))
                total += (ord(list[i][0][a])-38)
            else:
                #print((ord(list[i][0][a])-96))
                total += (ord(list[i][0][a])-96)
        #count(a,0,(len(list[i][n]))) >=0 True:
            break

print("")
print (total)


fileToRead = open("SpaceCleanup.txt" , "r")
lines = fileToRead.readlines()
n = 0 
list = []
number = 0
total = 0

for line in lines:
    a,b = line.rstrip().split(",")
    list.append([[],[]])
    a1,a2 = a.split("-")
    b1,b2 = b.split("-")
    number = int(a1)
    #print(len(a))
# $(int(a[0]))
    s = 0

    list[n][s].append(int(a1))
    for i in range (0,(int(a2)-int(a1))):
        #print(ord(a[i]))
        number += 1 
        list[n][s].append(number)
    s = 1
    number = int(b1)
    list[n][s].append(int(b1))

    for i in range (0,(int(b2)-int(b1))):
        #print(ord(a[i]))
        number += 1 
        s = 1
        list[n][s].append(number)   

   # print(list[n][1])
    #print(list[n][0])
    #print((len(list[n][1])))
    totalAddOn = 0
    TT = True
    for i in range(int(len(list[n][0]))):
        ''' if list[n][1][i] in list[n][0]:
            total +=1
            break'''
        if list[n][0][i] in list[n][1]:
            totalAddOn = 1
            TT = False
            break 
            


    if TT == True:
        for i in range(int(len(list[n][1]))):
            if list[n][1][i] in list[n][0]:
                totalAddOn = 1
                break
       
    total += totalAddOn



    #print(a2)

   # print(a)
    #print(b)

    n += 1
    #print(list)
print(total)

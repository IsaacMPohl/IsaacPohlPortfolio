#Day 2
#Can you open the file????
with open("Day2.txt","r") as f:
    file = f.readlines()

#what does the file actually look like?
#print(file)

#Clean the data
newFile=[]
for line in file:
    opp,me=line.rstrip().replace(" ","")
    newFile.append(f"{opp}{me}")
#print(newFile)

#Dictonary -> Sequence -> relys on a keyword to obtain a value
combos={"AX":3,
        "AY":4,
        "AZ":8,
        "BX":1,
        "BY":5,
        "BZ":9,
        "CX":2,
        "CY":6,
        "CZ":7
        }

#print(combos[0])
print(combos["AX"])

total=0
for line in newFile:
    total+=combos[line]
print(total)

#Other notes (krabs combo menu)
subtotal = 0
order = []
menu={
    "kp":2.50,
    "kpc":2,75,
    "dkp":3.00,
    "dkpc":3.25
}
ui = input("what would you like? ")
order.append(ui)
subtotal+=menu[ui]
    
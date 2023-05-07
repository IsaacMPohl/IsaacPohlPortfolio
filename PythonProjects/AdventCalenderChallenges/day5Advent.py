C = '''[C]'''
D = '''[D]'''
G = '''[G]'''
F = '''[F]'''
L = '''[L]'''
P = '''[P]'''
Q = '''[Q]'''
S = '''[S]'''
B = '''[B]'''
R = '''[R]'''
N = '''[N]'''
W = '''[W]'''
Z = '''[Z]'''
M = '''[M]'''
V = '''[V]'''
H = '''[H]'''
T = '''[T]'''
J = '''[J]'''

pile1 = [N,R,G,P]
pile2 = [J,T,B,L,F,G,D,C]
pile3 = [M,S,V]
pile4 = [L,S,R,C,Z,P]
pile5 = [P,S,L,V,C,W,D,Q]
pile6 = [C,T,N,W,D,M,S]
pile7 = [H,D,G,W,P]
pile8 = [Z,L,P,H,S,C,M,V]
pile9 = [R,P,F,L,W,G,Z]
'''
    [C]         [Q]         [V]    
    [D]         [D] [S]     [M] [Z]
    [G]     [P] [W] [M]     [C] [G]
    [F]     [Z] [C] [D] [P] [S] [W]
[P] [L]     [C] [V] [W] [W] [H] [L]
[G] [B] [V] [R] [L] [N] [G] [P] [F]
[R] [T] [S] [S] [S] [T] [D] [L] [P]
[N] [J] [M] [L] [P] [C] [H] [Z] [R]
 1   2   3   4   5   6   7   8   9 
'''

#pile1 = [Z,N]
#pile2 = [M,C,D]
#pile3 = [P]

fileToRead = open("arranging.txt" , "r")
lines = fileToRead.readlines() 
for line in lines:
    move,moveNumber,f, pilePull,to ,toLocation = (line.rstrip().split(" "))
    
    #print(pilePull)
    if pilePull == "1":
        pilePull = pile1
    elif pilePull == "2":
        pilePull = pile2
    elif pilePull == "3":
        pilePull = pile3
    elif pilePull == "4":
        pilePull = pile4
    elif pilePull == "5":
        pilePull = pile5
    elif pilePull == "6":
        pilePull = pile6
    elif pilePull == "7":
        pilePull = pile7
    elif pilePull == "8":
        pilePull = pile8
    elif pilePull == "9":
        pilePull = pile9
        
    if toLocation == "1":
        toLocation = pile1
    elif toLocation == "2":
        toLocation = pile2
    elif toLocation == "3":
        toLocation = pile3   
    elif toLocation == "4":
        toLocation = pile4
    elif toLocation == "5":
        toLocation = pile5
    elif toLocation == "6":
        toLocation = pile6 
    elif toLocation == "7":
        toLocation = pile7
    elif toLocation == "8":
        toLocation = pile8
    elif toLocation == "9":
        toLocation = pile9    
    #print(pilePull)
    for i in range(int(moveNumber)):
        variable = pilePull.pop(len(pilePull)-(1+(int(moveNumber)-(i+1))))
        #print(variable)
        #print(pilePull)
        toLocation.append(variable)
    
print(pile1[len(pile1)-1])
print(pile2[len(pile2)-1])
print(pile3[len(pile3)-1])
print(pile4[len(pile4)-1])
print(pile5[len(pile5)-1])
print(pile6[len(pile6)-1])
print(pile7[len(pile7)-1])
print(pile8[len(pile8)-1])
print(pile9[len(pile9)-1])


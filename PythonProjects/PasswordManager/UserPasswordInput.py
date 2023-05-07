import string

class UserPasswordInput:
    
    #Constructor

    def __init__(self,character,password):
        #Sets all the variables needed
        self.character = character
        self.num = False
        self.special = False
        self.cap = False
        self.count = len(password)>=8
    #toString
    def __str__(self):
        #This is how I determine if the user wants to put in account iformation or file information
        #for localVariable in list
        return(out)
    


    #setters 
    def special(charcter):
        if (character in string.punctuation):
            special = True
            return(special)
    def Caps(character):
        if (character in string.ascii_uppercase):
            cap = True
            return(cap)
    def num(character): 
        if (character in string.digits):
            num = True
            return(num)

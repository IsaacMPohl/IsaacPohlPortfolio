class documentAddInfo:
    
    #Constructor

    def __init__(self,userName, firstName, lastName, password,num):
        #Sets all the variables needed
        self.userName = userName 
        self.firstName = firstName
        self.lastName = lastName
        self.password = password
        self.num = num

    #toString
    def __str__(self):
        #This is how I determine if the user wants to put in account iformation or file information
        if self.num == 1:
            out=f"{self.lastName},{self.firstName},{self.password},{self.userName}"
        elif self.num == 2:
            out=f"{self.userName},{self.firstName},{self.lastName}"

        #for localVariable in list
        return(out)
    

    #getters
    def getFirstName(self):
        return self.firstName
    def getLastName(self):
        return self.lastName
    def userName(self):
        return self.userName
    def password(self):
        return self.password

    #setters 
    #This function adds the information into the txt files
    def write(add,document):
        fileToWriteTo = open(document, "a")
        fileToWriteTo.write(f"{add.__str__()} \n")  
        fileToWriteTo.close()
    #This function creates txt files
    def createName(category,userName):
        fileToWriteTo = open(f"C{category}{userName}.txt ", "a")
        fileToWriteTo.close()
    

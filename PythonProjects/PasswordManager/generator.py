import string
import random

class Generator:
  
  def __init__(self,password=""):
    
    if password:
      self.password=password
      self.checkStrength()
      
    else:
      self.genPassword()
      self.string=True
      
  def checkStrength(self):
    password=self.password
    num = False
    special = False
    cap = False
    count = len(password)>=8
    
    for character in password:
      
      if (character in string.ascii_uppercase):
        cap = True
        
      elif (character in string.digits):
        num = True
        
      elif (character in string.punctuation):
        special = True
        
    if num and cap and special and count:
      return True
      
    else:
      return False
      
  def genPassword(self):
    allPossibleChars=string.ascii_letters+string.digits+string.punctuation
    self.password = ""
    
    while(not self.checkStrength()):
      index=random.randint(0,len(allPossibleChars)-1)
      newChar=allPossibleChars[index]

      if newChar == ",":
        newChar=""
      
      if newChar != "\\":
        self.password = self.password+newChar
        
  def __str__(self):
    return self.password


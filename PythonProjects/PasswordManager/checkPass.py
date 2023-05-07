import string
class CheckPossiblePass:
  while True:
    password = input("What is your password? ")
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
    if num and cap and special and count == True:
      break
    else:
      print("Password does not meet requirements. Please try again.")
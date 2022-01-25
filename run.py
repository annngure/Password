
from user import User
#from credentials import Credentials

usernames=[]
passwords=[]
email=[]

def register():
  usernames.append(input("Enter your username"))
  passwords.append(input("Enter your password"))
  email.append(input("Enter your email"))

def login():
    username = input("Enter your username")
    password= input("Enter your Password")
    if username in usernames and password in passwords:
      print ("Welcome!")
    else:
       print("Incorrect!")

def main():
     print("")
    
while True:
    account_ready= input("Select : a:Sign Up  b:Login  c:Exit ")
    if account_ready =="a":
     register()
    if account_ready=="b":
     login()
    if account_ready=="c":
      break
    # elif:
    # print("Invalid ,Select : a:Sign Up  b:Login  c:Exit!")
    if __name__=='__main__':
      main()
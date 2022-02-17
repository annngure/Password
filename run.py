from user import User
from credentials import Credentials


def create_useraccount(username, password):
    '''
    create user account
    '''
    new_user= User(username, password)

    return new_user


def save_user(user):
    '''
    save user
    '''
    user.save_user()
    
def save_credentials(Credentials):
    '''
    save credentials
    '''
    credentials.save_credentials

def find_user(username):
    '''
    find user account
    '''
    return User.find_user(username)

def create_credentials(account,password,email):
    '''
    create credentials methods
    '''
    new_cred= Credentials(account,password,email)
    return new_cred

def save_cred(cred):
    '''
    save credentials
    '''
    cred.save_cred()

def display_cred():
    '''
    display all the saved credentials
    '''
    return Credentials.display_cred()

def find_account(account):
    '''
    search for an account
    '''
    return Credentials.find_account(account)

def delete_cred(account):
    '''
    delete account
    '''
    account.delete_cred()


username=[]
passwords=[]
email=[]

def register():
  username.append(input("Enter your username"))
  passwords.append(input("Enter your password"))
  email.append(input("Enter your email"))

def login():
    username = input("Enter your username")
    password= input("Enter your Password")
    if username in username and password in passwords:
      print ("Welcome to Password Locker!")
    else:
       print("Incorrect!")

def main():
     print("")
    
while True:
    account_ready= input("Select : a:Sign Up  b:Login  c:Exit  d:display_accounts")
    if account_ready =="a":
     register()
    if account_ready=="b":
     login()
    if account_ready=="c":
      break
    elif account_ready =="d":
        if  display_cred():
            print("All accounts displayed here:")
        for account in display_cred():
            print(f"{cred.account}\n {cred.email}\n {cred.password}")
        else:
             print("invalid input!")
     
if __name__=='__main__':
  main()
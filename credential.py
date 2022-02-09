class Credentials:
 '''
 create generations of new users
 
 '''
 credential_list=[] #empty arry to save a list of accounts

def __init__(self,usernames,passwords,account):
    self.usernames=usernames  
    self.passwords=passwords
    self.account=account
#save new user objects in the user_list
def save_cred(self):
    Credentials.credential_list.append(self)
    
#append method is used to add a new user


#delete credential account
def delete_cred(self):
     Credentials.credential_list.remove(self)

@classmethod
def find_user(find,account):
    '''
    find username using search terms
    '''
    for credential in find .credential_list:
        if credential.account == account:

           return credential
    
import pyperclip #function used to copy and paste from the comp

class Credentials:
    '''
    create new user accounts
    '''
    cred_list=[] #empty for new user accounts

def __init__(self,account,email,passlock):
    self.account=account
    self.email=email
    self.passlock=passlock

#save function
def save_cred(self):
    '''
    save credentials in cred_list
    '''
    Credentials.cred_list.append(self)

#delete function
def delete_cred(self)
Credentials.cred_list.remove(self)

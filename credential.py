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

#used to find credentials.....@classmethod ..inbuild function to return class.
@classmethod
    def find_account(cls, account):
        '''
        search for accounts
        '''
        for cred in cls.cred_list:
            if cred.account == account:
                return cred    

#for confirmation
@classmethod
    def cred_exists(cls, account):
        '''
        confirm a class actually exists
        '''
        for cred in cls.cred_list:
            if cred.account == account:
                return True
        return False  

#display
@classmethod
    def display_cred(cls):
        '''
        method that returns all credentials
        '''
        return cls.cred_list                

#copying password
@classmethod
    def copy_passlock(cls, passlock):
            find_account = Credentials.find_account(passlock)
            pyperclip.copy(find_account.passlock)    
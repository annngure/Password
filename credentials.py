class Credentials:
    '''
    create generations of new account

    '''
    cred_list=[] #empty arry to save a list of accounts

    def __init__(self,account,email,password):
        self.account=account
        self.password=password
        self.email=email
#save new user objects in the user_list
    def save_cred(self):
        Credentials.cred_list.append(self)
    
#append method is used to add a new user


#delete credential account
    def delete_cred(self):
        Credentials.cred_list.remove(self)
    
    @classmethod
    def find_account(cls,account):
        '''
        find creds using search terms
        '''
        for cred in cls.cred_list:
            if cred.account == account:
                return cred
    

    @classmethod
    def cred_exists(cls, account):
        '''
        credentials actually exists
        '''
        for cred in cls.cred_list:
            if cred.account == account:
                return True
        return False 

    @classmethod
    def display_cred(cls):
        '''
        returns all credentials
        '''
        return cls.cred_list
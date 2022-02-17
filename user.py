class User:
    '''
     create generations of new users
    '''
    user_list = []  #empty arry to save a list of users
    
    def __init__(self, username, password):
        '''
        saving user credentials into user_list for login
        '''
        self.username = username
        self.password = password
#save new user objects in the user_list

    def save_user(self):
        User.user_list.append(self)

        #append method is used to add a new user

       #delete user account
    def delete_user(self):
        '''
        delete a user account
        '''
        User.user_list.remove(self)


        

    @classmethod
    def find_user(cls, username):
        '''
        find username using search terms
        '''
        for user in cls.user_list:
            if user.username == username:
                return  user
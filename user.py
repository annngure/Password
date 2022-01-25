class User:
 '''
 create generations of new users
 
 '''
 user_list=[] #empty arry to save a list of users

 def User(self,usernames,passwords):
    self.usernames=usernames  
    self.passwords=passwords

#save new user objects in the user_list
def save_user(self):
    User.user_list.append(self)
#append method is used to add a new user

#delete user account
def delete_user(self):
    User.user_list.remove(self)

@classmethod
def find_user(find,usernames):
    '''
    find username using search terms
    '''
    for user in find .user_list:
        if user.usernames == usernames:

           return user
    

class User:
 '''
 #create generations of new users
 
 '''
 user_list=[] #empty arry to save a list of users

 def__init__(self,user_name,password):
     self.user_name=user_name  
     self.password=password

#save new user objects in the user_list
def save_user(self):
    User.user_list.append(self)
#append method is used to add a new user

#delete user account
def delete_user(self):
    User.user_list.remove(self)
    

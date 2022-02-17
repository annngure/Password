import unittest
from user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        '''
        run before each test
        '''
        self.new_user=User("ann","ngure12")

    def test_init(self):
        '''
        check if user class is initialized
        '''
        self.assertEqual(self.new_user.username,"ann")
        self.assertEqual(self.new_user.password,"ngure12")
            
 
    def test_save_user(self):
        '''
        check if user can be saved in user_list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)


    def tearDown(self):
        '''
        clean up after each test
        '''
        User.user_list=[]

  
   
    def test_delete_user(self):
         '''
         check if user test can be delete
         '''
         self.new_user.save_user()
         test_user = User("test","password")
         test_user.save_user()
         self.new_user.delete_user()
         self.assertEqual(len(User.user_list),1)
    
   
    def test_find_user(self):
        '''
        find a user using username
        '''
        self.new_user.save_user()
        test_user = User("test", "password")
        test_user.save_user()
        found_user = User.find_user("ann")
        self.assertEqual(found_user.username, self.new_user.username)

if __name__ =="__main__":
    unittest.main()
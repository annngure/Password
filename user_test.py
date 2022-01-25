import unittest
from user import User
class TestUser(unittest.TestCase):

    def setUp(self):
        '''
        run before each test
        '''
        self.new_user=User("Ann","1234","annngurewanjiku@gmail.com")

    def tearDown(self):
        '''
        clean up to prevent errors
        '''
        User.user_list=[]

    def test_init(self):
        '''
        check if user class is initialized
        '''
        self.assertEqual(self.new_cred.username,"Ann")
         self.assertEqual(self.new_cred.passlock,"12345")
        self.assertEqual(self.new_cred.email,"annngurewanjiku@gmail.com")
    
    def test_save_user(self):
        '''
        check if user can be saved in user_list
        '''
         self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

     def test_delete_user(self):
        '''
        check if user test can be delete
        '''
        self.new_user.save_user()
        test_user=User("Name","password","testuser")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

    def test_search_for_user(self):
        '''
        test if user can be searched for
        '''
        self.new_user.save_user()
        test_user=User("Name","password","testuser)
        test_user.save_user()
        find_user=User.find_usernames("Name")
        self.assertEqual(find_user.usernames,test_user.usernames)

    def test_confirm_user_exists(self):
        '''
        confirm that user exsits
        '''
        self.new_user.save_user()
        test_user.save_user()
        user_exists= User.user_exists("Name")
        self.assertTrue(user_exists)
    
   
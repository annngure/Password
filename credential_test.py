import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
     
     def setUp(self):
         '''
         setup before a test is run
         '''
         self.new_cred= Credentials("Ann","12345","annngurewanjiku@gmail.com")

    def tearDown(self):
        '''
        clear list before test is run
        '''
        Credentials.cred_list=[]

    def test_init(self):
        '''
        check if initialization is done as expected
        '''
        self.assertEqual(self.new_cred.username,"Ann")
         self.assertEqual(self.new_cred.passlock,"12345")
        self.assertEqual(self.new_cred.email,"annngurewanjiku@gmail.com")
       

    def test_save_credentials(self):
        '''
        check if credentials can be saved
        '''
        self.new_cred.save_cred()
        self.assertEqual(len(Credentials.cred_list),1)

    def test_delete_credentials(self):
        '''
        check if credentials test can be delete
        '''
        self.new_cred.save_cred()
        test_cred=Credentials("Name","password","testuser")
        test_cred.save_cred()
        self.new_cred.delete_cred()
        self.assertEqual(len(Credentials.cred_list),1)

    def test_search_for_cred(self):
        '''
        test if credentials can be searched for
        '''
        self.new_cred.save_cred()
        test_cred=Credentials("Name","password","testuser)
        test_cred.save_cred()
        find_cred=Credentials.find_usernames("Name")
        self.assertEqual(find_cred.usernames,test_cred.usernames)

    def test_confirm_cred_exists(self):
        '''
        confirm that credentials exsits
        '''
        self.new_cred.save_cred()
        test_cred.save_cred()
        cred_exists= Credentials.cred_exists("Name")
        self.assertTrue(cred_exists)
    
    d
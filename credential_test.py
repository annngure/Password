import unittest
from credentials import Credentials
import pyperclip

class TestCredentials(unittest.TestCase):
     
     def setUp(self):
         '''
         setup before a test is run
         '''
         self.new_cred= Credentials("Gmail","annngurewanjiku@gmail.com","12345")

    def tearDown(self):
        '''
        clear list before test is run
        '''
        Credentials.cred_list=[]

    def test_init(self):
        '''
        check if initialization is done as expected
        '''
        self.assertEqual(self.new_cred.account,"Gmail")
        self.assertEqual(self.new_cred.email,"annngurewanjiku@gmail.com")
        self.assertEqual(self.new_cred.passlock,"12345")

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
        test_cred=Credentials("Facebook","testuser","password")
        test_cred.save_cred()
        self.new_cred.delete_cred()
        self.assertEqual(len(Credentials.cred_list),1)

    def test_search_for_cred(self):
        '''
        test if credentials can be searched for
        '''
        self.new_cred.save_cred()
        test_cred=Credentials("Facebook","testuser","password")
        test_cred.save_cred()
        find_cred=Credentials.find_account("Facebook")
        self.assertEqual(find_cred.account,test_cred.account)

    def test_confirm_cred_exists(self):
        '''
        confirm that credentials exsits
        '''
        self.new_cred.save_cred()
        test_cred.save_cred()
        cred_exists= Credentials.cred_exists("Facebook")
        self.assertTrue(cred_exists)
    
    def test_dispaly_credentials(self):
        '''
        if all credentials can be displayed
        '''
        self.assertEqual(Credentials.dispaly_cred(),Credentials.cred_list)

    def test_copy_password(self):
        '''
        test if password can be copied
        '''
        self.new_cred.save_cred()
        Credentials.copy_passlock("12345")
        self.assertEqual(self.new_cred.passlock,pyperclip.paste())
import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):

    def setUp(self):
        '''
        setup before a test is run
        '''
        self.new_cred = Credentials("Google","annngurewanjiku@gmail.com","ngure12")
    def tearDown(self):
        '''
        clear list before any test is run
        '''
        Credentials.cred_list = []


    def test_init(self):
        '''
        check if instances initialize as expected
        '''
        self.assertEqual(self.new_cred.account, "Google")
        self.assertEqual(self.new_cred.email, "annngurewanjiku@gmail.com")
        self.assertEqual(self.new_cred.password, "ngure12")


    def test_save_credentials(self):
        '''
        check if credentials can be saved
        '''  
        self.new_cred.save_cred()
        self.assertEqual(len(Credentials.cred_list),1)

       
    def test_saving_multiple_creds(self):
        '''
        check if users can store multiple credentials
        '''
        self.new_cred.save_cred()
        test_cred = Credentials("Instagram", "testuser","password")
        test_cred.save_cred()
        self.assertEqual(len(Credentials.cred_list),2)


    def test_delete_credentials(self):
        '''
        test if you can delete credentials test
        '''
        self.new_cred.save_cred()
        test_cred = Credentials("Instagram", "testuser","password")
        test_cred.save_cred()
        self.new_cred.delete_cred()
        self.assertEqual(len(Credentials.cred_list), 1)

    def test_search_for_cred(self):
        '''
        test if credentials can be searched for
        '''
        self.new_cred.save_cred()
        test_cred = Credentials("Instagram", "testuser","password")
        test_cred.save_cred()
        find_cred= Credentials.find_account("Instagram")
        self.assertEqual(find_cred.account, test_cred.account)
        
        
    def test_confirm_cred_exists(self):
        '''
        confirm that credentials actually exists
        '''
        self.new_cred.save_cred()
        test_cred = Credentials("Instagram", "testuser","password")
        test_cred.save_cred()
        cred_exists = Credentials.cred_exists("Instagram")
        self.assertTrue(cred_exists)

        
    def test_display_credentials(self):
        '''
        test if all credentials can be displayed
        '''
        self.assertEqual(Credentials.display_cred(), Credentials.cred_list)


if __name__ =="__main__":
    unittest.main()
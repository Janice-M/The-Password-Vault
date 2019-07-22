import unittest
import pyperclip
import random

from password import User, Credential

class TestUser (unittest.TestCase):
    ''' Test class that defines test cases for the user class behaviours.
    Args: unittest.TestCase: helps in creating test cases '''
    def setUp(self):
        ''' Function to create a user account before each test '''
        
        self.test_user = User('Janice','somepassword0123')

    def test__init__(self):
        ''' Test to if check the initialization/creation of user instances is properly done '''
        
        self.assertEqual(self.test_user.loginUsername,'Janice')
        self.assertEqual(self.test_user.loginPassword,'somepassword0123')
    
    def verify(self):
        """ This function verifies togin to enable users to access their vault """
        self.test_user=  User('Janice','somepassword0123')
        

if __name__ == '__main__':
	unittest.main(verbosity=2)
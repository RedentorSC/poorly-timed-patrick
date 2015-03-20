import unittest
import os
from patrick import PatrickBot

class TestPatrickBot(unittest.TestCase):

    def setUp(self):
        self.pwd_environ_var = "patrick_p"
        self.bot = PatrickBot()

    def test_password_environment_var(self):
        '''
        Make sure environment variable patrick_p 
        is set to something on this machine
        '''
        self.assertTrue(bool(os.environ.get(self.pwd_environ_var)))

    def test_login(self):
        self.assertTrue(self.bot.login())

if __name__ == '__main__':
    unittest.main()

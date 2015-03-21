import unittest
import os
from patrick import PatrickBot

class TestPatrickBot(unittest.TestCase):

    def setUp(self):
        self.pwd_environ_var = "patrick_p"
        self.bot = PatrickBot()
        self.test_comment_true = " is this the krusty krab"
        self.test_comment_false = "oh long johnson"

    def test_password_environment_var(self):
        '''
        Make sure environment variable patrick_p 
        is set to something on this machine
        '''
        self.assertTrue(bool(os.environ.get(self.pwd_environ_var)))

    def test_login(self):
        self.assertTrue(self.bot.login())

    def test_is_flagged_comment(self):
        self.assertTrue(self.bot.is_flagged_comment(self.test_comment_true))
        self.assertFalse(self.bot.is_flagged_comment(self.test_comment_false))
    
    def test_acquire_comments(self):
        self.assertTrue(self.bot.acquire_comments())


    
if __name__ == '__main__':
    unittest.main()

import unittest

class TestShittyPatrickBot(unittest.TestCase):

    def setUp(self):
        pass

    def test_password_environment_var(self):
        '''
        Make sure environment variable patrick_p 
        is set to something on this machine
        '''
        pass

    def test_login(self):
        try:
            # login(username, password)

        except:
            self.fail()

if __name__ == '__main__':
    unittest.main()

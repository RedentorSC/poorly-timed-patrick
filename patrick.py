import os
import praw

class PatrickBot(object):
    '''
    No! This is Patrick!
    '''

    def __init__(self):
        self.r         = praw.Reddit(user_agent = 'shitty_patrick_bot')
        self.logged_in = False

    def login(self):
        '''
        Returns True  if login was successful
        Returns False if an exception was thrown
        '''
        try:
            self.r.login('shitty_patrick_bot', os.environ['patrick_p'])
            self.logged_in = True
            return True

        except:
            return False



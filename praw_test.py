import praw

class ShittyPatrickBot(object):
    '''
    No! This is Patrick!
    '''

    def __init__(self):
        self.r         = praw.Reddit(user_agent = 'shitty_patrick_bot')
        self.logged_in = False
        pass

    def login(self):
        '''
        Returns True if login was successful, False if an exception 
        was thrown.
        '''
        self.logged_in = True

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


    def is_flagged_comment(self, comment):
        '''take in a comment, determine if its valid, return true'''
        comment = comment.lower().strip()
        if comment.startswith("is this"):
            return True
        else:
            return False
    
    '''
    def acquire_comments(self):
        subreddit = r.get_subreddit('benpringle')
        for submission in subreddit.get_new(limit = 10):
            if submission.is_flagged_comment:
                submission.respond

    '''



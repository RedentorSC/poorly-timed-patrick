import os
import praw
import time
import sys
import logging

class PatrickBot(object):
    '''
    No! This is Patrick!
    '''

    def __init__(self):
        logging.getLogger().setLevel(logging.INFO)

        self.r              = praw.Reddit(user_agent = 'shitty_patrick_bot')
        self.subreddits     = ["spongebob", "shittyaskscience", "starcraft", "adviceanimals", "benpringle", "starcraftcirclejerk", "me_irl", "funny"]
        self.response       = "No, this is Patrick. \n\n\n\n\n\n^This ^message ^was ^created ^by ^a ^bot"
        self.sleep_time     = 10 * 60
        self.comment_ids    = set()

    def login(self):
        """Returns True  if login was successful
        Returns False if an exception was thrown
        """
        logging.info("Attempting login...")
        try:
            self.r.login('shitty_patrick_bot', os.environ['patrick_p'])
            logging.info("Login successful.")
            return True
        except:
            logging.info("Login failed.")
            return False

    def is_flagged_comment(self, comment):
        """Check for comments starting with 'is this' """
        return comment.body.lower().strip().startswith("is this")
    
    def already_done(self, comment):
        """Check if we have already written a reply in a previous run."""
        self.comment_ids = set([c.parent_id for c in self.r.user.get_comments()])
        return comment.fullname in self.comment_ids

    def _process_comment_obj(self, comment):
        """Recursively handle MoreComments objects"""
        if isinstance(comment, praw.objects.MoreComments):
            for obj in comment.comments():
                self._process_comment_obj(obj)

        elif isinstance(comment, praw.objects.Comment):
            if self.is_flagged_comment(comment) and not self.already_done(comment):                    
                logging.info("Replying to comment from {}. Text: {}".format(comment.author, comment.body))
                comment.reply(self.response)
                comment.upvote()

    def process_comments(self, subreddit):
        """Grab 25 submissions from a subreddit and reply to any flagged comments."""
        subreddit = self.r.get_subreddit(subreddit)
        for submission in subreddit.get_hot(limit = 25):
            flat_comments = praw.helpers.flatten_tree(submission.comments)
            for comment in flat_comments:
                try:
                    self._process_comment_obj(comment)
                except Exception as e:
                    logging.warning(e)
                    continue

    def run(self):
        """The main loop, which runs once every 15 minutes. 
        Looks through self.subreddits and replies to any (new) flagged comments."""
        self.login()
        while True:
            logging.info("Searching through the following subreddits: {}".format(self.subreddits))
            for subreddit in self.subreddits:
                logging.info("Searching {}".format(subreddit))
                self.process_comments(subreddit)
            logging.info("Sleeping for {} ms...".format(self.sleep_time))
            time.sleep(self.sleep_time)

if __name__ == '__main__':
    bot = PatrickBot().run()






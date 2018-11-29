"""Helper functions for working with reddit"""

import random, praw
import datetime as dt
import secrets.secrets as secrets

def start_reddit():
  """Instantiate an instance of Reddit"""
  return praw.Reddit(client_id=secrets.CLIENT_ID, \
                     client_secret=secrets.CLIENT_SECRET, \
                     user_agent="influence-impressions", \
                     username=secrets.USERNAME, \
                     password=secrets.PASSWORD)

def random_subreddit(instance, choices=["Hearthstone"]):
    """Returns a random subreddit object from a list of names."""
    return instance.subreddit(random.choice(choices))

def specific_subreddit(instance, name="Hearthstone"):
    """Returns a subreddit object from name."""
    if name:
        return instance.subreddit(name)
    return False

def get_submissions_by_date(start="", end=dt.datetime.now(dt.timezone.utc)):
    print(end)
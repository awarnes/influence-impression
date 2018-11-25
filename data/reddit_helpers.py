"""Helper functions for working with reddit"""

import praw

import secrets.secrets as secrets

def start_reddit():
  """Instantiate an instance of Reddit"""
  return praw.Reddit(client_id=secrets.CLIENT_ID, \
                     client_secret=secrets.CLIENT_SECRET, \
                     user_agent="influence-impressions", \
                     username=secrets.USERNAME, \
                     password=secrets.PASSWORD)
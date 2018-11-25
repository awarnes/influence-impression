#! /usr/local/bin/python3

import praw
import pandas as pd
import datetime as dt
import random
import json

import secrets.secrets as secrets

reddit = praw.Reddit(client_id=secrets.CLIENT_ID, \
                     client_secret=secrets.CLIENT_SECRET, \
                     user_agent="influence-impressions", \
                     username=secrets.USERNAME, \
                     password=secrets.PASSWORD)

subreddit_names = ["Hearthstone", "NintendoSwitch"]

subreddit = reddit.subreddit(random.choice(subreddit_names))

for submission in subreddit.new(limit=1):
  print(submission.title, submission.id, submission.author)
  author = submission.author

  redditor = reddit.redditor(author)

  print(redditor.name)
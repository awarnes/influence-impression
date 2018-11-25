#! /usr/local/bin/python3

import random, json, praw
import pandas as pd

import helpers.helpers as helpers
import data.reddit_helpers as rh
import data.save_data as sd

reddit = rh.start_reddit()

subreddit_names = ["Hearthstone", "NintendoSwitch"]

def random_subreddit(choices=subreddit_names):
    """Returns a random subreddit object from a list of names."""
    return reddit.subreddit(random.choice(choices))

def specific_subreddit(name):
    """Returns a subreddit object from name."""
    if name:
        return reddit.subreddit(name)
    return False

def format_subreddit_posts():
    pass

subreddit = random_subreddit()

topics_dict = {
    "title":[], \
    "score":[], \
    "id":[], "url":[], \
    "comms_num": [], \
    "created": [], \
    "body":[]
}

for submission in subreddit.new():
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(helpers.get_date(submission.created))
    topics_dict["body"].append(submission.selftext)

topics_data = pd.DataFrame(topics_dict)
name = "test{}.csv".format(random.randint(0,9))

sd.save_to_csv(topics_data, name, folder="/rand/")

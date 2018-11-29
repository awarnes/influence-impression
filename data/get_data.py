#! /usr/local/bin/python3

"""
Test Submission:
submission = reddit.submission(id="a19k3f") # Arena Patron Release submission
print(submission.author.name)
pprint.pprint(json.dumps(str(vars(submission))))

From what appears available (11/28/18) we'll want to pull everything
in the submission except the private vars (_comments_by_id)
and translate author -> author.name and subreddit -> subreddit.display_name
"""

import pprint

import helpers.helpers as helpers
import data.reddit_helpers as rh
import data.crud_helpers as crud

reddit = rh.start_reddit()

def format_subreddit_posts():
    pass

# Set to Hearthstone for purposes of this poc test project
hearthstone = rh.specific_subreddit(reddit)




# topics_dict = {
#     "title":[], \
#     "score":[], \
#     "id":[], "url":[], \
#     "comms_num": [], \
#     "created": [], \
#     "body":[]
# }

# for submission in subreddit.new():
#     topics_dict["title"].append(submission.title)
#     topics_dict["score"].append(submission.score)
#     topics_dict["id"].append(submission.id)
#     topics_dict["url"].append(submission.url)
#     topics_dict["comms_num"].append(submission.num_comments)
#     topics_dict["created"].append(helpers.get_date(submission.created))
#     topics_dict["body"].append(submission.selftext)

# topics_data = pd.DataFrame(topics_dict)
# name = f"test{random.randint(0,9)}.pkl"

# crud.pickle_df(topics_data, name, folder="/rand/")

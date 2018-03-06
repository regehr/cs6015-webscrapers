import praw # Python wrapper for reddit API
import sys # Allows to get command-line inputs
import operator # Allows sorting a dictionary into a tuple

# can use: help(class type here) to get info about the objecect type
# can use: print(vars(class variable here) to get variables of the class


# Reddit object is what provides convenient access to Reddit's API
reddit = praw.Reddit("BOT") # BOT/login info comes from the praw.ini.
DATA_LIMIT = 100.0 # Number of data points to be gathered (max is 1000)
redditorName = sys.argv[1]  # Get the redditor from the commandline
redditor = reddit.redditor(redditorName)


def topTenDetails ( redditor, list):

    # Collects a tally of the 1000 newest comments from this user
    subreddits = dict()
    for dataPoint in list:

        subReddit = "/" + dataPoint.subreddit_name_prefixed  # This comment's sub

        # If this subreddit is already in the dictionary
        if subreddits.has_key(subReddit):
            subreddits[subReddit] = subreddits[subReddit] + 1

        # If the subreddit isn't in the dictionary
        else:
            subreddits[subReddit] = 1

    # Sorts the dictionary by value into a list of tuples
    sortedValues = sorted(subreddits.items(), key=operator.itemgetter(1), reverse=True)
    # Print out the results
    for pair in sortedValues[0:10]:
        percent = (pair[1] / DATA_LIMIT) * 100
        print(pair[0] + " " + str(pair[1]) + " - " + str(percent) + "%")


comments = redditor.comments.new(limit=DATA_LIMIT)
posts = redditor.submissions.new(limit=DATA_LIMIT)
upvoted = redditor.upvoted()


topTenDetails(redditor, comments)



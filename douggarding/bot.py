import praw # Python wrapper for reddit API
import sys # Allows to get command-line inputs
import operator # Allows sorting a dictionary into a tuple

# can use: help(class type here) to get info about the objecect type
# can use: print(vars(class variable here) to get variables of the class

# Reddit object is what provides convenient access to Reddit's API
reddit = praw.Reddit("BOT") # BOT/login info comes from the praw.ini.
DATA_LIMIT = 1000.0 # Number of data points to be gathered (max is 1000)
redditorName = sys.argv[1]  # Get the redditor from the commandline
redditor = reddit.redditor(redditorName)
comments = redditor.comments.new(limit=DATA_LIMIT) # List of redditors newest comments
posts = redditor.submissions.new(limit=DATA_LIMIT) # List of redditors newest posts

'''
Takes a redditor object and a list of their data (either their comments or submissions).
It then prints to the console the their top 10 subreddits and the percent of their activity
that went into each. 

Print type variable accepts "reddit" and "console". If "reddit" is used, then a string is
returned that will display the data in a table form on reddit. otherwise the data will 
be printed to the console
'''
def topTenDetails ( redditor, list, printType):

    # Collects a tally of the 1000 newest comments from this user
    subreddits = dict()
    dataPoints = 0.0
    for dataPoint in list:
        dataPoints += 1.0
        subReddit = dataPoint.subreddit_name_prefixed  # This comment's sub

        # If this subreddit is already in the dictionary
        if subreddits.has_key(subReddit):
            subreddits[subReddit] = subreddits[subReddit] + 1

        # If the subreddit isn't in the dictionary
        else:
            subreddits[subReddit] = 1

    # Sorts the dictionary by value into a list of tuples
    sortedValues = sorted(subreddits.items(), key=operator.itemgetter(1), reverse=True)


    if printType == "reddit":
        message = "SUBREDDIT|COMMENTS|PERCENT\n:--|:--|:--"
        # Print out the results
        for pair in sortedValues[0:10]:
            percent = round((pair[1] / dataPoints) * 100, 2)
            newDataEntryString = "\n/" + pair[0] + "|" + str(pair[1]) + "|" + str(percent) + "%"
            message += newDataEntryString
        return message

    else:
        # set to print for console
        for pair in sortedValues[0:10]:
            percent = round((pair[1] / dataPoints) * 100, 2)
            print(pair[0] + " | " + str(pair[1]) + " | " + str(percent) + "%")

'''
This method will read in new and unread messages that come to the user represented
by this bot. The message subject, sender, and the message itself will be printed to 
the console, and the message will be marked as read.
'''
def readInbox():
    for message in reddit.inbox.stream():

        # Read the message
        sender = str(message.author)
        print("Subject: " + str(message.subject))
        print("Sender: " + sender)
        print("Message: " + str(message.body))
        message.mark_read()

        # Send a message with subreddit usage data to the redditor
        redditor = reddit.redditor(sender)
        list = redditor.comments.new(limit=DATA_LIMIT)  # List of redditors newest comments
        message = topTenDetails(redditor, list, "reddit")
        reddit.redditor(sender).message("Your subreddit data", message)


topTenDetails(redditor, comments, "console")
#readInbox()

print("\nEND PROGRAM")


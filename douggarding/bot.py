import praw # Python wrapper for some reddit API

# can use: help(class type here) to get info about the objecect type
# can use: print(vars(class variable here) to get variables of the class

# BOT info comes from the praw.ini. Contains login info related to this bot and  account
# Reddit object is what provides convenient access to Reddit's API
reddit = praw.Reddit("BOT")


inbox = reddit.inbox
#help(inbox)

for message in inbox.all():
    # print(message.body) # message.body gets the text of the message
    # can do: author, name, created, body,

    print(message.author)
    print(message.subject)
    print(message.body)


#instance of a subreddit
subreddit = reddit.subreddit("test")
# print out data related to the subreddit
print(subreddit.display_name)
print(subreddit.title)
print(subreddit.description)


#instance of a redditor
wildSketchRedditor = reddit.redditor("AWildSketchAppeared")
print(wildSketchRedditor.comment_karma)


for comment in wildSketchRedditor.comments.new(limit=1):
    print(comment.body.split('\n', 1)[0][:79])




'''
for submission in reddit.subreddit("learnpython").new(limit=2):
    print(submission.title)
'''


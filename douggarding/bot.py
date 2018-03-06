import praw

reddit = praw.Reddit("BOT") # bot info comes from the praw.ini

print(reddit.user.me())

#instance of a subreddit
subreddit = reddit.subreddit("test")
# print out data related to the subreddit
print(subreddit.display_name)
print(subreddit.title)
print(subreddit.description)

#instance of a redditor
wildSketchRedditor = reddit.redditor("AWildSketchAppeared")
print(wildSketchRedditor.comment_karma)



for submission in reddit.subreddit("learnpython").new(limit=2):
    print(submission.title)
import praw
import pandas as pd
import random

#enter your data
username=""
client_id=""
client_secret=""
password=""

reddit_instance=praw.Reddit(
    username=username,
    client_id=client_id,
    client_secret=client_secret,
    password=password,
    user_agent="test_bot"
)

#so we don't spam use r/testingground4bots
subreddit = reddit_instance.subreddit("testingground4bots")
#to verify that you're connected
#print(subreddit)
df=pd.DataFrame()
titles=[]
scores=[]
ids=[]
#set limit to None for real time data analysis?
#it grabs 100 posts by default
posts=subreddit.new(limit=50)
for post in posts:
    titles.append(post.title)
    scores.append(post.score) #upvotes
    ids.append(post.id)
df['Id']=ids   
df['Titles'] = titles
df['Upvotes'] = scores
df = df.sort_values(by=['Upvotes'])
print(df)
df2=[]
df2=df['Id']
print(df2)
randomNum=random.random()*10
randomNum=int(randomNum)
randomPostId = df2[randomNum]
comments = reddit_instance.submission(randomPostId)
print(comments.comments)
for comment in comments.comments:
        comment_text = comment.body.lower()
        print(comment_text)
        if "test" in comment_text:
            comment.reply("testComment")
            
            
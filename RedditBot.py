import praw
from random import randint
import time
import toolazytoini

# initialize with appropriate values 
client_id = toolazytoini.client_id
client_secret = toolazytoini.client_id 
username = toolazytoini.username
password = toolazytoini.password
user_agent = toolazytoini.user_agent
redirect_uri = toolazytoini.redirect_uri
  
# creating an authorized reddit instance 
reddit = praw.Reddit(client_id = client_id,
                     client_secret = client_secret,  
                     username = username,  
                     password = password, 
                     user_agent = user_agent) 

subreddit = reddit.subreddit('mechanicalMercs')

print("THE BOT LIVES!")

for submission in subreddit.top(limit=5):
    submission.upvote()
    print(f"{submission} upvoted to {submission.score}")

keywords = ['gamble']

#calls since last restart
call_counter = 0

print('Checking...')
for comment in subreddit.stream.comments(skip_existing=True):
    print('Regular Comment...')
    cbody = comment.body
    if any(keyword in cbody for keyword in keywords) and comment.author != 'BotBot816': #if any keywords from keywords are found, add them to a list and if that list has anything in it, return true.  Found at https://www.reddit.com/r/redditdev/comments/8mp0yu/can_i_search_for_comments_including_specific/ though I also had to look into list comprehension to understand it
        for reply in comment.replies:
            if reply.author == 'BotBot816':
                break

        #keyword lister
        found_keywords = []
        for word in keywords:
            if word in cbody:
                found_keywords.append(word)
        print(found_keywords)


        #which keyword?
        #gamble rolls a 3 sided die to decide whether to upvote, downvote, or abstain from voting on a comment.        
        if 'gamble' in found_keywords:
            vote = randint(0,2)
            reply = 'You have decided to take a gamble, with your karma on the line!\n'
            if vote == 0:
                vote = 'n downvote'
                comment.downvote()
                reply += 'However, unfortunately for you, you have taken a downvote.\n'
            elif vote == 1:
                vote = 'n upvote'
                comment.upvote()
                reply += 'You have won the gamble!  Take the upvote!\n'
            else:
                vote = ' nonvote'
                reply += 'But nothing happens...\n'

            #IMPORTANT
            if call_counter == 0: #as it adds 1 after it is complete
                s = ''
            else: s = 's'

            #sets the remaining part of the reply
            reply += f'\n\n^This ^makes ^{call_counter + 1} ^call{s} ^since ^my ^last ^reset'

            #replies to the comment with the results
            comment.reply(reply)

            print(f'{comment.author} said "{cbody}"\nHe rolled a{vote}.\n\n')

        call_counter += 1
        
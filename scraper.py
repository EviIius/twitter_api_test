import tweepy
import time
import pandas as pd

consumer_key = "dk496UnzFlpfOn2hnxc8r1KPc" #Your API/Consumer key 
consumer_secret = "XdDgsppveB9M8coZnbRaSVZmDdf9YmmdFGjY4mJbqeC4WlbkDQ" #Your API/Consumer Secret Key
access_token = "1231455706445778945-yztrJ9pVwytEqUXKgd7Q3sPtzauRkz"    #Your Access token key
access_token_secret = "4ElmRoKULbDszg9f2KbZknXVXv1FBN325GGF1uEfwdPxQ" #Your Access token Secret key

#Pass in our twitter API authentication key
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_token, access_token_secret
)

#Instantiate the tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True)



####PROFILE SCRAPER####
'''
username = "NotPaulGG"
no_of_tweets =100

try:
    #The number of tweets we want to retrieved from the user
    tweets = api.user_timeline(screen_name=username, count=no_of_tweets)
    
    #Pulling Some attributes from the tweet
    attributes_container = [[tweet.created_at, tweet.favorite_count,tweet.source,  tweet.text] for tweet in tweets]

    #Creation of column list to rename the columns in the dataframe
    columns = ["Date Created", "Number of Likes", "Source of Tweet", "Tweet"]
    
    #Creation of Dataframe
    tweets_df = pd.DataFrame(attributes_container, columns=columns)
except BaseException as e:
    print('Status Failed On,',str(e))
    time.sleep(3)
    '''

####MEDIA SCRAPER####

search_query = "sex for grades"
no_of_tweets =150

try:
    #The number of tweets we want to retrieved from the search
    tweets = api.search_tweets(q=search_query, count=no_of_tweets)
    
    #Pulling Some attributes from the tweet
    attributes_container = [[tweet.user.name, tweet.created_at, tweet.favorite_count, tweet.source,  tweet.text] for tweet in tweets]

    #Creation of column list to rename the columns in the dataframe
    columns = ["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"]
    
    #Creation of Dataframe
    tweets_df = pd.DataFrame(attributes_container, columns=columns)
except BaseException as e:
    print('Status Failed On,',str(e))
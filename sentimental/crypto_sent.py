import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

import plotly.plotly as py
import plotly.graph_objs as go

import plotly
import plotly.graph_objs

class TwitterClient(object):
    '''
        Generic Twitter Class for sentiment analysis.
        '''
    def __init__(self):
        '''
            Class constructor or initialization method.
            '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = 'bJST2PXuMFLE7Kdaw4YkpF3HH'
        consumer_secret = 'PZapPrwxc2lwi1Sj1fMNSxM68hOJlbKJpEV7q5duKVUTIGH7ru'
        access_token = '937024531067232256-xdtdQQq51w9HLDbMSr59z11ZIAu5bre'
        access_token_secret = '0U0aSiwhSHpgBQMc7hnKxmBpPKbSVKY9x5ND49cixLFwz'
        
        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

def clean_tweet(self, tweet):
    '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
            return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

        def get_tweet_sentiment(self, tweet):
        '''
            Utility function to classify sentiment of passed tweet
            using textblob's sentiment method
            '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

def get_tweets(self, query, count = 10):
    '''
        Main function to fetch tweets and parse them.
        '''
            # empty list to store parsed tweets
            tweets = []
                
                try:
                    # call twitter api to fetch tweets
                    fetched_tweets = self.api.search(q = query, count = count)
                        
                        # parsing tweets one by one
                        for tweet in fetched_tweets:
                            # empty dictionary to store required params of a tweet
                            parsed_tweet = {}
                                
                                # saving text of tweet
                                parsed_tweet['text'] = tweet.text
                                    # saving sentiment of tweet
                                    parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
                                        
                                        # appending parsed tweet to tweets list
                                        if tweet.retweet_count > 0:
                                            # if tweet has retweets, ensure that it is appended only once
                                            if parsed_tweet not in tweets:
                                                tweets.append(parsed_tweet)
                                                    else:
                                                        tweets.append(parsed_tweet)
                                                            
                                                            # return parsed tweets
                                                            return tweets
                                                                
                                                                except tweepy.TweepError as e:
                                                                    # print error (if any)
                                                                    print("Error : " + str(e))



def main():
    # creating object of TwitterClient Class
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = 'crypto', count = 200)
    
    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    # percentage of negative tweets
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
    # percentage of neutral tweets
    neutweets = 100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets)
    print("Neutral tweets percentage: {} %".format(100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets)))
    # printing first 5 positive tweets
    #print("\n\nPositive tweets:")
    #for tweet in ptweets[:10]:
    #    print(tweet['text'])
    
    # printing first 5 negative tweets
    #print("\n\nNegative tweets:")
    #for tweet in ntweets[:10]:
    #    print(tweet['text'])
    
    trace1 = go.Bar(
                    x=[':)'],
                    y=[ptweets],
                    name=':)'
                    )
                    trace2 = go.Bar(
                                    x=[':()'],
                                    y=[ntweets],
                                    name=':()'
                                    )
                    trace3 = go.Bar(
                                    x=[':|'],
                                    y=[ntweets],
                                    name=':|'
                                    )
                    data = [trace1, trace2,trace3]
                    layout = go.Layout(
                                       barmode='group'
                                       )
                    
                    
                    
                    plotly.offline.plot({
                                        "data": [plotly.graph_objs.Bar(
                                                                       x=['^__^','$__$','>__<'],
                                                                       y=[100*len(ptweets)/len(tweets),neutweets,100*len(ntweets)/len(tweets)],
                                                                       marker=dict(
                                                                                   color=['rgba(141,236,120,1)', 'rgba(255,207,145,0.8)',
                                                                                          'rgba(165,30,44,1)']),)]})


if __name__ == "__main__":
    # calling main function
    main()

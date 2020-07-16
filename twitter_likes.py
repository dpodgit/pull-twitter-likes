"""
Author: David O'Dwyer
Date: May 2020
"""

import twitter_credentials
import tweepy
import json
from tweepy import OAuthHandler
from tweepy import API


class TweetFinder():

    """
    A class that opens a connection to the Twitter API and pulls
    text-of and link-to x-number of favourited tweets of specified user.

    Number of tweets and user handle (@username) are via user input.

    Returned tweets dumped into formatted JSON in current working dir.

    Abides by Twitter API rate limit.
    Authentical credentials referenced from twitter_credentials.py 
    
    """

    def __init__(self, consumer_key, consumer_secret,
            access_token, access_token_secret):

        try:

            self.consumer_key = consumer_key
            self.consumer_secret = consumer_secret
            self.access_token = access_token
            self.access_token_secret = access_token_secret

            self.auth = OAuthHandler(self.consumer_key, self.consumer_secret)
            self.auth.set_access_token(self.access_token, self.access_token_secret)

        except:
            print("Authentication Credentials Invalid")
            exit()

    def get_tweets(self, handle, number_of_tweets):

        """
        Input:  User handle, via main(), via user input
                Number of tweets to retrieve, via main(), via user input; 
                    most to least recent.

        Output: Formatted JSON containing tweets' text, in current working dir.

        Connects to API & authenticals with credentials;
        With rate limit, pulls specified number of tweets;
        Adds tweets' text to a dictionary;
        Dumps dictionary to JSON
        """

        try:

            api = API(self.auth)

            user=handle

            favs = tweepy.Cursor(api.favorites, id=user, \
                    wait_on_rate_limit=True, wait_on_rate_limit_notify=True, \
                    tweet_mode='extended').items(number_of_tweets)

            favs_text = dict()
            i=0

            for f in favs:
                favs_text[i] = f.full_text
                i += 1

            with open("tweets.json", "w") as outfile:
                json.dump(favs_text, outfile, sort_keys=True,\
                     indent=4, separators=(',', ': '))

        except:
            
            print("Could not retrieve tweets. Ensure handle and number of tweets are valid.")

def main():

    user_handle = input("Type the handle of the user (e.g. @user): ")
    number_tweets = int(input("Type the number of tweets to retrieve: "))

    twitter_finder = TweetFinder(
        twitter_credentials.CONSUMER_KEY,
        twitter_credentials.CONSUMER_SECRET,
        twitter_credentials.ACCESS_TOKEN,\
        twitter_credentials.ACCESS_TOKEN_SECRET)

    return twitter_finder.get_tweets(user_handle, number_tweets)


if __name__ == "__main__":
    main()

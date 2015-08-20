# Author: Jason Chang

# Libraries needed
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sys

# Twitter credentials
consumer_key = 'UTQo43HVZJVmqydZ1S2hiPDaw'
consumer_secret = 'uCXkRQpeJ1Wy55whXsrOFnVuIWBzl3uBmZKtCoGCJyDkbdKkJB'
access_token = '627714227-XgUMt9espQA69FAAw5qbb6KPB0FtqGC2jSt2dyEx'
access_secret = 'FnoJwswLnEFsiY7O3BRqy87ZZMOUdRTmmSja4xTgpTPWX'

# Listener class instance
# Determines what to do with tweets
class Listener(StreamListener):
    # Formats stream of tweets into desired format
    def on_data(self, data):
        d = json.loads(data)  # Deserializes/Parses JSON into a Python dictionary using a conversion table.
        # makes sure there is text in the tweet
        if u'text' in d.keys():
            # converts unicode text to string
            unicode_string = d['text']
            encoded_string = unicode_string.encode('utf-8')
            d['text'] = encoded_string
            print d['text']
        else:
            pass
        return True
        
    # prints out error
    def on_error(self, status):
        print >> sys.stderr, 'Encountered error with status code:', status

    def on_timeout(self):
        print >> sys.stderr, 'Timeout'  # prints out timeout
        return True                     # stops program from killing the stream

if __name__ == '__main__':

    # Puts in Twitter authentication and connects to Twitter Streaming API
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    twitterStream = Stream(auth, Listener())

    # This line filters Twitter Streams to capture data by the keywords: 'donald trump', 'jeb bush', 'scott walker', 'marco rubio', 'ben carson', 'ted cruz'
    twitterStream.filter(track=['donald trump', 'jeb bush', 'scott walker', 'marco rubio', 'ben carson', 'ted cruz'])

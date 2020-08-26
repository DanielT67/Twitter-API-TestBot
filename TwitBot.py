import tweepy
import time
consumer_key = 'f4gxKarngTxW1KVUDwurwMzbf'  # api key
consumer_secret = 'kxHafmG5HZaOkMRNytP1aaZtFDnwoWZaREFTJo2skZ5oob7bq4'  # api secret key
key = '1292952619611295763-Pw8komq5UHFKJnJLTen2OQhmhI1Z0E'  # access token
secret = 'dYdkxwk29m6MKpi9lGCYglLBFlxw4G9vFyXQgxmOgyLO6'  #access token secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

FILE_NAME = "LastSeen.txt"

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id


def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return


user = api.me()

search = 'Python'
numTweets = 5

for tweet in tweepy.Cursor(api.search, search).items(numTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(1)
    except tweepy.error.Tweeperror as e:
        print(e.reason)
    except StopIteration:
        break

for follower in tweepy.Cursor(api.followers).items():
    if follower.name == 'Ohno':
        follower.follow()

#This is a test.
import time
import tweepy
import re

consumer_key = "aYvZwGA0cQybvozQmmJzy3a7U"
consumer_secret = "zDZ3oDVzXQKx2ynIErL4xg8K6AbqrUSfmyZQscGDie42M9upCa"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAGNIHAEAAAAAQf8mtmgLxvHsusDoa5PzpdkviME%3DQ7vf4dNyUpsbgaNnqhiILouK5WNvs6GSxwjUlMgQStAnTt3hTX"
access_key = "1250139000444198913-JUbjRvIdhaJLs8wDusfvYkhhkgoEbF"
access_secret = "SlNRbqJ2W5OEjBaypeElp7zLUVcjh5bgMDvIP5VvmEKWF"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

with open("GenericTextDoc.txt", "r", encoding = "utf-8") as f:
    text = f.read()


TWEET_instance = re.compile(r'TWEET')
match = TWEET_instance.findall(text)

i = 0
while i <= 16:
    if i < 16:
        time.sleep(1)
        print("Tweeting in ", 15 - i, "seconds.")
        i += 1
    if i == 16:
        print(match)
        i = 0
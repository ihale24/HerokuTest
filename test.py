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

with open("Harry_Potter_and_the_Philosopher's_Stone.txt", "r", encoding = "utf8") as f:
    text = f.read()

text_watermark_stripped = re.sub(r'Page |[^.]*Harry Potter and the Philosophers Stone - J.K. Rowling', ' ', text)
text_mrs_stripped = re.sub(r'Mrs.', 'Mrs', text_watermark_stripped)
text_mr_stripped = re.sub(r'Mr\.', 'Mr', text_mrs_stripped)

text_wang_replacement = re.sub(r'[Ww]and ','wang ', text_mr_stripped)
text_plural_wang_replacement = re.sub(r'[Ww]ands ','wangs ', text_wang_replacement)
text_period_wang_replacement = re.sub(r'[Ww]and\.', 'wang.', text_plural_wang_replacement)

Hagrid_instance = re.compile(r'Hagrid')
match = Hagrid_instance.findall(text)

i = 0
while i <= 16:
    if i < 16:
        time.sleep(1)
        print("Finding Hagrid in", 15 - i, "seconds.")
        i += 1
    if i == 16:
        print(match)
        i = 0
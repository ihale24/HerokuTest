#This is a test.
import time
import tweepy
import re

#Twitter API keys
consumer_key = "aYvZwGA0cQybvozQmmJzy3a7U"
consumer_secret = "zDZ3oDVzXQKx2ynIErL4xg8K6AbqrUSfmyZQscGDie42M9upCa"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAGNIHAEAAAAAQf8mtmgLxvHsusDoa5PzpdkviME%3DQ7vf4dNyUpsbgaNnqhiILouK5WNvs6GSxwjUlMgQStAnTt3hTX"
access_key = "1250139000444198913-JUbjRvIdhaJLs8wDusfvYkhhkgoEbF"
access_secret = "SlNRbqJ2W5OEjBaypeElp7zLUVcjh5bgMDvIP5VvmEKWF"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

#opening Harry Potter text file
with open("Harry_Potter_and_the_Philosopher's_Stone.txt", "r", encoding = "utf8") as f:
    text = f.read()

#stripping files of watermarks, Mrs. and Mr.
text_watermark_stripped = re.sub(r'Page |[^.]*Harry Potter and the Philosophers Stone - J.K. Rowling', ' ', text)
text_mrs_stripped = re.sub(r'Mrs.', 'Mrs', text_watermark_stripped)
text_mr_stripped = re.sub(r'Mr\.', 'Mr', text_mrs_stripped)

#replacing "wand" in its various forms with "wang"
text_wang_replacement = re.sub(r'[Ww]and ','wang ', text_mr_stripped)
text_plural_wang_replacement = re.sub(r'[Ww]ands ','wangs ', text_wang_replacement)
text_period_wang_replacement = re.sub(r'[Ww]and\.', 'wang.', text_plural_wang_replacement)

#finding all instances of the word "wang" along with its preceeding sentence
wang_instance = re.compile(r'[^.?!]*[.?!][^.?!]*?wang[^.]*?[\.\?\!]')
matches = wang_instance.findall(text_period_wang_replacement)

#establish wang instance counter
instance = 16

#set up timer
timer = 0
while timer <= 86401: 
    if timer < 86401: #while less than 86401, print countdown every second and increment timer
        time.sleep(1)
        print("Tweeting next quote in", 86400 - timer, "seconds.")
        timer += 1
    if timer == 86401: #when timer hits 86401, Tweet th latest instance and print confirmation along with instance number
        api.update_status(matches[instance])
        print("Just tweeted this:", matches[instance])
        print("Instance number:", instance)
        timer = 0
        instance+=1 #increment wang instance counter
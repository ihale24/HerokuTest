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
   #for testing: C:\\Users\\Isaac\\Anaconda3\\THIS_FOLDER_CONTAINS_CODE\\HerokuTest\\Harry_Potter_and_the_Philosopher's_Stone.txt
    text = f.read()

#stripping files of watermarks, Mrs. and Mr.
text_watermark_stripped = re.sub(r'Page |[^.]*Harry Potter and the Philosophers Stone - J.K. Rowling', ' ', text)
text_mrs_stripped = re.sub(r'Mrs.', 'Mrs', text_watermark_stripped)
text_mr_stripped = re.sub(r'Mr\.', 'Mr', text_mrs_stripped)

#replacing "wand" in its various forms with "wang"
text_wang_replacement = re.sub(r'[Ww]and ','wang ', text_mr_stripped)
text_comma_wang_replacement = re.sub(r'[Ww]and,','wang,', text_wang_replacement)
text_plural_wang_replacement = re.sub(r'[Ww]ands ','wangs ', text_comma_wang_replacement)
text_period_wang_replacement = re.sub(r'[Ww]and\.', 'wang.', text_plural_wang_replacement)

#finding all instances of the word "wang" along with its preceeding sentence
wang_instance = re.compile(r'[^.?!]*[.?!][^.?!]*?wang[^.]*?[\.\?\!]')
matches = wang_instance.findall(text_period_wang_replacement)

timer = 0 #set up timer

while timer <= 61: 
    if timer < 61: #while less than 61, print countdown every second and increment timer
        time.sleep(1)
        print("Tweeting next quote in", 60 - timer, "seconds.")
        timer += 1
    if timer == 61: #when timer hits 61, Tweet the latest instance and print confirmation along with instance number
        with open("wang_instance.txt", "r", encoding = "utf8") as w:
        #for testing, use: C:\\Users\\Isaac\\Anaconda3\\THIS_FOLDER_CONTAINS_CODE\\HerokuTest\\wang_instance.txt
            instance = int(w.read())
        api.update_status(matches[instance]) #update status with quote corresponding to instance number
        print("Just tweeted this:", matches[instance], "Instance number: ", instance)
        instance+=1 #increment wang instance counter
        with open("wang_instance.txt", "w", encoding = "utf8") as n:
            n.write(str(instance)) #rewrite text document with new instance number
        timer = 0

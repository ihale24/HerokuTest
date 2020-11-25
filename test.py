import time
import tweepy
import re

#Twitter API keys
consumer_key = "aYvZwGA0cQybvozQmmJzy3a7U"
consumer_secret = "zDZ3oDVzXQKx2ynIErL4xg8K6AbqrUSfmyZQscGDie42M9upCa"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAGNIHAEAAAAAQf8mtmgLxvHsusDoa5PzpdkviME%3DQ7vf4dNyUpsbgaNnqhiILouK5WNvs6GSxwjUlMgQStAnTt3hTX"
access_key = "1250139000444198913-JUbjRvIdhaJLs8wDusfvYkhhkgoEbF"
access_secret = "SlNRbqJ2W5OEjBaypeElp7zLUVcjh5bgMDvIP5VvmEKWF"

#Twitter API authorization & establishing API object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

#opening Harry Potter text file
with open("harrypotterandthesorcerer'sstone.txt", "r", encoding = "utf8") as f:
   #for testing: C:\\Users\\Isaac\\Anaconda3\\THIS_FOLDER_CONTAINS_CODE\\HerokuTest\\harrypotterandthesorcerer'sstone.txt
    text = f.read()

#stripping text document of periods in "Mr." and "Mrs."
text_mrs_stripped = re.sub(r'Mrs\.', 'Mrs', text)
text_mr_stripped = re.sub(r'Mr\.', 'Mr', text_mrs_stripped)

#compiling all sentences that use the word "wand" and their preceding sentence into a list
#wand_instance = re.compile(r'[^.?!]*[.?!]|\"(?<=[.!?])[^.?!]*?wand(?=[^aeiouyr])[^.]*?[\.\?\!]')
wand_instance = re.compile(r'[^.?!]*[.?!][^.?!]*?wand(?=[^aeiouyr])[^.?!]*?[.?!]\"?')
matches = wand_instance.findall(text_mr_stripped)

#strip each match of lone quotation marks, newlines, and spaces
for i in range(len(matches)):
    if matches[i].startswith("\""):
        matches[i] = matches[i].replace("\"", "", 1)
    matches[i] = matches[i].strip("\n")
    matches[i] = matches[i].strip(" ")
    matches[i] = re.sub(r'(?<=[Ww]an)d', 'g', matches[i])


# Moaning_Myrtle = api.get_user("moaningg_myrtle")
# status = Moaning_Myrtle.status.text
# current_instance = matches.index(status)
# next_instance = current_instance + 1

timer = 0 

while timer <= 28801: 
    if timer < 28801: #while less than 28801, print countdown every second and increment timer
        time.sleep(1)
        print("Tweeting next quote in", 28800 - timer, "seconds.")
        timer += 1
    if timer == 28801: #when timer hits 28801, Tweet the next instance and print confirmation along with instance number
        
        #refreshes Moaning Myrtle profile information
        Moaning_Myrtle = api.get_user("moaningg_myrtle")
        status_id = Moaning_Myrtle.status.id
        status = api.get_status(status_id, tweet_mode="extended").full_text
        current_instance = matches.index(status)
        next_instance = current_instance + 1

        api.update_status(matches[next_instance])
        print("Just tweeted this:", matches[next_instance], "Instance number: ", next_instance)
        timer = 0

"""
#opening Harry Potter text file
with open("C:\\Users\\Isaac\\Anaconda3\\THIS_FOLDER_CONTAINS_CODE\\HerokuTest\\Harry_Potter_and_the_Philosopher's_Stone.txt", "r", encoding = "utf8") as f:
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
minus_lines = re.sub(r'\n(?=[A-Za-z])', '', text_period_wang_replacement)

#finding all instances of the word "wang" along with its preceeding sentence
wang_instance = re.compile(r'[^.?!]*[.?!][^.?!]*?wang[^.]*?[\.\?\!]')
#wang_instance = re.compile(r'[^.?!]*[./!][A-Za-z\']*wang[^.]*?[\.\?\!]')
matches = wang_instance.findall(minus_lines)


for match in matches:
    if match.startswith(chr(8221)):
        match.replace("\”", "")
        print(match)
        print("match")
        print() 

# tweets = api.user_timeline("moaningg_myrtle")
# recent_tweet = tweets[0].text
# print(matches.index(recent_tweet))

# instance = matches.index(tweets[0].text)
# print(instance)


timer = 0 #set up timer

while timer <= 28801: 
    if timer < 28801: #while less than 28801, print countdown every second and increment timer
        time.sleep(1)
        print("Tweeting next quote in", 28800 - timer, "seconds.")
        timer += 1
    if timer == 28801: #when timer hits 28801, Tweet the latest instance and print confirmation along with instance number
        with open("wang_instance.txt", "r", encoding = "utf8") as w:
        #for testing, use: C:\\Users\\Isaac\\Anaconda3\\THIS_FOLDER_CONTAINS_CODE\\HerokuTest\\wang_instance.txt
            instance = int(w.read())
        api.update_status(matches[instance]) #update status with quote corresponding to instance number
        print("Just tweeted this:", matches[instance], "Instance number: ", instance)
        instance+=1 #increment wang instance counter
        with open("wang_instance.txt", "w", encoding = "utf8") as n:
            n.write(str(instance)) #rewrite text document with new instance number
        timer = 0
"""
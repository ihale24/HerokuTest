#This is a test.
import time
import tweepy
import requests

with open("GenericTextDoc.txt", "r", encoding = "utf-8") as f:
    text = f.read()

i = 0
while i <= 16:
    if i < 16:
        time.sleep(1)
        print("Tweeting in ", 15 - i, "seconds.")
        i += 1
    if i == 16:
        print(text)
        i = 0
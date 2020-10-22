#This is a test.
import time

i = 0
while i <= 16:
    if i < 16:
        time.sleep(1)
        print("Tweeting in ", 15 - i, "seconds.")
        i += 1
    if i == 16:
        print("TWEET")
        i = 0
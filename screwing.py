import webbrowser
import time
import random

while True:
    sites = random.choice(['www.google.com','www.youtube.com','www.udemy.com'])
    visit = "https://{}".format(sites)
    webbrowser.open(visit)
    seconds = random.randrange(5,20)
    time.sleep(seconds)
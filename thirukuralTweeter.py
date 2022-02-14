import requests
import tweepy
import random

S = requests.Session()

URL = "https://api-thirukkural.vercel.app/api?num="

idNum = random.randint(1, 1330)
print(idNum)
URL = URL + str(idNum)
R = S.get(url=URL)
DATA = R.json()

#print(DATA["parse"]["text"]["*"])
section = DATA["sect_eng"]
chaptor_grp = DATA["chapgrp_eng"]
#chaptor = DATA["chap_eng"]
kural = DATA["eng"]
kuralExp = DATA["eng_exp"]
static_text = "Thirukural - திருக்குறள்"
breadcrum = section +"/"+ chaptor_grp
tweet_msg = static_text +"\n"+ breadcrum +"\n\n"+ kural +"\n\n"+ kuralExp
print(tweet_msg)
print(len(tweet_msg))
# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create API object
api = tweepy.API(auth)
api.verify_credentials()
try:
    api.verify_credentials()
    print("Authentication Successful")
except:
    print("Authentication Error")

# Create a tweet
api.update_status(tweet_msg)
print("tweet published")

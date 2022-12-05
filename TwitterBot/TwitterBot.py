import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

api = tweepy.API(auth)

try:
   api.verify_credentials()
   print("Authentication OK")
except:
    print("Error during authentication")

api.update_status("Cyber100 is a great class!")

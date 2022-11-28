import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("LDeMINB5gnQJUqdNCsUIUhekX", 
    "p3kcJ6PzMpIbff0j2yaXCavFrNvAyBFT3YBfiiGWl9UVVpCutK")
auth.set_access_token("1597108682571087883-KBkckZ0S0SU6OCyGbkGb6uv5GIyf8Y", "pWt843BiIo2PB8PvhM17YuiejxqAxOWwMVJS5HrppcdFH")

api = tweepy.API(auth)


try:
   api.verify_credentials()
   print("Authentication OK")
except:
    print("Error during authentication")

api.update_status("Hello Tweepy!")

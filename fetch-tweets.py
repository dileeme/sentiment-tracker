import tweepy  

# Twitter API keys (replace with your own)
api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_secret = "YOUR_ACCESS_SECRET"

# Authenticate
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# Fetch tweets
query = "$AAPL OR #StockMarket -filter:retweets"
tweets = api.search_tweets(q=query, count=100, lang="en")

for tweet in tweets:
    print(tweet.text)

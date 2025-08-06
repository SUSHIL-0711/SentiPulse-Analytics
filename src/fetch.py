# --- src/fetch.py ---
import tweepy
from config import BEARER_TOKEN

client = tweepy.Client(bearer_token=BEARER_TOKEN)

def fetch_tweets(query, max_results=20):
    response = client.search_recent_tweets(query=query, max_results=max_results, tweet_fields=["text", "created_at"])
    tweets = [tweet.text for tweet in response.data] if response.data else []
    return tweets

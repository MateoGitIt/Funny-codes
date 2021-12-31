import tweepy

consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)


def main_bot():

    harvard_keywords = ["Harvard University", "Harvard", "Crimson", "Harvard Yard",
                        "Harvard Bridge", "Apley Court", "Canaday", "Grays",
                        "Greenough", "Hollis" , "Holworthy" , "Hurlbut", "Lionel",
                        "Mower", "Massachusetts Hall", "Matthews", "Pennypacker",
                        "Stoughton", "Straus", "Thayer", "Weld", "Wigglesworth"
                        "Annenberg Hall", "Veritas", "Veritaffle", "Adams House"
                        "Currier House", "Cabot House", "Dudley Co-op",
                        "Dunster House", "Leverett House", "Eliot House",
                        "Kirkland House", "Lowell House", "Mather House",
                        "Pforzheimer House", "Quincy House", "Winthrop House",
                        "Harvard Statue", "John Harvard", "Memorial Church"
                        "Harvard Library", "Harvard Science Center",
                        "Harvard Innovation Lab", "Loker Reading Room",
                        "Harvard Commons", "Smith Campus Center"]

    for i in harvard_keywords:
        kws = i

    # Find tweets with keywords
    fetched_tweets = tweepy.Cursor(api.search, q=kws, rpp=100).items()
    for tweet in fetched_tweets:
        def filter_major_kws():
            if "Harvard" in tweet.text:
                return True
            else:
                return False
        interactions = (tweet.favorite_count + tweet.retweet_count)
        if interactions >= 5:
            if filter_major_kws():
                try:
                    api.create_favorite(id=tweet.id)
                    api.retweet(id=tweet.id)
                except Exception:
                    pass

    # Everything Harvard tweets will be RT'd and liked
    harvard_tweets = api.user_timeline(screen_name="Harvard")
    for tweet in harvard_tweets:
        harvard_interactions = (tweet.favorite_count + tweet.retweet_count)
        if harvard_interactions >= 70:
            try:
                api.create_favorite(id=tweet.id)
                api.retweet(id=tweet.id)
            except Exception:
                pass

if __name__ == "__main__":
    main_bot()

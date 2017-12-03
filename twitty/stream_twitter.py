from tweepy.streaming import StreamListener
import asyncio
import re
import requests
from aylienapiclient import textapi

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self):
        super().__init__()
        self.bot = None
        self.channel = None
        self.id = []
        self.client = textapi.Client("57b03f56", "a9d04e2fb4b3a79c090c02d2c2797eda")
        return
    def on_status(self,data):
        if "RT" not in data._json['text']:
            for i in self.id:
                if int(data._json['user']['id']) == int(i):
                    value = "https://twitter.com/statuses/" + data._json['id_str']
                    asyncio.run_coroutine_threadsafe(self.bot.send_message(self.channel, value), self.bot.loop)
        return True

    def set_discord(self,client):
        self.bot = client
        return self.bot

    def set_channel(self,channel):
        self.channel = channel

    def set_id(self,id):
        self.id = id

    def on_error(self, status):
        print(status)




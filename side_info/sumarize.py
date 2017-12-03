import discord
import datetime
import aiohttp
import async_timeout
import asyncio
from random import randint
from aylienapiclient import textapi

class Sumarize():
    def __init__(self, auth,url,limit):
        self.auth = str(auth).split("#")
        self.auth = self.auth[0]
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        self.id = "None"
        self.client = textapi.Client("57b03f56", "a9d04e2fb4b3a79c090c02d2c2797eda")
        self.url = url
        self.limit = int(limit)
        return

    def sum(self):
        value_sum = value_sent = sumarize = sentiment = ""
        list_v = []
        try:
            sentiment = self.client.Sentiment({'url': self.url})
            sumarize = self.client.Summarize({'url': self.url, 'sentences_number': self.limit})
        except Exception as e:
            print(e)
        try:
            for i in sumarize['sentences']:
                value_sum += str(i) + "\n\n"
            value_sum = "```" + value_sum + "```"
            value_sent += "\n```css\nAnalyse of the present link in the tweet :\nPolarity : " + str(
                sentiment['polarity_confidence']) + " [" + str(sentiment['polarity']) \
                     + "]\nSubjectivité : " + str(sentiment['subjectivity_confidence']) + " [" + str(
                sentiment['subjectivity']) + "]```"
        except Exception as e:
            value_sum = value_sent = "```Your link is apparently not valid```"
            print(e)
        list_v.append([value_sum,value_sent])
        return list_v
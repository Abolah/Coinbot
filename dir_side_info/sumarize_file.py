import datetime
from random import randint
from aylienapiclient import textapi


class Class_Summarize:
    def __init__(self, auth, article_url, limit):
        self.auth = str(auth).split("#")
        self.auth = self.auth[0]
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        self.id = "None"
        self.client = textapi.Client("57b03f56", "a9d04e2fb4b3a79c090c02d2c2797eda")
        self.url = article_url
        self.limit = int(limit)
        return

    def function_sum(self):
        value_sum = value_sent = summarize = ""
        list_v = []
        try:
            summarize = self.client.Summarize({'url': self.url, 'sentences_number': self.limit})
        except Exception as e:
            print(e)
        try:
            for i in summarize['sentences']:
                value_sum += str(i) + "\n\n"
            value_sum = "```" + value_sum + "```"
        except Exception as e:
            value_sum = value_sent = "```Your link is apparently not valid```"
            print(e)
        list_v.append([value_sum, value_sent])
        return list_v

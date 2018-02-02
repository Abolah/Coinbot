from pymarketcap import Pymarketcap
import datetime
from random import randint
import json


class Class_Catalysts:
    def __init__(self, auth):
        self.auth = str(auth).split("#")
        self.auth = self.auth[0]
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        return

    @staticmethod
    def function_cmc(coin):
        global name, ticker
        coin = coin.upper()
        coinmarketcap = Pymarketcap()
        cmc_json = coinmarketcap.ticker(coin)
        ticker = cmc_json["symbol"]
        name = cmc_json["name"]
        full_name = name + "%20" + "(" + ticker + ")"
        return full_name

    @staticmethod
    def function_cmcal(full_name, event_type):
        cmcal_url = "https://coinmarketcal.com/api/events?page=1&max=16&coins=" + full_name + "&showPastEvent=false"
        print(cmcal_url)
        return event_type




    @staticmethod
    def function_display_event(data, pwet):
        print(data, pwet)
        return data

    def get_catalysts(self, coin, event_type):
        get_coin = self.function_cmc(coin)
        get_event = self.function_cmcal(get_coin, event_type)
        return get_event

import datetime
from random import randint
from pymarketcap import Pymarketcap
import aiohttp
import async_timeout
import asyncio
import discord
import time


class Class_Binance:
    def __init__(self, auth):
        self.auth = str(auth).split("#")
        self.auth = self.auth[0]
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        self.default_cmc = "You need to provide a coin to check."
        self.name = "None"
        return

    async def function_cmc(self, coin):
        global cmc_json, ticker
        if coin == "":
            value_mc = self.default_cmc
        else:
            coin = coin.upper()
            coinmarketcap = Pymarketcap()
            cmc_json = coinmarketcap.ticker(coin, convert="EUR")
            marketcap = "MC : " + "$ " + "{:,}".format(float(cmc_json["market_cap_usd"])) + "\n"
            price = "Price : " + "$" + "{0:.3f}".format(float(cmc_json["price_usd"])) + " | " + "{0:.3f}".format(
                float(cmc_json["price_eur"])) + "€      \n"
            rank = "Rank : [Rank " + str(cmc_json["rank"]) + "]\n"
            change_1 = "1h Swing : " + str(cmc_json["percent_change_1h"]) + "%\n"
            change_24 = "24h Swing : " + str(cmc_json["percent_change_24h"]) + "%\n"
            change_7 = "7 days Swing : " + str(cmc_json["percent_change_7d"]) + "%\n"
            value_mc = "```css\n" + str(rank) + str(marketcap) + str(price) + str(change_1) + str(change_24) + str(
                change_7) + "```"

            self.name = cmc_json["name"]
        return value_mc

    async def function_fetch(self):
        print("yo")

    async def binance_query(self, coin):
        ticker = self.function_cmc(coin)
        print(ticker)

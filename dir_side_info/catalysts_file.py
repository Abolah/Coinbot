import json
import discord
import datetime
import aiohttp
import async_timeout
import asyncio
from random import randint


class Class_Catalysts:
    def __init__(self, auth):
        self.auth = str(auth).split("#")
        self.auth = self.auth[0]
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        self.long_name = "None"
        self.idcoin = "None"
        self.generalcmc = "None"
        self.symbol = "None"
        return

    async def function_cmc(self, coin):
        global cmcal
        print("Coin : " + coin)
        try:
            async with aiohttp.ClientSession() as session:
                async with async_timeout.timeout(5):
                    async with session.get("https://api.coinmarketcap.com/v1/ticker/?limit=1000&convert=EUR") as resp:
                        if resp.status == 200:
                            self.generalcmc = await resp.json()
        except asyncio.TimeoutError as e:
            self.generalcmc = "Timeout Error"
            print(e)
        except Exception as e:
            print(e)
            return -1
        try:
            for i in self.generalcmc:
                if i["symbol"] == self.coin.upper():
                    self.symbol = i["symbol"]
                    self.long_name = i["name"]
                    self.idcoin = i["id"]
                    cmcal = self.long_name + " (" + self.symbol + ")"
                    print("CMCAL name : " + cmcal)
                    break
        except Exception as e:
            print(e)
            return -1
        return cmcal

    async def function_display_event(self, data):
        print(data)

    async def get_catalysts(self, coin, event_type):
        print("Catalysts file, get_catalysts function")
        print("Coin : " + coin)
        print("Event : " + event_type)
        data = await self.function_cmc(coin)
        embed = self.function_display_event(data)
        return embed

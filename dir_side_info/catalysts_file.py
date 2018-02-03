import discord
from pymarketcap import Pymarketcap
import datetime
from random import randint
import json
import urllib.request


class Class_Catalysts:
    def __init__(self, auth):
        self.auth = str(auth).split("#")
        self.auth = self.auth[0]
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        return

    @staticmethod
    def function_cmc(coin):
        if coin == "":
            full_name = ""
        else:
            global name, ticker
            coin = coin.upper()
            coinmarketcap = Pymarketcap()
            cmc_json = coinmarketcap.ticker(coin)
            ticker = cmc_json["symbol"]
            name = cmc_json["name"]
            full_name = name + "%20" + "(" + ticker + ")"
        return full_name

    @staticmethod
    def function_cmcal(self, full_name, event_type):
        global title, coin_name, date, desc, cat
        event_type = event_type.capitalize()
        if event_type == "" and full_name == "":
            cmcal_url = "https://coinmarketcal.com/api/events?page=1&max=5&showPastEvent=false"
        elif full_name == "":
            cmcal_url = "https://coinmarketcal.com/api/events?page=1&max=5&categories=" + event_type + "&showPastEvent=false"
        elif event_type == "":
            cmcal_url = "https://coinmarketcal.com/api/events?page=1&max=5&coins=" + full_name + "&showPastEvent=false"
        else:
            cmcal_url = "https://coinmarketcal.com/api/events?page=1&max=5&coins=" + full_name + "&categories=" + event_type + "&showPastEvent=false"

        with urllib.request.urlopen(cmcal_url) as url:
            full_json = json.loads(url.read().decode())
        for i in full_json:
            title = i["title"]
            coin_name = i["coin_name"]
            date_event = i["date_event"]
            date = date_event.split("T")
            date = date[0]
            desc = i["description"]
            cat = i["categories"]
            print(title)
            print(coin_name)
            print(date)
            print(desc)
            print(cat)
            print(" \n\n")

        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com", timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.set_thumbnail(url="https://files.coinmarketcap.com/static/img/coins/32x32/bitcoin.png")
        embed.set_footer(text="Request achieved")
        embed.add_field(name=":star2: Incoming events :star2:",
                        value="Here are the informations I could retrieve " + self.auth, inline=False)
        embed.add_field(name=":floppy_disk: Information about the incoming event", value="pwet", inline=True)

        return embed


    def get_catalysts(self, coin, event_type):
        print(event_type)
        get_coin = self.function_cmc(coin)
        embed = self.function_cmcal(get_coin, event_type)
        return embed

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

    def function_cmc(self, coin):
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

    def function_cmcal(self, full_name, event_type):
        event_type = event_type.capitalize()
        if event_type == "" and full_name == "":
            cmcal_url = "https://coinmarketcal.com/api/events?page=1&max=5&showPastEvent=false"
        elif full_name == "":
            cmcal_url = "https://coinmarketcal.com/api/events?page=1&max=5&categories={}&showPastEvent=false".format(
                event_type)
        elif event_type == "":
            cmcal_url = "https://coinmarketcal.com/api/events?page=1&max=5&coins={}&showPastEvent=false".format(
                full_name)
        else:
            cmcal_url = "https://coinmarketcal.com/api/events?page=1&max=5&coins={}&categories={}&showPastEvent=false".format(
                full_name, event_type)

        with urllib.request.urlopen(cmcal_url) as url:
            data_json = json.loads(url.read().decode())
        event = ""
        for i in data_json:
            title = str(i["title"])
            coin_name = str(i["coin_name"])
            date_event = str(i["date_event"])
            date = date_event.split("T")
            date = date[0]
            desc = str(i["description"])
            cat = str(i["categories"])
            event += "[" + coin_name + "]" + " [" + date + "]" + " " + cat + "\n[" + title + "] \n" + desc + "\n\n"
        return event

    def function_display(self, event):
        events = "```css\n" + event + "```"
        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.set_thumbnail(url="https://files.coinmarketcap.com/static/img/coins/32x32/bitcoin.png")
        embed.set_footer(text="Request achieved at")
        embed.add_field(name=":calendar_spiral:  Incoming events :calendar_spiral: ",
                        value="Here are the informations I could retrieve " + self.auth, inline=False)
        embed.add_field(name=":floppy_disk: Information about the incoming events", value=events, inline=True)
        embed.add_field(name= "Data retrieved with :heart: from : ", value="```py\nCoinmarketcal.com\n```", inline=False)
        return embed

    def get_catalysts(self, coin, event_type):
        get_coin = self.function_cmc(coin)
        event = self.function_cmcal(get_coin, event_type)
        embed = self.function_display(event)

        return embed

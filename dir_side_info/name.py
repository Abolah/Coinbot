from random import randint
import datetime
import discord
from pymarketcap import Pymarketcap


class Class_Name:
    def __init__(self):
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        self.name = "None"
        self.eur_price = "None"
        self.btc_price = "None"
        self.usd_price = "None"
        self.coin = "None"
        return

    def function_cmc(self, coin):
        self.coin = coin.upper()
        coin = coin.upper()
        coinmarketcap = Pymarketcap()
        eur_json = coinmarketcap.ticker(coin, convert="EUR")
        btc_json = coinmarketcap.ticker(coin, convert="BTC")
        self.btc_price = btc_json["data"]["quotes"]["BTC"]["price"]
        self.usd_price = eur_json["data"]["quotes"]["USD"]["price"]
        self.eur_price = eur_json["data"]["quotes"]["EUR"]["price"]
        self.name = eur_json["data"]["name"]

    def display(self):
        data = "```css\nThe coin " + self.coin + " has for name " + self.name + "\nThe BTC value is about : " + str(
            self.btc_price) + " BTC" + "\nThe USD value is about : " + str(
            self.usd_price) + "$\nThe EUR value is about : " + str(self.eur_price) + "\n```"
        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.add_field(name=":tada: Informations about " + self.name, value=data, inline=True)
        embed.set_footer(text="Request achieved :")

        return embed

    async def get_name(self, coin):
        self.function_cmc(coin)
        embed = self.display()
        return embed

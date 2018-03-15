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
        cmc_json = coinmarketcap.ticker(coin, convert="EUR")
        self.btc_price = cmc_json["price_btc"]
        self.usd_price = cmc_json["price_usd"]
        self.eur_price = cmc_json["price_eur"]
        self.name = cmc_json["name"]

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

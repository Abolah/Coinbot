from pymarketcap import Pymarketcap
import datetime
import discord
from random import randint


class Class_listing:
    def __init__(self, auth):
        self.auth = str(auth).split("#")
        self.auth = self.auth[0]
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        return

    def function_cmc(self):
        coinmarketcap = Pymarketcap(timeout=10)
        listings = coinmarketcap.listings()
        cmc_list = list()
        for i in listings["data"]:
            cmc_list.append(i)
        last5 = cmc_list[-5:]
        coin = ""
        for c in last5:
            name = str(c["name"])
            ticker = str(c["symbol"])
            coin += "[" + name + "] [" + ticker + "]\n"
        coins = "```css\n" + coin + "```"
        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com", timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.add_field(name=":floppy_disk: 5 last coins listed on CoinMarketCap", value=coins, inline=True)
        embed.set_footer(text="Request achieved :")
        return embed

    async def listing_launch(self):
        embed = self.function_cmc()
        return embed

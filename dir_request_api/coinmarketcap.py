import discord
import datetime
from pymarketcap import Pymarketcap
from random import randint
import requests


class Class_Coinmarketcap:
    def __init__(self, auth):
        self.auth = str(auth).split("#")
        self.auth = self.auth[0]
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        self.currency = "EUR"
        self.url_logo = "https://files.coinmarketcap.com/static/img/coins/32x32/bitcoin.png"
        self.cmc_global_api = "https://api.coinmarketcap.com/v2/global/?convert=EUR"

    async def function_cmcap(self):
        r = requests.get(self.cmc_global_api)
        cmc_json = r.json()

        marketcap = str("MC : " + "$" + "{:,}".format(float(cmc_json["data"]["quotes"]["USD"]["total_market_cap"])) + "\n")
        volume = "Market Volume : ${:,}".format(cmc_json["data"]["quotes"]["USD"]["total_volume_24h"]) + "\n"
        dominance = "Bitcoin Dominance = " + str(cmc_json["data"]["bitcoin_percentage_of_market_cap"]) + "%\n"
        active_markets = "Pairs : " + str(cmc_json["data"]["active_markets"]) + "\n"
        value = "```css\n" + marketcap + dominance + volume + active_markets + "```"

        return value

    async def function_btcap(self):
        coinmarketcap = Pymarketcap()
        cmc_btc = coinmarketcap.ticker("bitcoin", convert=self.currency)
        price = str("Price : " + "$" + "{0:.3f}".format(float(cmc_btc["data"]["quotes"]["USD"]["price"])) + " | " + "{0:.3f}".format(float(cmc_btc["data"]["quotes"]["EUR"]["price"])) + "€      \n")
        volume = "24h Volume: "  "$ " + "{:,}".format(float(cmc_btc["data"]["quotes"]["USD"]["volume_24h"])) + "\n"
        change_1 = "24h Swing : " + str(cmc_btc["data"]["quotes"]["USD"]["percent_change_24h"]) + "%\n"
        change_7 = "7 days Swing : " + str(cmc_btc["data"]["quotes"]["USD"]["percent_change_7d"]) + "%\n\n"
        value_btc = "```css\n" + price + volume + change_1 + change_7 + "```"

        return value_btc

    async def display(self, value, value_btc):
        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.set_thumbnail(url="https://lh3.googleusercontent.com/uZCnvLDpbtQB1KLbM-AGWLhx7W-MxaUmBUOup5VV9y100zE9DXZ8tY_GIEcd8LQ9QhsI=w300")
        embed.add_field(name=":trophy: CoinMarketCap Informations", value=value)
        embed.add_field(name=":medal: Bitcoin Informations", value=value_btc, inline=True)
        embed.set_footer(text="Request achieved :")
        return embed

    async def cmc_query(self):
        cmc = await self.function_cmcap()
        btc = await self.function_btcap()
        embed = await self.display(cmc, btc)
        return embed

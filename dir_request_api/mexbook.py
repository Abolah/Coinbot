from pymarketcap import Pymarketcap
import datetime
import discord
from random import randint
import requests


class Class_BitmexOrderBook:
    def __init__(self, auth):
        self.auth = str(auth).split("#")
        self.auth = self.auth[0]
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        self.default_print = "Default Print"
        self.bitmex_order_book = "https://www.bitmex.com/api/v1/orderBook/L2?symbol=XBT&depth=10"
        self.book_buy = ""
        self.book_sell = ""
        return

    @staticmethod
    def function_cmc():
        coin = "BTC"
        coinmarketcap = Pymarketcap(timeout=10)
        try:
            cmc_json = coinmarketcap.ticker(coin, convert="EUR")
            rank = str("Rank : [Rank " + str(cmc_json["data"]["rank"]) + "]\n")
            if cmc_json["data"]["quotes"]["USD"]["market_cap"] is None:
                marketcap = "MarketCap : Unknown\n"
            else:
                marketcap = str(
                    "MC : " + "$" + "{:,}".format(float(cmc_json["data"]["quotes"]["USD"]["market_cap"])) + "\n")

            price = str(
                "Price : ${0:.3f}".format(float(cmc_json["data"]["quotes"]["USD"]["price"])) + " | {0:.3f}€\n".format(
                    float(cmc_json["data"]["quotes"]["EUR"]["price"])))
            if cmc_json["data"]["quotes"]["USD"]["percent_change_1h"] is None:
                change_1 = "1h Swing : Unknown\n"
            else:
                change_1 = str("1h Swing : " + str(cmc_json["data"]["quotes"]["USD"]["percent_change_1h"]) + "%\n")
            if cmc_json["data"]["quotes"]["USD"]["percent_change_24h"] is None:
                change_24 = "24h Swing : Unknown\n"
            else:
                change_24 = str("24h Swing : " + str(cmc_json["data"]["quotes"]["USD"]["percent_change_24h"]) + "%\n")
            if cmc_json["data"]["quotes"]["USD"]["percent_change_7d"] is None:
                change_7 = "7 days Swing : Unknown\n"
            else:
                change_7 = str("7 days Swing : " + str(cmc_json["data"]["quotes"]["USD"]["percent_change_7d"]) + "%\n")
            value_mc = "```css\n" + rank + marketcap + price + change_1 + change_24 + change_7 + "```"
        except TypeError or KeyError:
            value_mc = "```css\nThis ticker does not exist on Coinmarketcap.\nMaybe you made a typo in the coin's ticker.```"

        return value_mc

    def function_orderbook(self):
        r = requests.get(self.bitmex_order_book)
        order_book_json = r.json()
        for i in order_book_json:
            size = str(i["size"])
            price = str(i["price"])
            side = str(i["side"])
            if side == "Sell":
                self.book_sell += "Size: " + size + " $USD\nPrice: " + price + " $USD\nSide: " + side + "\n\n"
            elif side == "Buy":
                self.book_buy += "Size: " + size + " $USD\nPrice: " + price + " $USD\nSide: " + side + "\n\n"

        return

    def function_display(self, value_mc):
        order_book_buy = "```css\n" + self.book_buy + "```"
        order_book_sell = "```css\n" + self.book_sell + "```"
        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.set_thumbnail(url="https://images.duckduckgo.com/iu/?u=http%3A%2F%2Fcoin-street.com%2Fimg-contents%2Flogo%2FBitMex%2FWeb%2Flogo.png&f=1")
        embed.add_field(name=":medal: CoinMarketCap Informations", value=value_mc, inline=False)
        embed.add_field(name=":octopus: Bitmex OrderBook Buy", value=order_book_buy, inline=True)
        embed.add_field(name=":octopus: Bitmex OrderBook Sell", value=order_book_sell, inline=True)
        embed.set_footer(text="Request achieved :")
        return embed

    async def bitmex(self):
        ticker = self.function_cmc()
        self.function_orderbook()
        embed = self.function_display(ticker)
        return embed

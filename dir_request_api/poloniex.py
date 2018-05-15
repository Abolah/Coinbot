from pymarketcap import Pymarketcap
import datetime
import discord
from random import randint
import requests


class Class_Poloniex:
    def __init__(self, auth):
        self.auth = str(auth).split("#")
        self.auth = self.auth[0]
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        self.name = "None"
        self.poloniex_api_url = "https://poloniex.com/public?command=returnTicker"
        self.key = "None"
        self.pair = "None"
        return

    def function_cmc(self, coin):
        global cmc_json
        if coin == "iota":
            coin = "miota"
        coin = coin.upper()
        coinmarketcap = Pymarketcap(timeout=10)
        try:
            cmc_json = coinmarketcap.ticker(coin, convert="EUR")
            self.name = cmc_json["data"]["name"]
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

    def function_poloniex(self, coin):
        if coin.upper() == "BTC":
            self.pair = coin + "_USDT"
            self.key = "USDT_BTC"
        else:
            self.pair = coin + "_BTC"
            self.key = "BTC_" + coin.upper()

        api_url = self.poloniex_api_url
        r = requests.get(api_url)
        poloniex_json = r.json()

        try:
            if coin == "BTC":
                pair = "Pair : " + self.key.replace("_", "-") + "\n"
                if poloniex_json[self.key]["last"] is None:
                    last = "Last : Unknown\n"
                else:
                    last = "Last : {}\n".format(float(poloniex_json[self.key]["last"]))
                if poloniex_json[self.key]["highestBid"] is None:
                    bid = "Bid : Unknown\n"
                else:
                    bid = "Bid : {}\n".format(float(poloniex_json[self.key]["highestBid"]))
                if poloniex_json[self.key]["lowestAsk"] is None:
                    ask = "Ask : Unknow\n"
                else:
                    ask = "Ask : {}\n".format(float(poloniex_json[self.key]["lowestAsk"]))
                if poloniex_json[self.key]["quoteVolume"] is None:
                    volume = "Volume : Unknown\n"
                else:
                    volume = "Volume : {} BTC\n".format(float(poloniex_json[self.key]["quoteVolume"]))
                if poloniex_json[self.key]["high24hr"] is None:
                    high = "1d High : Unknown\n"
                else:
                    high = "1d High : {}\n".format(poloniex_json[self.key]["high24hr"])
                if poloniex_json[self.key]["low24hr"] is None:
                    low = "1d Low : Unknown\n"
                else:
                    low = "1d Low : {}\n".format(poloniex_json[self.key]["low24hr"])
                value_polo = "```css\n" + pair + volume + last + bid + ask + high + low + "```"
            else:
                pair = "Pair : " + self.key.replace("_", "-") + "\n"
                if poloniex_json[self.key]["last"] is None:
                    last = "Last : Unknown\n"
                else:
                    last = "Last : {}\n".format(float(poloniex_json[self.key]["last"]))
                if poloniex_json[self.key]["highestBid"] is None:
                    bid = "Bid : Unknown\n"
                else:
                    bid = "Bid : {}\n".format(float(poloniex_json[self.key]["highestBid"]))

                if poloniex_json[self.key]["lowestAsk"] is None:
                    ask = "Ask : Unknown\n"
                else:
                    ask = "Ask : {}\n".format(float(poloniex_json[self.key]["lowestAsk"]))
                if poloniex_json[self.key]["quoteVolume"] is None:
                    volume = "Volume : Unknown\n"
                else:
                    volume = "Volume : {} BTC\n".format(poloniex_json[self.key]["quoteVolume"])
                if poloniex_json[self.key]["high24hr"] is None:
                    high = "1d High : Unknown\n"
                else:
                    high = "1d High : {}\n".format(poloniex_json[self.key]["high24hr"])
                if poloniex_json[self.key]["low24hr"] is None:
                    low = "1d Low : Unknown\n"
                else:
                    low = "1d Low : {}\n".format(float(poloniex_json[self.key]["low24hr"]))
                value_polo = "```css\n" + pair + volume + last + bid + ask + high + low + "\n```"
        except KeyError:
            value_polo = "```css\n{} is not listed on Poloniex.\n```".format(self.name)

        return value_polo

    def function_display_ok(self, value_mc, value_polo):
        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.add_field(name=":medal: CoinMarketCap Informations", value=value_mc, inline=True)
        embed.add_field(name=":crystal_ball: Poloniex Informations", value=value_polo, inline=False)
        embed.set_footer(text="Request achieved :")
        return embed

    def function_display_err(self, cmc_value):
        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.add_field(name=":medal: CoinMarketCap Informations", value=cmc_value, inline=False)
        embed.set_footer(text="Request achieved :")

        return embed

    async def poloniex(self, coin):
        tickers = self.function_cmc(coin)
        if tickers == "```css\nThis ticker does not exist on Coinmarketcap.\nMaybe you made a typo in the coin's ticker.```":
            embed = self.function_display_err(tickers)
        else:
            values = self.function_poloniex(coin)
            embed = self.function_display_ok(tickers, values)
        return embed

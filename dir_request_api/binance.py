from pymarketcap import Pymarketcap
import datetime
import discord
from random import randint
import requests


class Class_Binance:
    def __init__(self, auth):
        self.auth = str(auth).split("#")
        self.auth = self.auth[0]
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        self.name = "None"
        self.default_ticker = "BTC"
        self.default_print = "Default Print"
        self.binance_api_url_btc = "https://www.binance.com/api/v1/ticker/24hr?symbol={}BTC"
        self.binance_api_url_usdt = "https://www.binance.com/api/v1/ticker/24hr?symbol={}USDT"
        self.default_cmc = "btc"
        return

    def function_cmc(self, coin):
        coin = coin.upper()
        coinmarketcap = Pymarketcap(timeout=10)
        cmc_json = coinmarketcap.ticker(coin, convert="EUR")
        rank = str("Rank : [Rank " + str(cmc_json["rank"]) + "]\n")
        marketcap = str("MC : " + "$" + "{:,}".format(float(cmc_json["market_cap_usd"])) + "\n")
        price = str("Price : " + "$" + "{0:.3f}".format(float(cmc_json["price_usd"])) + " | " + "{0:.3f}".format(
            float(cmc_json["price_eur"])) + "€      \n")
        change_1 = str("1h Swing : " + str(cmc_json["percent_change_1h"]) + "%\n")
        change_24 = str("24h Swing : " + str(cmc_json["percent_change_24h"]) + "%\n")
        change_7 = str("7 days Swing : " + str(cmc_json["percent_change_7d"]) + "%\n")
        value_mc = "```css\n" + rank + marketcap + price + change_1 + change_24 + change_7 + "```"
        self.name = cmc_json["name"]

        return value_mc

    def function_binance(self, coin):
        coin = coin.upper()
        if coin == "BTC":
            api_url = self.binance_api_url_usdt.format(coin)
        else:
            api_url = self.binance_api_url_btc.format(coin)

        r = requests.get(api_url)
        binance_json = r.json()

        if "msg" not in binance_json:
            if coin == "BTC":
                pair = "Pair : USDT-" + coin + "\n"
                if binance_json["lastPrice"] is None:
                    last = "Last : Unknown\n"
                else:
                    last = "Last : {}\n".format(float(binance_json["lastPrice"]))
                if binance_json["bidPrice"] is None:
                    bid = "Bid : Unknown\n"
                else:
                    bid = "Bid : {}\n".format(float(binance_json["bidPrice"]))
                if binance_json["askPrice"] is None:
                    ask = "Ask : Unknown\n"
                else:
                    ask = "Ask : {}\n".format(float(binance_json["askPrice"]))
                if binance_json["volume"] is None:
                    volume = "Volume : Unknown\n"
                else:
                    volume = "Volume : {} BTC\n".format(float(binance_json["volume"]))
                if binance_json["highPrice"] is None:
                    high = "1d High : Unknown\n"
                else:
                    high = "1d High : {}\n".format(float(binance_json["highPrice"]))
                if binance_json["lowPrice"] is None:
                    low = "1d Low : Unknown\n"
                else:
                    low = "1d Low : {}\n".format(float(binance_json["lowPrice"]))
                value_bin = "```css\n" + pair + volume + last + bid + ask + high + low + "```"
            else:
                pair = "Pair : BTC-" + coin + "\n"
                if binance_json["lastPrice"] is None:
                    last = "Last : Unknown\n"
                else:
                    last = "Last : {}\n".format(float(binance_json["lastPrice"]))
                if binance_json["bidPrice"] is None:
                    bid = "Bid : Unknown\n"
                else:
                    bid = "Bid : {}\n".format(float(binance_json["bidPrice"]))
                if binance_json["askPrice"] is None:
                    ask = "Ask : Unknown\n"
                else:
                    ask = "Ask : {}\n".format(float(binance_json["askPrice"]))
                if binance_json["volume"] is None:
                    volume = "Volume : Unknown\n"
                else:
                    volume = "Volume : {} BTC\n".format(float(binance_json["volume"]))
                if binance_json["highPrice"] is None:
                    high = "1d High : Unknown\n"
                else:
                    high = "1d High : {}\n".format(float(binance_json["highPrice"]))
                if binance_json["lowPrice"] is None:
                    low = "1d Low : Unknown\n"
                else:
                    low = "1d Low : {}\n".format(float(binance_json["lowPrice"]))
                value_bin = "```css\n" + pair + volume + last + bid + ask + high + low + "```"
        else:
            value_bin = "```css\n{} is not listed on Binance. ```".format(self.name)

        return value_bin

    def function_display(self, value_mc, value_bin):
        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.add_field(name=":medal: CoinMarketCap Informations", value=value_mc, inline=True)
        embed.add_field(name=":game_die: Binance Informations", value=value_bin, inline=False)
        embed.set_footer(text="Request achieved :")
        return embed

    async def binance(self, coin):
        tickers = self.function_cmc(coin)
        values = self.function_binance(coin)
        embed = self.function_display(tickers, values)
        return embed

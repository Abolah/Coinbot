from pymarketcap import Pymarketcap
import datetime
import discord
from random import randint
import requests


class Class_Bittrex:
    def __init__(self, auth):
        self.auth = str(auth).split("#")
        self.auth = self.auth[0]
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        self.name = "None"
        self.default_ticker = "BTC"
        self.default_print = "Default Print"
        self.bittrex_api_url_btc = "https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-{}"
        self.bittrex_api_url_usdt = "https://bittrex.com/api/v1.1/public/getmarketsummary?market=usdt-{}"
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

    def function_bittrex(self, coin):
        if coin == "btc":
            api_url = self.bittrex_api_url_usdt.format(coin)
        else:
            api_url = self.bittrex_api_url_btc.format(coin)
        r = requests.get(api_url)
        bittrex_json = r.json()

        if "INVALID_MARKET" not in bittrex_json["message"]:
            if coin == "btc":
                pair = "Pair : USDT-" + coin.upper() + "\n"
                if bittrex_json["result"][0]["Volume"] is None:
                    volume = "Volume : Unknown\n"
                else:
                    volume = "Volume : {} BTC\n".format(bittrex_json["result"][0]["Volume"])
                if bittrex_json["result"][0]["Last"] is None:
                    last = "Last : Unknown\n"
                else:
                    last = "Last : {}\n".format(bittrex_json["result"][0]["Last"])
                if bittrex_json["result"][0]["Bid"] is None:
                    bid = "Bid : Unknown\n"
                else:
                    bid = "Bid : {}\n".format(bittrex_json["result"][0]["Bid"])
                if bittrex_json["result"][0]["Ask"] is None:
                    ask = "Ask : Unknown\n"
                else:
                    ask = "Ask : {}\n".format(bittrex_json["result"][0]["Ask"])
                if bittrex_json["result"][0]["Low"] is None:
                    low = "1d Low : Unknown\n"
                else:
                    low = "1d Low : {}\n".format(bittrex_json["result"][0]["Low"])
                if bittrex_json["result"][0]["High"] is None:
                    high = "1d High : Unknown\n"
                else:
                    high = "1d High : {}\n".format(bittrex_json["result"][0]["High"])
                value_rex = "```css\n" + pair + volume + last + bid + ask + high + low + "```"
            else:
                pair = "Pair : BTC-" + coin.upper() + "\n"
                if bittrex_json["result"][0]["Volume"] is None:
                    volume = "Volume : Unknown\n"
                else:
                    volume = "Volume : {} BTC\n".format(bittrex_json["result"][0]["Volume"])
                if bittrex_json["result"][0]["Last"] is None:
                    last = "Last : Unknown\n"
                else:
                    last = "Last : {}\n".format(bittrex_json["result"][0]["Last"])
                if bittrex_json["result"][0]["Bid"] is None:
                    bid = "Bid : Unknown\n"
                else:
                    bid = "Bid : {}\n".format(bittrex_json["result"][0]["Bid"])
                if bittrex_json["result"][0]["Ask"] is None:
                    ask = "Ask : Unknown\n"
                else:
                    ask = "Ask : {}\n".format(bittrex_json["result"][0]["Ask"])
                if bittrex_json["result"][0]["Low"] is None:
                    low = "1d Low : Unknown\n"
                else:
                    low = "1d Low : {}\n".format(bittrex_json["result"][0]["Low"])
                if bittrex_json["result"][0]["High"] is None:
                    high = "1d High : Unknown\n"
                else:
                    high = "1d High : {}\n".format(bittrex_json["result"][0]["High"])
                value_rex = "```css\n" + pair + volume + last + bid + ask + high + low + "```"
        else:
            value_rex = "```css\n{} is not listed on Bittrex. ```".format(self.name)

        return value_rex

    def function_display_ok(self, value_mc, value_rex):
        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.add_field(name=":medal: CoinMarketCap Informations", value=value_mc, inline=True)
        embed.add_field(name=":dragon: Bittrex Informations", value=value_rex, inline=False)
        embed.set_footer(text="Request achieved :")
        return embed

    def function_display_err(self, cmc_value):
        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.add_field(name=":medal: CoinMarketCap Informations", value=cmc_value, inline=False)
        embed.set_footer(text="Request achieved :")

        return embed

    async def bittrex(self, coin):
        tickers = self.function_cmc(coin)
        if tickers == "```css\nThis ticker does not exist on Coinmarketcap.\nMaybe you made a typo in the coin's ticker.```":
            embed = self.function_display_err(tickers)
        else:
            values = self.function_bittrex(coin)
            embed = self.function_display_ok(tickers, values)
        return embed

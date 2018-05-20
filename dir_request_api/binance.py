from pymarketcap import Pymarketcap
import datetime
import discord
from random import randint
import requests
from dir_request_api import all


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

    def function_binance(self, coin):
        coin = coin.upper()
        if coin == "MIOTA":
            coin = "IOTA"
            api_url = self.binance_api_url_btc.format(coin)
        elif coin == "BTC":
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
                    last = "Last : {:,.0f}\n".format(float(binance_json["lastPrice"]))
                if binance_json["bidPrice"] is None:
                    bid = "Bid : Unknown\n"
                else:
                    bid = "Bid : {:,.0f}\n".format(float(binance_json["bidPrice"]))
                if binance_json["askPrice"] is None:
                    ask = "Ask : Unknown\n"
                else:
                    ask = "Ask : {:,.0f}\n".format(float(binance_json["askPrice"]))
                if binance_json["volume"] is None:
                    volume = "Volume : Unknown\n"
                else:
                    volume = "Volume : {:,.2f} BTC\n".format(float(binance_json["quoteVolume"]))
                if binance_json["highPrice"] is None:
                    high = "1d High : Unknown\n"
                else:
                    high = "1d High : {:,.0f}\n".format(float(binance_json["highPrice"]))
                if binance_json["lowPrice"] is None:
                    low = "1d Low : Unknown\n"
                else:
                    low = "1d Low : {:,.0f}\n".format(float(binance_json["lowPrice"]))
                value_bin = "```css\n" + pair + volume + last + bid + ask + high + low + "```"
            else:
                pair = "Pair : BTC-" + coin + "\n"
                if binance_json["lastPrice"] is None:
                    last = "Last : Unknown\n"
                else:
                    last = "Last : {:,.0f} sats\n".format(float(binance_json["lastPrice"]) / 0.00000001)
                if binance_json["bidPrice"] is None:
                    bid = "Bid : Unknown\n"
                else:
                    bid = "Bid : {:,.0f} sats\n".format(float(binance_json["bidPrice"]) / 0.00000001)
                if binance_json["askPrice"] is None:
                    ask = "Ask : Unknown\n"
                else:
                    ask = "Ask : {:,.0f} sats\n".format(float(binance_json["askPrice"]) / 0.00000001)
                if binance_json["volume"] is None:
                    volume = "Volume : Unknown\n"
                else:
                    volume = "Volume : {:,.2f} BTC\n".format(float(binance_json["quoteVolume"]))
                if binance_json["highPrice"] is None:
                    high = "1d High : Unknown\n"
                else:
                    high = "1d High : {:,.0f} sats\n".format(float(binance_json["highPrice"]) / 0.00000001)
                if binance_json["lowPrice"] is None:
                    low = "1d Low : Unknown\n"
                else:
                    low = "1d Low : {:,.0f} sats\n".format(float(binance_json["lowPrice"]) / 0.00000001)
                value_bin = "```css\n" + pair + volume + last + bid + ask + high + low + "```"
        else:
            value_bin = "```css\n{} is not listed on Binance. ```".format(self.name)

        return value_bin

    def function_display_ok(self, value_mc, value_bin):
        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.add_field(name=":medal: CoinMarketCap Informations", value=value_mc, inline=True)
        embed.add_field(name=":game_die: Binance Informations", value=value_bin, inline=False)
        embed.set_footer(text="Request achieved :")
        return embed

    def function_display_err(self, cmc_value):
        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.add_field(name=":medal: CoinMarketCap Informations", value=cmc_value, inline=False)
        embed.set_footer(text="Request achieved :")

        return embed

    async def binance(self, coin):
        tickers = self.function_cmc(coin)
        if tickers == "```css\nThis ticker does not exist on Coinmarketcap.\nMaybe you made a typo in the coin's ticker.```":
            embed = self.function_display_err(tickers)
        else:
            values = self.function_binance(coin)
            embed = self.function_display_ok(tickers, values)
        return embed

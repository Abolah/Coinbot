from pymarketcap import Pymarketcap
import datetime
import discord
from random import randint
import requests


class Class_Bitfinex:
    def __init__(self, auth):
        self.auth = str(auth).split("#")
        self.auth = self.auth[0]
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        self.name = "None"
        self.default_ticker = "BTC"
        self.default_print = "Default Print"
        self.bitfinex_api_url_btc = "https://api.bitfinex.com/v1/pubticker/{}btc"
        self.bitfinex_api_url_usdt = "https://api.bitfinex.com/v1/pubticker/btcusd"
        self.bitfinex_url_status = "https://api.bitfinex.com/v2/platform/status"
        return

    def function_cmc(self, coin):
        coin = coin.upper()
        coinmarketcap = Pymarketcap(timeout=10)
        try:
            cmc_json = coinmarketcap.ticker(coin, convert="EUR")
            self.name = cmc_json["name"]
            rank = str("Rank : [Rank " + str(cmc_json["rank"]) + "]\n")
            if cmc_json["market_cap_usd"] is None:
                marketcap = "MarketCap : Unknown\n"
            else:
                marketcap = str("MC : " + "$" + "{:,}".format(float(cmc_json["market_cap_usd"])) + "\n")

            price = str("Price : ${0:.3f}".format(float(cmc_json["price_usd"])) + " | {0:.3f}€\n".format(
                float(cmc_json["price_eur"])))
            if cmc_json["percent_change_1h"] is None:
                change_1 = "1h Swing : Unknown\n"
            else:
                change_1 = str("1h Swing : " + str(cmc_json["percent_change_1h"]) + "%\n")
            if cmc_json["percent_change_24h"] is None:
                change_24 = "24h Swing : Unknown\n"
            else:
                change_24 = str("24h Swing : " + str(cmc_json["percent_change_24h"]) + "%\n")
            if cmc_json["percent_change_7d"] is None:
                change_7 = "7 days Swing : Unknown\n"
            else:
                change_7 = str("7 days Swing : " + str(cmc_json["percent_change_7d"]) + "%\n")
            value_mc = "```css\n" + rank + marketcap + price + change_1 + change_24 + change_7 + "```"
        except KeyError:
            value_mc = "```css\nThis ticker does not exist on Coinmarketcap.\nMaybe you made a typo in the coin's ticker.```"

        return value_mc

    def function_bitfinex(self, coin):
        if coin == "iota" or coin == "miota":
            coin = "iot"
            api_url = self.bitfinex_api_url_btc.format(coin)
        elif coin == "btc":
            api_url = self.bitfinex_api_url_usdt
        else:
            api_url = self.bitfinex_api_url_btc.format(coin)
        r = requests.get(api_url)
        bitfinex_json = r.json()

        if "message" not in bitfinex_json:
            if coin == "btc":
                pair = "Pair : USDT-" + coin.upper() + "\n"
                if bitfinex_json["last_price"] is None:
                    last = "Last : Unknown\n"
                else:
                    last = "Last : {}\n".format(float(bitfinex_json["last_price"]))
                if bitfinex_json["bid"] is None:
                    bid = "Bid : Unknown\n"
                else:
                    bid = "Bid : {}\n".format(float(bitfinex_json["bid"]))
                if bitfinex_json["ask"] is None:
                    ask = "Ask : Unknown\n"
                else:
                    ask = "Ask : {}\n".format(float(bitfinex_json["ask"]))
                if bitfinex_json["volume"] is None:
                    volume = "Volume : Unknown\n"
                else:
                    volume = "Volume : {} BTC\n".format(float(bitfinex_json["volume"]))
                if bitfinex_json["high"] is None:
                    high = "1d High : Unknown\n"
                else:
                    high = "1d High : {}\n".format(float(bitfinex_json["high"]))
                if bitfinex_json["low"] is None:
                    low = "1d Low : Unknown\n"
                else:
                    low = "1d Low : {}\n".format(float(bitfinex_json["low"]))
                value_finex = "```css\n" + pair + volume + last + bid + ask + high + low + "```"
            else:
                pair = "Pair : BTC-" + coin.upper() + "\n"
                if bitfinex_json["last_price"] is None:
                    last = "Last : Unknown\n"
                else:
                    last = "Last : {}\n".format(float(bitfinex_json["last_price"]))
                if bitfinex_json["bid"] is None:
                    bid = "Bid : Unknown\n"
                else:
                    bid = "Bid : {}\n".format(float(bitfinex_json["bid"]))
                if bitfinex_json["ask"] is None:
                    ask = "Ask : Unknown\n"
                else:
                    ask = "Ask : {}\n".format(float(bitfinex_json["ask"]))
                if bitfinex_json["volume"] is None:
                    volume = "Volume : Unknown\n"
                else:
                    volume = "Volume : {} BTC\n".format(float(bitfinex_json["volume"]))
                if bitfinex_json["high"] is None:
                    high = "1d High : Unknown\n"
                else:
                    high = "1d High : {}\n".format(float(bitfinex_json["high"]))
                if bitfinex_json["low"] is None:
                    low = "1d Low : Unknown\n"
                else:
                    low = "1d Low : {}\n".format(float(bitfinex_json["low"]))
                value_finex = "```css\n" + pair + volume + last + bid + ask + high + low + "```"
        else:
            value_finex = "```css\n{} is not listed on Bitfinex.\n```".format(self.name)

        return value_finex

    def function_display_ok(self, value_mc, value_finex):
        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.add_field(name=":medal: CoinMarketCap Informations", value=value_mc, inline=True)
        embed.add_field(name=":fleur_de_lis: Bitfinex Informations", value=value_finex, inline=False)
        embed.set_footer(text="Request achieved :")
        return embed

    def function_display_err(self, cmc_value):
        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.add_field(name=":medal: CoinMarketCap Informations", value=cmc_value, inline=False)
        embed.set_footer(text="Request achieved :")

        return embed

    async def bitfinex(self, coin):
        tickers = self.function_cmc(coin)
        if tickers == "```css\nThis ticker does not exist on Coinmarketcap.\nMaybe you made a typo in the coin's ticker.```":
            embed = self.function_display_err(tickers)
        else:
            values = self.function_bitfinex(coin)
            embed = self.function_display_ok(tickers, values)
        return embed

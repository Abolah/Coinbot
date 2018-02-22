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
        return

    def function_cmc(self, coin):
        global cmc_json, ticker
        coin = coin.upper()
        coinmarketcap = Pymarketcap()
        cmc_json = coinmarketcap.ticker(coin, convert="EUR")

        marketcap = str("MC : " + "$" + "{:,}".format(float(cmc_json["market_cap_usd"])) + "\n")
        price = str("Price : " + "$" + "{0:.3f}".format(float(cmc_json["price_usd"])) + " | " + "{0:.3f}".format(float(cmc_json["price_eur"])) + "€      \n")
        rank = str("Rank : [Rank " + str(cmc_json["rank"]) + "]\n")
        change_1 = str("1h Swing : " + str(cmc_json["percent_change_1h"]) + "%\n")
        change_24 = str("24h Swing : " + str(cmc_json["percent_change_24h"]) + "%\n")
        change_7 = str("7 days Swing : " + str(cmc_json["percent_change_7d"]) + "%\n")
        value_mc = "```css\n" + rank + marketcap + price + change_1 + change_24 + change_7 + "```"

        self.name = cmc_json["name"]
        return value_mc

    def function_bitfinex(self, coin):
        global bitfinex_json, value_annex
        if coin == "btc":
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

    def function_display(self, value_mc, value_finex):
        name_logo = self.name.replace(" ", "-").lower()
        url_logo = "https://files.coinmarketcap.com/static/img/coins/32x32/" + name_logo + ".png"

        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.set_thumbnail(url=url_logo)
        embed.set_footer(text="Request achieved :")
        embed.add_field(name=":star2: Request about " + self.name,
                        value="Here are the informations I could retrieve " + self.auth, inline=False)
        embed.add_field(name=":medal: CoinMarketCap Informations", value=value_mc, inline=True)
        embed.add_field(name=":fleur_de_lis: Bitfinex Informations", value=value_finex, inline=False)
        return embed

    async def bitfinex(self, coin):
        tickers = self.function_cmc(coin)
        values = self.function_bitfinex(coin)
        embed = self.function_display(tickers, values)
        return embed

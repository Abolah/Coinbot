from pymarketcap import Pymarketcap
import datetime
import discord
from random import randint
import requests


class Class_HitBTC:
    def __init__(self, auth):
        self.auth = str(auth).split("#")
        self.auth = self.auth[0]
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        self.name = "None"
        self.default_ticker = "BTC"
        self.default_print = "Default Print"
        self.hitbtc_api_url_btc = "https://api.hitbtc.com/api/2/public/ticker/{}BTC"
        self.hitbtc_api_url_usd = "https://api.hitbtc.com/api/2/public/ticker/{}USD"
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

    def function_hitbtc(self, coin):
        coin = coin.upper()
        if coin == "MIOTA":
            coin = "IOTA"
            api_url = self.hitbtc_api_url_btc.format(coin)
        elif coin == "BTC":
            api_url = self.hitbtc_api_url_usdt.format(coin)
        else:
            api_url = self.hitbtc_api_url_btc.format(coin)
        r = requests.get(api_url)
        hitbtc_json = r.json()

        if "error" not in hitbtc_json:
            if coin == "BTC":
                pair = "Pair : USD-" + coin + "\n"
                if hitbtc_json["last"] is None:
                    last = "Last : Unknown\n"
                else:
                    last = "Last : {:,.0f}\n".format(float(hitbtc_json["last"]))
                if hitbtc_json["bid"] is None:
                    bid = "Bid : Unknown\n"
                else:
                    bid = "Bid : {:,.0f}\n".format(float(hitbtc_json["bid"]))
                if hitbtc_json["ask"] is None:
                    ask = "Ask : Unknown\n"
                else:
                    ask = "Ask : {:,}\n".format(float(hitbtc_json["ask"]))
                if hitbtc_json["volumeQuote"] is None:
                    volume = "Volume : Unknown\n"
                else:
                    volume = "Volume : {:,.2f} BTC\n".format(float(hitbtc_json["volumeQuote"]))
                if hitbtc_json["high"] is None:
                    high = "1 High : Unknown\n"
                else:
                    high = "1d High : {:,.0f}\n".format(float(hitbtc_json["high"]))
                if hitbtc_json["low"] is None:
                    low = "1d Low : Unknown\n"
                else:
                    low = "1d Low : {:,.0f}\n".format(float(hitbtc_json["low"]))
                value_hitbtc = "```css\n" + pair + volume + last + bid + ask + high + low + "```"
            else:
                pair = "Pair : BTC-" + coin + "\n"
                if hitbtc_json["last"] is None:
                    last = "Last : Unknown\n"
                else:
                    last = "Last : {:,.0f} sats\n".format(float(hitbtc_json["last"]) / 0.00000001)
                if hitbtc_json["bid"] is None:
                    bid = "Bid : Unknown\n"
                else:
                    bid = "Bid : {:,.0f} sats\n".format(float(hitbtc_json["bid"]) / 0.00000001)
                if hitbtc_json["ask"] is None:
                    ask = "Ask : Unknown\n"
                else:
                    ask = "Ask : {:,.0f} sats\n".format(float(hitbtc_json["ask"]) / 0.00000001)
                if hitbtc_json["volumeQuote"] is None:
                    volume = "Volume : Unknown\n"
                else:
                    volume = "Volume : {:,.2f} BTC\n".format(float(hitbtc_json["volumeQuote"]))
                if hitbtc_json["high"] is None:
                    high = "1 High : Unknown\n"
                else:
                    high = "1d High : {:,.0f} sats\n".format(float(hitbtc_json["high"]) / 0.00000001)
                if hitbtc_json["low"] is None:
                    low = "1d Low : Unknown\n"
                else:
                    low = "1d Low : {:,.0f} sats\n".format(float(hitbtc_json["low"]) / 0.00000001)
                value_hitbtc = "```css\n" + pair + volume + last + bid + ask + high + low + "```"
        else:
            value_hitbtc = "```css\n{} is not listed on HitBTC.\n```".format(self.name)
        return value_hitbtc

    def function_display_ok(self, value_mc, value_hitbtc):
        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.add_field(name=":medal: CoinMarketCap Informations", value=value_mc, inline=True)
        embed.add_field(name=":octopus: HitBTC Informations", value=value_hitbtc, inline=False)
        embed.set_footer(text="Request achieved :")
        return embed

    def function_display_err(self, cmc_value):
        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.add_field(name=":medal: CoinMarketCap Informations", value=cmc_value, inline=False)
        embed.set_footer(text="Request achieved :")

        return embed

    async def hitbtc(self, coin):
        tickers = self.function_cmc(coin)
        if tickers == "```css\nThis ticker does not exist on Coinmarketcap.\nMaybe you made a typo in the coin's ticker.```":
            embed = self.function_display_err(tickers)
        else:
            values = self.function_hitbtc(coin)
            embed = self.function_display_ok(tickers, values)
        return embed

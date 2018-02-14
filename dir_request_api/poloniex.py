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
        global cmc_json, ticker
        coin = coin.upper()
        coinmarketcap = Pymarketcap()
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

        if coin == "BTC":

            pair = "Pair : " + self.key.replace("_", "-") + "\n"
            last = "Last : " + "{0:.2f}".format(float(poloniex_json[self.key]["last"])) + "\n"
            bid = "Bid : " + "{0:.2f}".format(float(poloniex_json[self.key]["highestBid"])) + "\n"
            ask = "Ask : " + "{0:.2f}".format(float(poloniex_json[self.key]["lowestAsk"])) + "\n"
            volume = "Volume : " + "{0:.2f}".format(float(poloniex_json[self.key]["baseVolume"])) + " BTC" + "\n"
            high = "1d High : " + poloniex_json[self.key]["high24hr"] + "\n"
            low = "1d Low : " + poloniex_json[self.key]["low24hr"] + "\n"
            value_polo = "```css\n" + pair + volume + last + bid + ask + high + low + "```"
        else:
            pair = "Pair : " + self.key.replace("_", "-") + "\n"
            last = "Last : " + poloniex_json[self.key]["last"] + "\n"
            bid = "Bid : " + poloniex_json[self.key]["highestBid"] + "\n"
            ask = "Ask : " + poloniex_json[self.key]["lowestAsk"] + "\n"
            volume = "Volume : " + "{0:.2f}".format(float(poloniex_json[self.key]["baseVolume"])) + " BTC" + "\n"
            high = "1d High : " + poloniex_json[self.key]["high24hr"] + "\n"
            low = "1d Low : " + poloniex_json[self.key]["low24hr"] + "\n"
            value_polo = "```css\n" + pair + volume + last + bid + ask + high + low + "```"

        return value_polo

    def function_display(self, value_mc, value_polo):
        name_logo = self.name.replace(" ", "-").lower()
        url_logo = "https://files.coinmarketcap.com/static/img/coins/32x32/" + name_logo + ".png"

        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.set_thumbnail(url=url_logo)
        embed.set_footer(text="Request achieved:")
        embed.add_field(name=":star2: Request about " + self.name,
                        value="Here are the informations I could retrieve " + self.auth, inline=False)
        embed.add_field(name=":medal: CoinMarketCap Informations", value=value_mc, inline=True)
        embed.add_field(name=":crystal_ball: Poloniex Informations", value=value_polo, inline=False)
        return embed

    async def poloniex(self, coin):
        tickers = self.function_cmc(coin)
        values = self.function_poloniex(coin)
        embed = self.function_display(tickers, values)
        return embed

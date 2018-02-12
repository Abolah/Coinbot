from pymarketcap import Pymarketcap
import datetime
import discord
from random import randint
import requests


class Class_Cryptopia:
    def __init__(self, auth):
        self.auth = str(auth).split("#")
        self.auth = self.auth[0]
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        self.name = "None"
        self.default_ticker = "BTC"
        self.default_print = "Default Print"
        self.cryptopia_api_url_btc = "https://www.cryptopia.co.nz/api/GetMarket/{}_BTC"
        self.cryptopia_api_url_usdt = "https://www.cryptopia.co.nz/api/GetMarket/{}_USDT"
        return

    def function_cmc(self, coin):
        global cmc_json, ticker
        coin = coin.upper()
        coinmarketcap = Pymarketcap()
        cmc_json = coinmarketcap.ticker(coin, convert="EUR")
        rank = str("Rank : [Rank " + str(cmc_json["rank"]) + "]\n")
        marketcap = str("MC : " + "$ " + "{:,}".format(float(cmc_json["market_cap_usd"])) + "\n")
        price = str("Price : " + "$" + "{0:.3f}".format(float(cmc_json["price_usd"])) + " | " + "{0:.3f}".format(
            float(cmc_json["price_eur"])) + "€      \n")
        change_1 = str("1h Swing : " + str(cmc_json["percent_change_1h"]) + "%\n")
        change_24 = str("24h Swing : " + str(cmc_json["percent_change_24h"]) + "%\n")
        change_7 = str("7 days Swing : " + str(cmc_json["percent_change_7d"]) + "%\n")
        value_mc = "```css\n" + rank + marketcap + price + change_1 + change_24 + change_7 + "```"

        self.name = cmc_json["name"]
        return value_mc

    def function_cryptopia(self, coin):
        coin = coin.upper()
        if coin == "BTC":
            api_url = self.cryptopia_api_url_usdt.format(coin)
        else:
            api_url = self.cryptopia_api_url_btc.format(coin)

        r = requests.get(api_url)
        topia_json = r.json()

        if coin == "BTC":
            pair = "Pair : BTC-" + coin + "\n"
            last = "Last : " + "{0:.2f}".format(topia_json["Data"]["LastPrice"]) + "\n"
            bid = "Bid : " + "{0:.2f}".format(topia_json["Data"]["BidPrice"]) + "\n"
            ask = "Ask : " + "{0:.2f}".format(topia_json["Data"]["AskPrice"]) + "\n"
            volume = "Volume : " + "{0:.2f}".format(topia_json["Data"]["BaseVolume"]) + " BTC" + "\n"
            high = "24 High : " + "{0:.8f}".format(topia_json["Data"]["High"]) + "\n"
            low = "24 Low : " + "{0:.8f}".format(topia_json["Data"]["Low"]) + "\n"
            value_topia = "```css\n" + pair + volume + last + bid + ask + high + low + "```"
        else:
            pair = "Pair : BTC-" + coin + "\n"
            last = "Last : " + "{0:.8f}".format(topia_json["Data"]["LastPrice"]) + "\n"
            bid = "Bid : " + "{0:.8f}".format(topia_json["Data"]["BidPrice"]) + "\n"
            ask = "Ask : " + "{0:.8f}".format(topia_json["Data"]["AskPrice"]) + "\n"
            volume = "Volume : " + "{0:.2f}".format(topia_json["Data"]["BaseVolume"]) + " BTC" + "\n"
            high = "24 High : " + "{0:.8f}".format(topia_json["Data"]["High"]) + "\n"
            low = "24 Low : " + "{0:.8f}".format(topia_json["Data"]["Low"]) + "\n"
            value_topia = "```css\n" + pair + volume + last + bid + ask + high + low + "```"

        return value_topia

    def function_display(self, value_mc, value_topia):
        name_logo = self.name.replace(" ", "-").lower()
        url_logo = "https://files.coinmarketcap.com/static/img/coins/32x32/" + name_logo + ".png"

        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.set_thumbnail(url=url_logo)
        embed.set_footer(text="Request achieved:")
        embed.add_field(name=":star2: Request about " + self.name,
                        value="Here are the informations I could retrieve " + self.auth, inline=False)
        embed.add_field(name=":medal: CoinMarketCap Informations", value=value_mc, inline=True)
        embed.add_field(name=":space_invader: Cryptopia Informations", value=value_topia, inline=False)
        return embed

    async def cryptopia(self, coin):
        tickers = self.function_cmc(coin)
        values = self.function_cryptopia(coin)
        embed = self.function_display(tickers, values)
        return embed

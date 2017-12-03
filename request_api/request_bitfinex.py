import aiohttp
import async_timeout
import asyncio
import datetime
import discord
from random import randint
import time
class Bitfinex():
    def __init__(self,arg,auth):
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        self.coin = arg
        if self.coin.upper() == "BTC":
            self.pair = self.coin.lower() + "usd"
        else:
            self.pair = self.coin.lower() + "btc"
        self.long_name = "None"
        self.idcoin = "None"
        self.generalcmc = "None"
        self.auth = str(auth).split("#")
        self.auth = self.auth[0]
        return

    async def general_cmc(self):
        try:
            async with aiohttp.ClientSession() as session:
                    async with async_timeout.timeout(5):
                        async with session.get("https://api.coinmarketcap.com/v1/ticker/?limit=1000") as resp:
                            if resp.status == 200:
                                self.generalcmc = await resp.json()
        except asyncio.TimeoutError as e:
            self.generalcmc = "Timeout Error"
            print(e)
        except Exception as e:
            print(e)
            return -1
        try:
            for i in self.generalcmc:
                if i["symbol"] == self.coin.upper():
                    self.long_name = i["name"]
                    self.idcoin = i["id"]
                    break
        except Exception as e:
            print(e)
            return -1
        return 0

    async def fetch(self):
        list_json = []
        list_name = ["Bitfinex","Coinmarketcap"]
        list_urls = ["https://api.bitfinex.com/v1/pubticker/" + self.pair ,"https://api.coinmarketcap.com/v1/ticker/" + self.idcoin + "/?convert=EUR"]
        for i,name in zip(list_urls,list_name):
            try:
                async with aiohttp.ClientSession() as session:
                        async with async_timeout.timeout(5):
                            async with session.get(i) as resp:
                                if resp.status == 200:
                                    time.sleep(0.01)
                                    list_json.append([await resp.json(),name])
            except asyncio.TimeoutError as e:
                print(e)
                list_json.append([e,name])
                return  list_json
            except Exception as e:
                print(e)
                return 0
        return list_json


    def affichage(self,list_json):
        finex_json = {}
        cmc_json = {}
        for i in list_json:
            if i[1] == "Bitfinex":
                finex_json = i[0]
            if i [1] == "Coinmarketcap":
                cmc_json = i[0]
        try:
            name_logo = self.long_name.replace(" ","-").lower()
            url_logo = "https://files.coinmarketcap.com/static/img/coins/32x32/"+ name_logo + ".png"
        except Exception as e:
            print("err url",e)
            url_logo = ""

        try:
            if self.coin.upper() == "BTC":
                pair = "Pair : USDT-" + self.coin.upper() + "\n"
                last = "Last : " + "{0:.2f}".format(float(finex_json["last_price"])) + "\n"
                bid = "Bid : " + "{0:.2f}".format(float(finex_json["bid"])) + "\n"
                ask = "Ask : " + "{0:.2f}".format(float(finex_json["ask"])) + "\n"
                volume = "Volume : " + "{0:.2f}".format(float(finex_json["volume"])) + "\n"
                value_finex = "```css\n" + pair + volume + last + bid + ask + "```"
            else:
                pair = "Pair : BTC-" + self.coin.upper() + "\n"
                last = "Last : " + "{0:.8f}".format(float(finex_json["last_price"])) + "\n"
                bid = "Bid : " + "{0:.8f}".format(float(finex_json["bid"])) + "\n"
                ask = "Ask : " + "{0:.8f}".format(float(finex_json["ask"])) + "\n"
                volume = "Volume : " + "{0:.2f}".format(float(finex_json["volume"])) + "\n"
                value_finex = "```css\n" + pair + volume + last + bid + ask + "```"

        except Exception as e:
            print("err main_finex",e)
            value_finex = "```Erreur API Bitfinex```"

        try:
            high = "High : " + "{0:.8f}".format(float(finex_json["low"])) + "\n"
            low = "Low : " + "{0:.8f}".format(float(finex_json["high"])) + "\n"
            value_annex = "```css\n" + low + high +  "```"
        except Exception as e:
            print("err annex_finex",e)
            value_annex = "```Error API Bitfinex```"

        try:
            try:
                marketcap = "MC : " + "{:,}".format(float(cmc_json[0]["market_cap_usd"])) + "$\n"
            except Exception as e:
                marketcap = "MC : Unknown\n"
                print("mc err", e)
            price = "Price : " + "{0:.3f}".format(float(cmc_json[0]["price_usd"])) + "$ | " + "{0:.3f}".format(float(cmc_json[0]["price_eur"])) + "€\n"
            rank = "Rank : [Rank " + str(cmc_json[0]["rank"]) + "]\n"
            change_1 = "1h Swing : " + str(cmc_json[0]["percent_change_1h"]) + "%\n"
            change_24 = "24h Swing : " + str(cmc_json[0]["percent_change_24h"]) + "%\n"
            change_7 = "7 days Swing : " + str(cmc_json[0]["percent_change_7d"]) + "%\n"
            value_mc = "```css\n" + str(rank) + str(marketcap) + str(price) + str(change_1) + str(change_24) + str(change_7) + "```"
        except Exception as e:
            print("err cmc",e)
            value_mc = "```\nErreur formatage CMC```"

        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.set_thumbnail(url=url_logo)
        embed.set_footer(text="Request achieved on")
        embed.add_field(name=":star2: Request about " + self.long_name,
                        value="Here are the informations I could retrieve " + self.auth,
                        inline=False)
        embed.add_field(name=":fleur_de_lis: Bitfinex Informations", value=value_finex, inline=True)
        embed.add_field(name=":medal: CoinMarketCap Informations", value=value_mc, inline=True)
        embed.add_field(name=":information_source: Additional Informations", value=value_annex)
        return embed

    async def bitfinex_query(self):
        await self.general_cmc()
        data = await self.fetch()
        affichage = self.affichage(data)
        return affichage
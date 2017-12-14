import datetime
import discord
import aiohttp
import async_timeout
import asyncio
from random import randint
import time


class bittrex:
    def __init__(self, arg, auth):
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        self.coin = arg.upper()
        if self.coin.upper() == "BCH":
            self.coin = "bcc"
        if self.coin.upper() == "BTC":
            self.pair = "usdt-" + self.coin.lower()
        else:
            self.pair = "btc-" + self.coin.lower()
        self.long_name = "None"
        self.idcoin = "None"
        self.generalcmc = "None"
        self.auth = str(auth).split("#")
        self.auth = self.auth[0]
        return

    async def general_cmc(self):
        if self.coin.upper() == "BCC":
            tmp = "BCH"
        else:
            tmp = self.coin.upper()
        try:
            async with aiohttp.ClientSession() as session:
                async with async_timeout.timeout(10):
                    async with session.get("https://api.coinmarketcap.com/v1/ticker/?limit=1000") as resp:
                        if resp.status == 200:
                            self.generalcmc = await resp.json()
        except asyncio.TimeoutError as e:
            self.generalcmc = "Timeout Error"
            print("err", e)
        except Exception as e:
            print(e)
        try:
            for i in self.generalcmc:
                if i["symbol"] == tmp:
                    self.long_name = i["name"]
                    self.idcoin = i["id"]
                    break
        except Exception as e:
            print(e)
        return 0

    async def fetch(self):
        list_json = []
        list_name = ["Bittrex", "Coinmarketcap"]
        list_urls = ["https://bittrex.com/api/v1.1/public/getmarketsummary?market=" + self.pair,
                     "https://api.coinmarketcap.com/v1/ticker/" + self.idcoin + "/?convert=EUR"]
        for i, name in zip(list_urls, list_name):
            try:
                async with aiohttp.ClientSession() as session:
                    async with async_timeout.timeout(5):
                        async with session.get(i) as resp:
                            if resp.status == 200:
                                time.sleep(0.01)
                                list_json.append([await resp.json(), name])
            except asyncio.TimeoutError as e:
                list_json.append([e, name])
                print(e)
                return list_json
            except ConnectionResetError as e:
                print(e)
                return 0
        return list_json

    def affichage(self, list_json):
        rex_json = {}
        cmc_json = {}
        for i in list_json:
            if i[1] == "Bittrex":
                rex_json = i[0]
            if i[1] == "Coinmarketcap":
                cmc_json = i[0]
        # Try/Except sur l'API Logo CMC
        try:
            # A changer ici
            name_logo = self.long_name.replace(" ", "-").lower()
            url_logo = "https://files.coinmarketcap.com/static/img/coins/32x32/" + name_logo + ".png"
        except Exception as e:
            print("err url", e)
            url_logo = ""

        # Try/Except sur l'API Bittrex
        try:
            if self.coin == "BTC":
                name = "Pair :" + str(rex_json["result"][0]["MarketName"]) + "\n"
                volume = "Volume : " + "{0:.2f}".format(rex_json["result"][0]["BaseVolume"]) + " BTC" + "\n"
                last = "Last : " + "{0:.2f}".format(rex_json["result"][0]["Last"]) + "\n"
                bid = "Bid : " + "{0:.2f}".format(rex_json["result"][0]["Bid"]) + "\n"
                ask = "Ask : " + "{0:.2f}".format(rex_json["result"][0]["Ask"]) + "\n"
                low = "24h Low : " + "{0:.2f}".format(rex_json["result"][0]["Low"]) + "\n"
                high = "24h High : " + "{0:.2f}".format(rex_json["result"][0]["High"]) + "\n"
                prev = "PrevDay : " + "{0:.2f}".format(rex_json["result"][0]["PrevDay"]) + "\n"
                value_rex = "```css\n" + name + volume + last + bid + ask + "```"
                value_annex = "```css\n" + low + high + prev + "```"
            else:
                name = "Pair :" + str(rex_json["result"][0]["MarketName"]) + "\n"
                volume = "Volume : " + "{0:.2f}".format(rex_json["result"][0]["BaseVolume"]) + " BTC" + "\n"
                last = "Last : " + "{0:.8f}".format(rex_json["result"][0]["Last"]) + "\n"
                bid = "Bid : " + "{0:.8f}".format(rex_json["result"][0]["Bid"]) + "\n"
                ask = "Ask : " + "{0:.8f}".format(rex_json["result"][0]["Ask"]) + "\n"
                low = "24h Low : " + "{0:.8f}".format(rex_json["result"][0]["Low"]) + "\n"
                high = "24h High : " + "{0:.8f}".format(rex_json["result"][0]["High"]) + "\n"
                prev = "PrevDay : " + "{0:.8f}".format(rex_json["result"][0]["PrevDay"]) + "\n"
                value_rex = "```css\n" + name + volume + last + bid + ask + "```"
                value_annex = "```css\n" + low + high + prev + "```"
        except Exception as e:
            print("err main_rex", e)
            value_rex = "```\nError API Bittrex```"
            value_annex = "```Markdown\nError API Bittrex```"

        # Try/Except sur l'API CMC
        try:
            try:
                marketcap = "MC : " + "$ " + "{:,}".format(float(cmc_json[0]["market_cap_usd"])) + "\n"
            except Exception as e:
                marketcap = "MC : Unknown\n"
                print("mc err", e)
            price = "Price : " + "$ " + "{0:.3f}".format(float(cmc_json[0]["price_usd"])) + " | " + "{0:.3f}".format(float(cmc_json[0]["price_eur"])) + " €    \n"
            rank = "Rank : [Rank " + str(cmc_json[0]["rank"]) + "]\n"
            change_1 = "1h Swing : " + str(cmc_json[0]["percent_change_1h"]) + "%\n"
            change_24 = "24h Swing: " + str(cmc_json[0]["percent_change_24h"]) + "%\n"
            change_7 = "7 days Swing : " + str(cmc_json[0]["percent_change_7d"]) + "%\n"
            value_mc = "```css\n" + str(rank) + str(marketcap) + str(price) + str(change_1) + str(change_24) + str(
                change_7) + "```"
        except Exception as e:
            print("err cmc", e)
            value_mc = "```\nErreur formatage CMC```"

        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.set_thumbnail(url=url_logo)
        embed.set_footer(text="Request achieved on")
        embed.add_field(name=":star2: Request about " + str(self.long_name),
                        value="Here are the informations I could retrieve " + self.auth,
                        inline=False)
        embed.add_field(name=":dragon: Bittrex Information", value=value_rex, inline=True)
        embed.add_field(name=":medal: CoinMarketCap Information", value=value_mc, inline=True)
        embed.add_field(name=":information_source: Additional Informations", value=value_annex)

        return embed

    async def bittrex_query(self):
        await self.general_cmc()
        data = await self.fetch()
        affichage = self.affichage(data)
        return affichage

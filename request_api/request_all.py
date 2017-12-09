import datetime
from random import randint
import aiohttp
import async_timeout
import asyncio
import discord
import time


class all_currencies:
    def __init__(self, arg, auth):
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        self.coin = arg
        if self.coin.upper() == "BTC":
            self.pair_binance = self.coin + "USDT"
            self.pair_finex = self.coin.lower() + "usd"
            self.pair_rex = "usdt-" + self.coin.lower()
            self.pair_topia = self.coin + "_USDT"
            self.key = "USDT_BTC"
        else:
            self.pair_binance = self.coin + "BTC"
            self.pair_finex = self.coin.lower() + "btc"
            self.pair_rex = "btc-" + self.coin.lower()
            self.pair_topia = self.coin + "_BTC"
            self.key = "BTC_" + arg.upper()
        self.long_name = "None"
        self.idcoin = "None"
        self.generalcmc = "None"
        self.auth = str(auth).split("#")
        self.auth = self.auth[0]
        if self.coin == "bch":
            self.coin_rex = "bcc"
        else:
            self.coin_rex = self.coin
        return

    async def fetch(self):
        list_json = []
        list_name = ["Bitfinex", "Bittrex", "Cryptopia", "Poloniex", "Binance", "Coinmarketcap"]
        list_urls = ["https://api.bitfinex.com/v1/pubticker/" + self.pair_finex,
                     "https://bittrex.com/api/v1.1/public/getmarketsummary?market=" + self.pair_rex,
                     "https://www.cryptopia.co.nz/api/GetMarket/" + self.pair_topia,
                     "https://poloniex.com/public?command=returnTicker",
                     "https://www.binance.com/api/v1/ticker/24hr?symbol=" + self.pair_binance,
                     "https://api.coinmarketcap.com/v1/ticker/" + self.idcoin + "/?convert=EUR"]
        for i, name in zip(list_urls, list_name):
            try:
                async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
                    async with async_timeout.timeout(5):
                        async with session.get(i) as resp:
                            if resp.status == 200:
                                time.sleep(0.01)
                                list_json.append([await resp.json(), name])
            except asyncio.TimeoutError as e:
                list_json.append([e, name])
                print(e)
                return list_json
            except Exception as e:
                print(e)
                return 0
        return list_json

    async def general_cmc(self):
        try:
            async with aiohttp.ClientSession() as session:
                async with async_timeout.timeout(5):
                    async with session.get("https://api.coinmarketcap.com/v1/ticker/?limit=1000&convert=EUR") as resp:
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

    def affichage(self, list_json):
        finex_json = polo_json = bin_json = topia_json = rex_json = cmc_json = 0
        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.add_field(name=":star2: Request achieved about " + self.long_name,
                        value="Here are the informations I could retrieve " + self.auth,
                        inline=False)

        for i in list_json:
            if i[1] == "Bitfinex":
                finex_json = i[0]
            if i[1] == "Bittrex":
                rex_json = i[0]
            if i[1] == "Cryptopia":
                topia_json = i[0]
            if i[1] == "Poloniex":
                polo_json = i[0]
            if i[1] == "Binance":
                bin_json = i[0]
            if i[1] == "Coinmarketcap":
                cmc_json = i[0]

        try:
            name_logo = self.long_name.replace(" ", "-").lower()
            url_logo = "https://files.coinmarketcap.com/static/img/coins/32x32/" + name_logo + ".png"
        except Exception as e:
            print("err url", e)
            url_logo = ""
        try:
            try:
                marketcap = "MarketCap : " + "{:,}".format(float(cmc_json[0]["market_cap_usd"])) + "$\n"
            except Exception as e:
                marketcap = "MarketCap : Unknown\n"
                print("mc err", e)
            price = "Price : " + "{0:.3f}".format(float(cmc_json[0]["price_usd"])) + "$ | " + "{0:.3f}".format(
                float(cmc_json[0]["price_eur"])) + "€\n"
            rank = "Rank : [Rank " + str(cmc_json[0]["rank"]) + "]\n"
            change_1 = "1h Swing : " + str(cmc_json[0]["percent_change_1h"]) + "%\n"
            change_24 = "24h Swing : " + str(cmc_json[0]["percent_change_24h"]) + "%\n"
            change_7 = "Variation 7 jours : " + str(cmc_json[0]["percent_change_7d"]) + "%\n"
            value_mc = "```css\n" + str(rank) + str(marketcap) + str(price) + str(change_1) + str(change_24) + str(
                change_7) + "```"
            embed.add_field(name=":medal: CoinMarketCap Informations", value=value_mc, inline=False)
        except Exception as e:
            print("err cmc", e)

        try:
            if self.coin.upper() == "BTC":
                last = "Last : " + "{0:.2f}".format(float(finex_json["last_price"])) + "\n"
                bid = "Bid : " + "{0:.2f}".format(float(finex_json["bid"])) + "\n"
                ask = "Ask : " + "{0:.2f}".format(float(finex_json["ask"])) + "\n"
                volume = "Volume : " + "{0:.2f}".format(float(finex_json["volume"])) + "\n"
                value_finex = "```css\n" + volume + last + bid + ask + "```"
            else:
                last = "Last : " + "{0:.8f}".format(float(finex_json["last_price"])) + "\n"
                bid = "Bid : " + "{0:.8f}".format(float(finex_json["bid"])) + "\n"
                ask = "Ask : " + "{0:.8f}".format(float(finex_json["ask"])) + "\n"
                volume = "Volume : " + "{0:.2f}".format(float(finex_json["volume"])) + "\n"
                value_finex = "```css\n" + volume + last + bid + ask + "```"
            embed.add_field(name=":fleur_de_lis: Bitfinex Informations", value=value_finex, inline=True)
        except Exception as e:
            print("err main_finex", e)

        try:
            if self.coin.upper() == "BTC":
                volume = "Volume : " + "{0:.2f}".format(rex_json["result"][0]["BaseVolume"]) + "\n"
                last = "Last : " + "{0:.2f}".format(rex_json["result"][0]["Last"]) + "\n"
                bid = "Bid : " + "{0:.2f}".format(rex_json["result"][0]["Bid"]) + "\n"
                ask = "Ask : " + "{0:.2f}".format(rex_json["result"][0]["Ask"]) + "\n"
                value_rex = "```css\n" + volume + last + bid + ask + "```"
            else:
                volume = "Volume : " + "{0:.2f}".format(rex_json["result"][0]["BaseVolume"]) + "\n"
                last = "Last : " + "{0:.8f}".format(rex_json["result"][0]["Last"]) + "\n"
                bid = "Bid : " + "{0:.8f}".format(rex_json["result"][0]["Bid"]) + "\n"
                ask = "Ask : " + "{0:.8f}".format(rex_json["result"][0]["Ask"]) + "\n"
                value_rex = "```css\n" + volume + last + bid + ask + "```"
            embed.add_field(name=":dragon: Bittrex Informations", value=value_rex, inline=True)
        except Exception as e:
            print("err main_rex", e)

        try:
            if self.coin.upper() == "BTC":
                last = "Last : " + "{0:.2f}".format(topia_json["Data"]["LastPrice"]) + "\n"
                bid = "Bid : " + "{0:.2f}".format(topia_json["Data"]["BidPrice"]) + "\n"
                ask = "Ask : " + "{0:.2f}".format(topia_json["Data"]["AskPrice"]) + "\n"
                volume = "Volume : " + "{0:.2f}".format(topia_json["Data"]["BaseVolume"]) + "\n"
                value_topia = "```css\n" + volume + last + bid + ask + "```"
            else:
                last = "Last : " + "{0:.8f}".format(topia_json["Data"]["LastPrice"]) + "\n"
                bid = "Bid : " + "{0:.8f}".format(topia_json["Data"]["BidPrice"]) + "\n"
                ask = "Ask : " + "{0:.8f}".format(topia_json["Data"]["AskPrice"]) + "\n"
                volume = "Volume : " + "{0:.2f}".format(topia_json["Data"]["BaseVolume"]) + "\n"
                value_topia = "```css\n" + volume + last + bid + ask + "```"
            embed.add_field(name=":space_invader: Cryptopia Informations", value=value_topia, inline=True)
        except Exception as e:
            print("err main_cryptopia", e)

        try:
            if self.coin.upper() == "BTC":
                last = "Last : " + "{0:.2f}".format(float(polo_json[self.key]["last"])) + "\n"
                bid = "Bid : " + "{0:.2f}".format(float(polo_json[self.key]["highestBid"])) + "\n"
                ask = "Ask : " + "{0:.2f}".format(float(polo_json[self.key]["lowestAsk"])) + "\n"
                volume = "Volume : " + "{0:.2f}".format(float(polo_json[self.key]["baseVolume"])) + "\n"
                value_polo = "```css\n" + volume + last + bid + ask + "```"
            else:
                last = "Last : " + "{0:.8f}".format(float(polo_json[self.key]["last"])) + "\n"
                bid = "Bid : " + "{0:.8f}".format(float(polo_json[self.key]["highestBid"])) + "\n"
                ask = "Ask : " + "{0:.8f}".format(float(polo_json[self.key]["lowestAsk"])) + "\n"
                volume = "Volume : " + "{0:.2f}".format(float(polo_json[self.key]["baseVolume"])) + "\n"
                value_polo = "```css\n" + volume + last + bid + ask + "```"
            embed.add_field(name=":crystal_ball: Poloniex Informations", value=value_polo, inline=True)
        except Exception as e:
            print("err main_polo", e)

        try:
            if self.coin.upper() == "BTC":
                last = "Last : " + "{0:.2f}".format(float(bin_json["lastPrice"])) + "\n"
                bid = "Bid : " + "{0:.2f}".format(float(bin_json["bidPrice"])) + "\n"
                ask = "Ask : " + "{0:.2f}".format(float(bin_json["askPrice"])) + "\n"
                volume = "Volume : " + "{0:.2f}".format(float(bin_json["quoteVolume"])) + "\n"
                value_bin = "```css\n" + volume + last + bid + ask + "```"
            else:
                last = "Last : " + bin_json["lastPrice"] + "\n"
                bid = "Bid : " + bin_json["bidPrice"] + "\n"
                ask = "Ask : " + bin_json["askPrice"] + "\n"
                volume = "Volume : " + "{0:.2f}".format(float(bin_json["quoteVolume"])) + "\n"
                value_bin = "```css\n" + volume + last + bid + ask + "```"
            embed.add_field(name=":game_die: Binance Informations", value=value_bin, inline=True)
        except Exception as e:
            print("err main_binance", e)

        embed.set_thumbnail(url=url_logo)
        embed.set_footer(text="Request achieved on")

        return embed

    async def query_all(self):
        await self.general_cmc()
        data = await self.fetch()
        embed = self.affichage(data)
        return embed

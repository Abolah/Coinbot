import aiohttp
import asyncio
import async_timeout
import discord
import datetime
from random import randint


class Class_whale:
    def __init__(self, arg, auth):
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        self.coin = arg
        self.auth = str(auth).split("#")
        self.auth = self.auth[0]

        if self.coin == "bch":
            self.coin_rex = "bcc"
        else:
            self.coin_rex = self.coin
        if self.coin.upper() == "USD":
            self.key_topia = "BTC_USDT"
            self.key_polo = "USDXBT"
            self.key_finex = "btcusd"
            self.key_rex = "USDT-BTC"
            self.key_kraken = "XBTUSD"
        else:
            self.key_finex = self.coin.upper() + "BTC"
            self.key_rex = "BTC-" + self.coin.upper()
            self.key_polo = "BTC_" + self.coin.upper()
            self.key_topia = self.coin.upper() + "_BTC"
            self.key_kraken = self.coin.upper() + "XBT"
        return

    async def function_fetch(self):
        list_json = []
        list_urls = ["https://bittrex.com/api/v1.1/public/getorderbook?market=" + self.key_rex + "&type=both",
                     "https://api.bitfinex.com/v1/book/" + self.key_finex + "?limit_bids=125&limit_asks=125",
                     "https://poloniex.com/public?command=returnOrderBook&currencyPair=" + self.key_polo + "&depth=150",
                     "https://www.cryptopia.co.nz/api/GetMarketOrders/" + self.key_topia,
                     "https://api.kraken.com/0/public/Depth?pair=" + self.key_kraken + "&count=250"]
        list_name = ["Bittrex", "Bitfinex", "Poloniex", "Cryptopia", "Kraken"]
        for url, name in zip(list_urls, list_name):
            try:
                async with aiohttp.ClientSession() as session:
                    async with async_timeout.timeout(6):
                        async with session.get(url) as resp:
                            if resp.status == 200:
                                list_json.append([await resp.json(), name])
            except asyncio.TimeoutError as e:
                list_json.append(["Timeout", e])
                print(e)
                return list_json
            except Exception as e:
                print(e)
                return 0
        return list_json

    @staticmethod
    async def function_sort_kraken(book_kraken, seuil):
        global key_k
        book_out = []
        print(book_kraken)
        for key in book_kraken["result"]:
            key_k = key
            break
        for i in book_kraken["result"][key_k]["asks"]:
            if float(i[1]) * float(i[0]) >= seuil:
                book_out.append(["Kraken", "Sell", float(i[1]) * float(i[0]), float(i[0])])
        for i in book_kraken["result"][key_k]["bids"]:
            if float(i[1]) * float(i[0]) >= seuil:
                book_out.append(["Kraken", "Buy", float(i[1]) * float(i[0]), float(i[0])])
        return book_out

    @staticmethod
    async def function_sort_all(list_json, seuil):
        book_sorted = []
        for exchange in list_json:
            if exchange[1] == "Bitfinex":
                try:
                    for i in exchange[0]["bids"]:
                        if float(i["amount"]) * float(i["price"]) >= float(seuil):
                            book_sorted.append(
                                ["Bitfinex", "Buy", float(i["amount"]) * float(i["price"]), float(i["price"])])
                    for i in exchange[0]["asks"]:
                        if float(i["amount"]) * float(i["price"]) >= float(seuil):
                            book_sorted.append(
                                ["Bitfinex", "Sell", float(i["amount"]) * float(i["price"]), float(i["price"])])
                except Exception as e:
                    print(e)
            if exchange[1] == "Poloniex":
                try:
                    for i in exchange[0]["asks"]:
                        if float(i[1]) * float(i[0]) >= seuil:
                            book_sorted.append(["Poloniex", "Sell", float(i[0]) * float(i[1]), float(i[0])])
                    for i in exchange[0]["bids"]:
                        if float(i[1] * float(i[0])) >= seuil:
                            book_sorted.append(["Poloniex", "Buy", float(i[0]) * float(i[1]), float(i[0])])
                except Exception as e:
                    print(e)
            if exchange[1] == "Cryptopia":
                try:
                    for i in exchange[0]["Data"]["Sell"]:
                        if i["Total"] >= seuil:
                            book_sorted.append(["Cryptopia", "Sell", i["Total"], float(i["Price"])])
                    for i in exchange[0]["Data"]["Buy"]:
                        if i["Total"] >= seuil:
                            book_sorted.append(["Cryptopia", "Buy", i["Total"], float(i["Price"])])
                except Exception as e:
                    print(e)
            if exchange[1] == "Bittrex":
                try:
                    for i in exchange[0]["result"]["sell"]:
                        if float(i["Quantity"]) * float(i["Rate"]) >= seuil:
                            book_sorted.append(
                                ["Bittrex", "Sell", float(i["Quantity"]) * float(i["Rate"]), float(i["Rate"])])
                    for i in exchange[0]["result"]["buy"]:
                        if float(i["Quantity"]) * float(i["Rate"]) >= seuil:
                            book_sorted.append(
                                ["Bittrex", "Buy", float(i["Quantity"]) * float(i["Rate"]), float(i["Rate"])])
                except Exception as e:
                    print(e)
            if exchange[1] == "Kraken":
                try:
                    for key in exchange[0]["result"]:
                        key_key = key
                        break
                    for i in exchange[0]["result"][key_key]["asks"]:
                        if float(i[1]) * float(i[0]) >= seuil:
                            book_sorted.append(["Kraken", "Sell", float(i[1]) * float(i[0]), float(i[0])])
                    for i in exchange[0]["result"][key_key]["bids"]:
                        if float(i[1]) * float(i[0]) >= seuil:
                            book_sorted.append(["Kraken", "Buy", float(i[1]) * float(i[0]), float(i[0])])
                except Exception as e:
                    print(e)
        final_book = sorted(book_sorted, key=lambda x: x[3], reverse=True)
        return final_book

    async def function_display(self, book):
        coin_wanted = self.coin.upper()
        limit = 10
        sell = 0
        buy = 0
        whale_buy = ""
        whale_sell = ""
        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.add_field(name=":star2: Request about the Whales",
                        value="Here are the informations I could retrieve " + self.auth,
                        inline=False)

        if self.coin.upper() == "BTC":
            symb = " $US"
        else:
            symb = " BTC"
        try:
            for i in book:
                if i[1] == "Buy" and buy < limit:
                    whale_buy += "[" + str(i[0]) + "] " + "Buying for " + "{0:.3f}".format(float(i[2])) + symb + " at " + "{0:.8f}".format(float(i[3])) + symb + "/" + coin_wanted + "\n"
                    buy += 1
                if buy == limit:
                    break
        except Exception as e:
            print(e)

        if whale_buy == "":
            whale_buy = "```css\n Error. The amount you asked may be too high```"
        else:
            whale_buy = "```css\n" + whale_buy + "```"

        embed.add_field(name=":whale2: Informations about the Bidding Whales", value=whale_buy, inline=False)
        try:
            for i in reversed(book):
                if i[1] == "Sell" and sell < limit:
                    whale_sell += "[" + str(i[0]) + "] " + "Selling for " + "{0:.3f}".format(float(i[2])) + symb + " at " + "{0:.8f}".format(float(i[3])) + symb + "/" + coin_wanted + "\n"
                    sell += 1
                if sell == limit:
                    break
        except Exception as e:
            print(e)

        if whale_sell == "":
            whale_sell = "```css\n Error. The amount you asked may be too high```"
        else:
            whale_sell = "```css\n" + whale_sell + "```"

        embed.add_field(name=":whale: Informations about the Asking Whales", value=whale_sell, inline=False)
        return embed

    async def query_whale(self, limit):
        print(limit)
        list_book = await self.function_fetch()
        list_sorted = await self.function_sort_all(list_book, limit)
        embed = await self.function_display(list_sorted)
        return embed

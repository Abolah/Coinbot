import aiohttp
import asyncio
import async_timeout
import discord
import datetime
from random import randint
import time


class Class_bitcoin:
    def __init__(self):
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)

    @staticmethod
    async def fetch():
        list_json = []
        list_urls = ["https://api.kraken.com/0/public/Ticker?pair=XBTUSD",
                     "https://www.bitstamp.net/api/v2/ticker/btcusd",
                     "https://bittrex.com/api/v1.1/public/getmarketsummary?market=usdt-btc",
                     "https://api.coinbase.com/v2/prices/spot?currency=USD",
                     "https://api.bitfinex.com/v1/pubticker/btcusd",
                     "https://www.bitmex.com/api/v1/instrument?symbol=XBTUSD",
                     "https://api.bithumb.com/public/ticker/BTC", "https://api.hitbtc.com/api/1/public/BTCUSD/ticker",
                     "https://api.gemini.com/v1/pubticker/btcusd"]
        list_name = ["Kraken", "Bitstamp", "Bittrex", "Coinbase", "Bitfinex", "Bitmex", "Bithumb", "HitBTC", "Gemini"]
        for url, name in zip(list_urls, list_name):
            try:
                async with aiohttp.ClientSession() as session:
                    async with async_timeout.timeout(15):
                        async with session.get(url) as resp:
                            if resp.status == 200:
                                time.sleep(0.01)
                                list_json.append([await resp.json(), name])
            except asyncio.TimeoutError as e:
                list_json.append(["Timeout", e])
                print(e)
                return list_json
            except Exception as e:
                print(e)
                return 0
        return list_json

    def function_display(self, list_json, author):
        value = ""
        value_other = ""
        won_value = 0.000888
        author = str(author).split("#")

        for i in list_json:
            if i[1] == "Kraken":
                try:
                    value = value + "Kraken : " + "$ " + "{0:.2f}".format(
                        float(i[0]["result"]["XXBTZUSD"]["c"][0])) + " [USD]\n"
                except Exception as e:
                    print(e)
            if i[1] == "Bitmex":
                try:
                    value = value + "Bitmex : " + "$ " + "{0:.2f}".format(float(i[0][0]["lastPrice"])) + " [USD]\n"
                except Exception as e:
                    print(e)
            if i[1] == "Coinbase":
                try:
                    value = value + "Coinbase : " + "$ " + "{0:.2f}".format(float(i[0]["data"]["amount"])) + " [USD]\n"
                except Exception as e:
                    print(e)
            if i[1] == "Bitstamp":
                try:
                    value = value + "Bitstamp : " + "$ " + "{0:.2f}".format(float(i[0]["last"])) + " [USD]\n"
                except Exception as e:
                    print(e)
            if i[1] == "Bittrex":
                try:
                    value = value + "Bittrex : " + "$ " + "{0:.2f}".format(i[0]["result"][0]["Last"]) + " [USDT]\n"
                except Exception as e:
                    print(e)
            if i[1] == "Bitfinex":
                try:
                    value = value + "Bitfinex " + "$ " + "{0:.2f}".format(float(i[0]["last_price"])) + " [USDT]\n"
                except Exception as e:
                    print(e)
            if i[1] == "Binance":
                try:
                    value = value + "Binance " + "$ " + "{0:.2f}".format(float(i[0]["bidPrice"])) + " [USDT]"
                except Exception as e:
                    print(e)
            if i[1] == "Bitflyer":
                try:
                    value_other = value_other + "Bitflyer : " + "$ " + "{0:.2f}".format(float(i[0]["best_bid"])) + " [USDT]\n"
                except Exception as e:
                    print(e)
            if i[1] == "Bithumb":
                try:
                    value_other = value_other + "Bithumb : " + "$ " + "{0:.2f}".format(float(i[0]["data"]["buy_price"]) * won_value) + " [USD]\n"
                except Exception as e:
                    print(e)
            if i[1] == "HitBTC":
                try:
                    value_other = value_other + "HitBTC : " + "$ " + "{0:.2f}".format(float(i[0]["bid"])) + " [USDT]\n"
                except Exception as e:
                    print(e)
            if i[1] == "Gemini":
                try:
                    value_other = value_other + "Gemini : " + "$ " + "{0:.2f}".format(float(i[0]["bid"])) + " [USD]"
                except Exception as e:
                    print(e)

        value_other = "```css\n" + value_other + " ```"
        value = "```css\n" + value + " ```"
        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.set_thumbnail(url="https://files.coinmarketcap.com/static/img/coins/32x32/bitcoin.png")
        embed.set_footer(text="Request achieved :")
        embed.add_field(name=":star2: Request about Bitcoin",
                        value="Here are the informations I could retrieve " + str(author[0]), inline=False)
        embed.add_field(name=":trophy: Informations about Bitcoin", value=value, inline=False)
        embed.add_field(name=" :flag_mp: Informations about the other Exchanges", value=value_other)
        return embed

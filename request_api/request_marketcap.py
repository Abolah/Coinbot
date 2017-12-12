import discord
import datetime
import aiohttp
import asyncio
import async_timeout
from random import randint


class Coinmarketcap:

    def __init__(self):
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)

    @staticmethod
    async def fetch():
        list_json = []
        list_name = ["Bitcoin", "Coinmarketcap"]
        list_urls = ["https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=USD",
                     "https://api.coinmarketcap.com/v1/global/?convert=USD"]
        for i, name in zip(list_urls, list_name):
            try:
                async with aiohttp.ClientSession() as session:
                    async with async_timeout.timeout(5):
                        async with session.get(i) as resp:
                            if resp.status == 200:
                                list_json.append([await resp.json(), name])
            except asyncio.TimeoutError as e:
                list_json.append([e, name])
                print(e)
                return list_json
            except Exception as e:
                print(e)
                return 0
        return list_json

    def format_affichage(self, json_data, json_data_btc, author):

        url_logo = "https://files.coinmarketcap.com/static/img/coins/32x32/bitcoin.png"
        try:
            author = str(author).split("#")
        except:
            author = "khey"
        try:
            marketcap = "Market Cap = " + "{:,}".format(json_data["total_market_cap_usd"]) + "$\n"
            volume = "Market Volume : " + "{:,}".format(json_data["total_24h_volume_usd"]) + "$\n"
            dominance = "Bitcoin Dominance = " + str(json_data["bitcoin_percentage_of_market_cap"]) + "%\n"
            nb_coin = "Coins : " + str(json_data["active_currencies"]) + "\n"
            active_markets = "Pairs : " + str(json_data["active_markets"]) + "\n"
            value = "```css\n" + marketcap + dominance + volume + "```"
            value_annex = "```css\n" + active_markets + nb_coin + "```"
        except:
            value = "```css\nCMC API Error: MAIN API```"
            value_annex = "```css\nCMC API Error : SIDE API```"
        try:
            price = "BTC Price : " + "{:,}".format(float(json_data_btc[0]["price_usd"])) + "$\n"
            volume = "24h Volume: " + "{:,}".format(float(json_data_btc[0]["24h_volume_usd"])) + "$\n"
            change_1 = "24h Swing : " + str(json_data_btc[0]["percent_change_24h"]) + "%\n"
            change_7 = "7 days Swing : " + str(json_data_btc[0]["percent_change_7d"]) + "%\n\n"
            value_btc = "```css\n" + price + volume + change_1 + change_7 + "```"
        except Exception as e:
            print(e)
            value_btc = "```css\nCMC API Error : BTC API```"

        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.set_thumbnail(url=url_logo)
        embed.set_footer(text="Request achieved on")
        embed.add_field(name=":star2: Request on the whole CryptoMarket",
                        value="Here are the informations I could retrieve " + str(author[0]),
                        inline=False)
        embed.add_field(name=":trophy: CoinMarketCap Informations", value=value)
        embed.add_field(name=":medal: Bitcoin Informations", value=value_btc, inline=True)
        embed.add_field(name=":information_source: Additional Informations", value=value_annex, inline=True)
        return embed

    async def cmc_query(self, author):
        json_data = ""
        json_data_btc = ""
        result = await self.fetch()
        if result[0][1] == "Bitcoin":
            json_data_btc = result[0][0]
        if result[1][1] == "Coinmarketcap":
            json_data = result[1][0]
        embed = self.format_affichage(json_data, json_data_btc, author)
        return embed

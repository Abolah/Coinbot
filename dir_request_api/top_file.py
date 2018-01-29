import datetime
import discord
import aiohttp
import async_timeout
import asyncio
from random import randint


class Topcoin:
    def __init__(self):
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)

    @staticmethod
    async def fetch():
        list_json = []
        list_name = ["CoinmarketcapLimit", "Coinmarketcap"]
        list_urls = ["https://api.coinmarketcap.com/v1/ticker/?limit=200",
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
                return list_json
            except Exception as e:
                print(e)
                return 0
        return list_json

    @staticmethod
    def to_list(json_data):
        list = []
        try:
            for i in json_data:
                if i["percent_change_24h"] is None:
                    i["percent_change_24h"] = 0
                if i["percent_change_1h"] is None:
                    i["percent_change_1h"] = 0
                if i["percent_change_7d"] is None:
                    i["percent_change_7d"] = 0
                list.append([i["name"], int(i["rank"]), float(i["percent_change_1h"]), float(i["percent_change_24h"]),
                             float(i["percent_change_7d"]), i["symbol"]])
        except Exception as e:
            print("Error converting to list")
            return "Error converting to list" + str(e)
        return list

    @staticmethod
    def top_sorting(list):
        sorted_list = sorted(list, key=lambda x: x[3])
        return sorted_list

    def format_affichage(self, sorted_list, data_global, author):
        url_logo = "https://files.coinmarketcap.com/static/img/coins/32x32/bitcoin.png"
        try:
            author = str(author).split("#")
        except:
            author = "khey"
        try:
            wcoin1 = "Rank [" + str(sorted_list[-1][1]) + "] [" + sorted_list[-1][5] + "] " + sorted_list[-1][
                0] + " : " + str(sorted_list[-1][3]) + " %\n"
            wcoin2 = "Rank [" + str(sorted_list[-2][1]) + "] [" + sorted_list[-2][5] + "] " + sorted_list[-2][
                0] + " : " + str(sorted_list[-2][3]) + " %\n"
            wcoin3 = "Rank [" + str(sorted_list[-3][1]) + "] [" + sorted_list[-3][5] + "] " + sorted_list[-3][
                0] + " : " + str(sorted_list[-3][3]) + " %\n"
            wcoin4 = "Rank [" + str(sorted_list[-4][1]) + "] [" + sorted_list[-4][5] + "] " + sorted_list[-4][
                0] + " : " + str(sorted_list[-4][3]) + " %\n"
            wcoin5 = "Rank [" + str(sorted_list[-5][1]) + "] [" + sorted_list[-5][5] + "] " + sorted_list[-5][
                0] + " : " + str(sorted_list[-5][3]) + " %\n"
            value_win = "```css\n" + wcoin1 + wcoin2 + wcoin3 + wcoin4 + wcoin5 + "```"
        except Exception as e:
            print(e)
            value_win = "```css\nErreur de l'API CMC : Principal win```"
        try:
            lcoin1 = "Rank [" + str(sorted_list[0][1]) + "] [" + sorted_list[0][5] + "] " + sorted_list[0][
                0] + " : " + str(sorted_list[0][3]) + " %\n"
            lcoin2 = "Rank [" + str(sorted_list[1][1]) + "] [" + sorted_list[1][5] + "] " + sorted_list[1][
                0] + " : " + str(sorted_list[1][3]) + " %\n"
            lcoin3 = "Rank [" + str(sorted_list[2][1]) + "] [" + sorted_list[2][5] + "] " + sorted_list[2][
                0] + " : " + str(sorted_list[2][3]) + " %\n"
            lcoin4 = "Rank [" + str(sorted_list[3][1]) + "] [" + sorted_list[3][5] + "] " + sorted_list[3][
                0] + " : " + str(sorted_list[3][3]) + " %\n"
            lcoin5 = "Rank [" + str(sorted_list[4][1]) + "] [" + sorted_list[4][5] + "] " + sorted_list[4][
                0] + " : " + str(sorted_list[4][3]) + " %\n"
            value_loose = "```js\n" + lcoin1 + lcoin2 + lcoin3 + lcoin4 + lcoin5 + "```"
        except Exception as e:
            print(e)
            value_loose = "```css\nErreur de l'API CMC : Principal loose```"

        try:
            marketcap = "Market Cap = " + "$ " + "{:,}".format(data_global["total_market_cap_usd"]) + "\n"
            volume = "Market Volume : " + "$ " + "{:,}".format(data_global["total_24h_volume_usd"]) + "\n"
            dominance = "Bitcoin Dominance = " + str(data_global["bitcoin_percentage_of_market_cap"]) + "%\n"
            value_annex = "```css\n" + marketcap + volume + dominance + "```"
        except Exception as e:
            print(e)
            value_annex = "```css\nCMC API Error : SIDE API```"

        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.set_thumbnail(url=url_logo)
        embed.set_footer(text="Request achieved on")
        embed.add_field(name=":star2: Request about the Top 200 coins",
                        value="Here are the informations I could retrieve " + str(author[0]),
                        inline=False)
        embed.add_field(name=":chart_with_upwards_trend: Top Win 24h", value=value_win)
        embed.add_field(name=":chart_with_downwards_trend: Top Lose 24h", value=value_loose)
        embed.add_field(name=":information_source: Additional Informations", value=value_annex)
        return embed

    async def query_top(self, author):
        json_global = ""
        sorted = []
        result = await self.fetch()
        if result[0][1] == "CoinmarketcapLimit":
            sorted = self.top_sorting(self.to_list(result[0][0]))
        if result[1][1] == "Coinmarketcap":
            json_global = result[1][0]
        embed = self.format_affichage(sorted, json_global, author)
        return embed

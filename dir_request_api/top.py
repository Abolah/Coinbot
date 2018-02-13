import datetime
import discord
import requests
from random import randint


class Class_Topcoin:
    def __init__(self, auth):
        self.auth = str(auth).split("#")
        self.auth = self.auth[0]
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        self.url_logo = "https://files.coinmarketcap.com/static/img/coins/32x32/bitcoin.png"
        self.global_cmc = "https://api.coinmarketcap.com/v1/global/?convert=USD"
        self.ticker_cmc = "https://api.coinmarketcap.com/v1/ticker/?limit=500"

    async def function_cmc_side(self):
        request = requests.get(self.global_cmc)
        cmc_json = request.json()

        marketcap = "Market Cap = ${:,}".format(cmc_json["total_market_cap_usd"]) + "\n"
        volume = "Market Volume : ${:,}".format(cmc_json["total_24h_volume_usd"]) + "\n"
        dominance = "Bitcoin Dominance = " + str(cmc_json["bitcoin_percentage_of_market_cap"]) + "%\n"
        active_markets = "Pairs : " + str(cmc_json["active_markets"]) + "\n"
        value_cmc = "```css\n" + marketcap + volume + dominance + active_markets + "```"

        return value_cmc

    async def function_list(self):
        request = requests.get(self.ticker_cmc)
        win_json = request.json()

        list = []
        for i in win_json:
            if i["percent_change_24h"] is None:
                i["percent_change_24h"] = 0
            if i["percent_change_1h"] is None:
                i["percent_change_1h"] = 0
            if i["percent_change_7d"] is None:
                i["percent_change_7d"] = 0
            list.append([i["name"], int(i["rank"]), float(i["percent_change_1h"]), float(i["percent_change_24h"]),
                         float(i["percent_change_7d"]), i["symbol"]])

        sorted_list = sorted(list, key=lambda x: x[3])
        return sorted_list

    @staticmethod
    async def function_top_win(sorted_list):

        win1 = "Rank [" + str(sorted_list[-1][1]) + "] [" + sorted_list[-1][5] + "] " + sorted_list[-1][
            0] + " : " + str(sorted_list[-1][3]) + " %\n"
        win2 = "Rank [" + str(sorted_list[-2][1]) + "] [" + sorted_list[-2][5] + "] " + sorted_list[-2][
            0] + " : " + str(sorted_list[-2][3]) + " %\n"
        win3 = "Rank [" + str(sorted_list[-3][1]) + "] [" + sorted_list[-3][5] + "] " + sorted_list[-3][
            0] + " : " + str(sorted_list[-3][3]) + " %\n"
        win4 = "Rank [" + str(sorted_list[-4][1]) + "] [" + sorted_list[-4][5] + "] " + sorted_list[-4][
            0] + " : " + str(sorted_list[-4][3]) + " %\n"
        win5 = "Rank [" + str(sorted_list[-5][1]) + "] [" + sorted_list[-5][5] + "] " + sorted_list[-5][
            0] + " : " + str(sorted_list[-5][3]) + " %\n"
        value_win = "```css\n" + win1 + win2 + win3 + win4 + win5 + "```"

        return value_win

    @staticmethod
    async def function_top_lose(sorted_list):

        lose1 = "Rank [" + str(sorted_list[0][1]) + "] [" + sorted_list[0][5] + "] " + sorted_list[0][
            0] + " : " + str(sorted_list[0][3]) + " %\n"
        lose2 = "Rank [" + str(sorted_list[1][1]) + "] [" + sorted_list[1][5] + "] " + sorted_list[1][
            0] + " : " + str(sorted_list[1][3]) + " %\n"
        lose3 = "Rank [" + str(sorted_list[2][1]) + "] [" + sorted_list[2][5] + "] " + sorted_list[2][
            0] + " : " + str(sorted_list[2][3]) + " %\n"
        lose4 = "Rank [" + str(sorted_list[3][1]) + "] [" + sorted_list[3][5] + "] " + sorted_list[3][
            0] + " : " + str(sorted_list[3][3]) + " %\n"
        lose5 = "Rank [" + str(sorted_list[4][1]) + "] [" + sorted_list[4][5] + "] " + sorted_list[4][
            0] + " : " + str(sorted_list[4][3]) + " %\n"
        value_loose = "```js\n" + lose1 + lose2 + lose3 + lose4 + lose5 + "```"

        return value_loose

    async def function_format_display(self, side, win, lose):

        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.set_thumbnail(url=self.url_logo)
        embed.set_footer(text="Request achieved :")
        embed.add_field(name=":star2: Request about the Top 200 coins",
                        value="Here are the informations I could retrieve " + self.auth,
                        inline=False)
        embed.add_field(name=":chart_with_upwards_trend: Top Win 24h", value=win)
        embed.add_field(name=":chart_with_downwards_trend: Top Lose 24h", value=lose)
        embed.add_field(name=":information_source: Additional Informations", value=side)
        return embed

    async def query_top(self):
        side = await self.function_cmc_side()
        sorted_list = await self.function_list()
        win = await self.function_top_win(sorted_list)
        lose = await self.function_top_lose(sorted_list)
        embed = await self.function_format_display(side, win, lose)
        return embed

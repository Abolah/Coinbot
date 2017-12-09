import aiohttp
import async_timeout
import asyncio
import discord
import datetime
from random import randint


class Conv:
    def __init__(self, auth):
        self.auth = str(auth).split("#")
        self.auth = self.auth[0]
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        self.id = "None"
        return

    async def price(self, coin, qty):
        global total_btc, total_usd
        url = "https://api.coinmarketcap.com/v1/ticker/?limit=1000"
        result = []
        data = None
        async with aiohttp.ClientSession() as session:
            try:
                async with async_timeout.timeout(5):
                    async with session.get(url) as resp:
                        if resp.status == 200:
                            data = await resp.json()
            except asyncio.TimeoutError as e:
                data = e
        try:
            total_usd = "Impossible to calculate the price"
            total_btc = "Impossible to calculate the price"
            for i in data:
                if i["symbol"] == coin.upper():
                    self.id = str(i["id"]).replace(" ", "-").lower()
                    total_usd = float(i["price_usd"]) * float(qty)
                    total_btc = float(i["price_btc"]) * float(qty)
        except Exception as e:
            print(e)

        result.append(total_btc)
        result.append(total_usd)
        return result

    def affichage(self, data, coin, qty):

        if isinstance(data[0], float):
            value = "```css\n" + qty + " " + coin.upper() + " valent " + "{0:.8f}".format(
                data[0]) + " BTC\n" + qty + " " + coin.upper() + " valent " + "{0:.2f}".format(data[1]) + " $```"
        else:
            value = "```css\nImpossible to calculate the price```"

        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.set_thumbnail(url="https://files.coinmarketcap.com/static/img/coins/32x32/" + self.id + ".png")
        embed.set_footer(text="Request achieved on")
        embed.add_field(name=":star2: Request of " + self.auth,
                        value="Here are the information that I could retrieve " + self.auth,
                        inline=False)
        embed.add_field(name=":tada: Information about your coin's price", value=value,
                        inline=True)
        return embed

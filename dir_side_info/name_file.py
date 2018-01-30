from random import randint
import datetime
import discord
import aiohttp
import async_timeout
import asyncio


class Class_Name:
    def __init__(self, auth, arg):
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        self.auth = str(auth).split("#")
        self.auth = self.auth[0]
        self.coin = arg
        return

    @staticmethod
    async def function_query_name():
        url = "https://api.coinmarketcap.com/v1/ticker/?limit=1000"
        data = ""
        async with aiohttp.ClientSession() as session:
            try:
                async with async_timeout.timeout(5):
                    async with session.get(url) as resp:
                        if resp.status == 200:
                            data = await resp.json()
            except asyncio.TimeoutError as e:
                data = e
        return data

    async def function_display(self, data):
        idcoin = "NONE"
        long_name = "NONE"
        price_usd = "0"
        price_btc = "0"
        try:
            for i in data:
                if i["symbol"] == self.coin.upper():
                    long_name = i["name"]
                    idcoin = i["id"]
                    price_btc = i["price_btc"]
                    price_usd = i["price_usd"]
                    break
            data = "```css\nThe coin " + self.coin.upper() + " has for name " + long_name + "\nThe BTC value is about : " + price_btc + "\nThe USD value is about : " + price_usd + "$\n```"
        except Exception as e:
            print(e)
            data = "```Error name\n```"
        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.set_thumbnail(url="https://files.coinmarketcap.com/static/img/coins/32x32/" + idcoin + ".png")
        embed.set_footer(text="Request achieved on")
        embed.add_field(name=":star2: Request for the name of " + self.coin.upper(),
                        value="Here are the information that I could retrieve " + self.auth,
                        inline=False)
        embed.add_field(name=":tada: Information about the coin " + self.coin.upper(), value=data,
                        inline=True)
        return embed

from pymarketcap import Pymarketcap
import discord
import datetime
from random import randint


class Class_Conv:
    def __init__(self, auth):
        self.auth = str(auth).split("#")
        self.auth = self.auth[0]
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        self.id = "None"
        self.name = "None"
        self.price_usd = "None"
        self.price_btc = "None"
        self.price_eur = "None"
        self.coin = "None"
        return

    async def function_cmc(self, coin):
        self.coin = coin.upper()
        coinmarketcap = Pymarketcap()
        cmc_json = coinmarketcap.ticker(self.coin, convert="EUR")
        btc_json = coinmarketcap.ticker(self.coin, convert="BTC")

        self.price_usd = float(cmc_json["data"]["quotes"]["USD"]["price"])
        self.price_eur = float(cmc_json["data"]["quotes"]["EUR"]["price"])
        self.price_btc = float(btc_json["data"]["quotes"]["BTC"]["price"])
        return

    async def function_price_calc(self, qty):
        total_usd = self.price_usd * float(qty)
        total_btc = self.price_btc * float(qty)
        total_eur = self.price_eur * float(qty)
        value = "```css\n{0} {1} are worth {2:.8f} BTC\n{0} {1} are worth ${3:.2f}\n{0} {1} are worth {4:.2f}€\n``` ".format(qty, self.coin, total_btc, total_usd, total_eur)
        return value

    async def function_display(self, value):
        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.add_field(name=":tada: Information about your coin's value", value=value)
        embed.set_footer(text="Request achieved :")
        return embed

    async def function_convert(self, coin, qty):
        await self.function_cmc(coin)
        calculator = await self.function_price_calc(qty)
        embed = await self.function_display(calculator)

        return embed

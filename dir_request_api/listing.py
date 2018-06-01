from pymarketcap import Pymarketcap
import datetime
import discord
from random import randint


class Class_listing:
    def __init__(self, auth):
        self.auth = str(auth).split("#")
        self.auth = self.auth[0]
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        self.name = "None"
        self.logo_url = "https://s2.coinmarketcap.com/static/img/coins/32x32/{}.png"
        self.default_ticker = "BTC"
        return

    def function_cmc(self, coin):
        global cmc_json
        if coin == "iota":
            coin = "miota"
            coin = coin.upper()
        elif coin == "knc":
            coin = "kyber-network"
        else:
            coin = coin.upper()
        coinmarketcap = Pymarketcap(timeout=10)
        cmc_json = coinmarketcap.ticker(coin, convert="EUR")
        id_coin = cmc_json["data"]["id"]
        btc_json = coinmarketcap.ticker(coin, convert="BTC")
        name = cmc_json["data"]["name"]
        btc_value = float(btc_json["data"]["quotes"]["BTC"]["price"] / 0.00000001)
        usd_value = float(cmc_json["data"]["quotes"]["USD"]["price"])
        price = str("```\nHourly : {}%\nDaily : {}%\nWeekly : {}%\n```").format(cmc_json["data"]["quotes"]["USD"]["percent_change_1h"], cmc_json["data"]["quotes"]["USD"]["percent_change_24h"], cmc_json["data"]["quotes"]["USD"]["percent_change_7d"])
        side = str("```\nRank : {}\nMarketCap : {:,.2f}M\nVolume : {}M\n```").format(cmc_json["data"]["rank"], float(cmc_json["data"]["quotes"]["USD"]["market_cap"]/1000000), float(cmc_json["data"]["quotes"]["USD"]["volume_24h"]/1000000))
        value_mc = price + side
        embed_disp = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                                   timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed_disp.set_author(name="[{}] | {:,.0f}sats | {:,.2f}$".format(coin, btc_value, usd_value), url="",
                              icon_url=self.logo_url.format(id_coin))
        embed_disp.add_field(name=name, value=value_mc, inline=True)
        embed_disp.set_footer(text="Request achieved :")
        return embed_disp

    async def mini(self, coin):
        global embed
        embed = self.function_cmc(coin)

        return embed

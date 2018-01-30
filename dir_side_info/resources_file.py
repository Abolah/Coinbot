import datetime
import discord
from random import randint


class Class_Resources:
    def __init__(self):
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        return

    @staticmethod
    def function_display():
        embed = discord.Embed(colour=discord.Colour(0x59b94a))
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/389024205985021954/402873687797268502/BMlogo.png")
        embed.add_field(name=":money_with_wings: Our favorite Exchanges :money_with_wings: ",
                        value="```www.gdax.com\nwww.bittrex.com\nhttps://www.binance.com/?ref=10812833\nwww.gemini.com\nwww.poloniex.com\nwww.kraken.com\nwww.bitfinex.com\nhttps://www.coinbase.com/join/58d1836873edbf00857e7276\nhttps://hitbtc.com/?ref_id=5a449aed2067c\nhttps://cex.io/r/0/up104761168/0/\nhttps://mercatox.com/?referrer=30546\nhttps://www.kucoin.com/#/?r=1bH3t ```")
        embed.add_field(name=":slot_machine: Trading Tools :slot_machine: ",
                        value="```\nTradingView\nhttps://www.coinigy.com/?r=d82151f2```")
        embed.add_field(name=":pick: Mining (if you need help just ask your question in #mining) :pick: ",
                        value="```\nhttps://minergate.com/a/d579a576a20a33fa80651b5c```")
        return embed

    async def get_resources(self):
        embed = self.function_display()
        return embed

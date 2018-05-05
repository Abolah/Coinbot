import datetime
import discord
from random import randint


class Class_update:
    def __init__(self):
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        return

    def function_display(self):
        embed = discord.Embed(title="Coinbot's CHANGELOG", colour=discord.Colour(self.color), description="Here are the latest update for CoinBot")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/393197371254767616/400637492191035404/bbot.png")
        embed.add_field(name="V3.4 Date: 6 May 2018", value="```\nRemoved some bugs.\nNow when you search a coin not listed on coinmarketcap the bot tells you the coin is not listed.\n```", inline=False)
        embed.add_field(name="V3.3 Date: 11 April 2018",value="```\nAdded the !mexbook command to display Bitmex orderbook.\n```", inline=False)
        embed.add_field(name="V3.2 Date: 4 April 2018",value="```\nFixed the !event command with the new coinmarketcal api.\n```", inline=False)
        embed.add_field(name="V3.1.5 Date: 21 March 2018", value="```\nError management for Bitfinex\nAlso modified the !name command.\n```", inline=False)
        embed.add_field(name="V3.1 Date: 13 March 2018", value="```\nModified the layout of all commands.\nModified some behaviours and solved some issues.\n```", inline=False)
        embed.add_field(name=":star:Thank you for your support !:star:",
                        value="If you like Coinbot don't forget to upvote it here: https://discordbots.org/bot/367061304042586124\nYou can also donate to the addresses listed in !bot.")
        return embed

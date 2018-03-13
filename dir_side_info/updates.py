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
        embed.add_field(name="V3.0 Date: 13 March 2018", value="```\nAdded the !updates command.\nModified some behaviours and solved some issues.\n```", inline=False)
        embed.add_field(name="V2.9.5 Date: 6 March 2018", value="```\nAdded the !balance command to check the value of a wallet in BTC or ETH (tokens too) on the blockchain.\nSolved some issues.\n```", inline=False)
        embed.add_field(name=":star:Thank you for your support !:star:",
                        value="If you like Coinbot don't forget to upvote it here: https://discordbots.org/bot/367061304042586124\nYou can also donate to the addresses listed in !bot.")
        return embed

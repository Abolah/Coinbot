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
        embed.add_field(name="V4.2 Date: 3rd June 2018",value="```\nAdded the !listing command to display the 5 latest listed coins on CoinMarketCap.\n```", inline=False)
        embed.add_field(name="V4.1 Date: 22 May 2018", value="```\nFixed the !event command and added a sort by coins.\n Also added coins logo on the exchanges commands.\n```", inline=False)
        embed.add_field(name="V4.0 Date: 22 May 2018", value="```\nBrand new !mini command !\n```", inline=False)
        embed.add_field(name="V3.6 Date: 20 May 2018", value="```\nNo more display errors when looking at low value coins\n```", inline=False)
        embed.add_field(name="V3.5 Date: 15 May 2018", value="```\nModified the command to use CoinMarketCap V2 API.\n```", inline=False)
        embed.add_field(name="V3.4 Date: 6 May 2018", value="```\nRemoved some bugs.\nNow when you search a coin not listed on coinmarketcap the bot tells you the coin is not listed.\n```", inline=False)
        embed.add_field(name=":star:Thank you for your support !:star:",
                        value="If you like Coinbot don't forget to upvote it here: https://discordbots.org/bot/367061304042586124\nYou can also donate to the addresses listed in !bot.")
        return embed

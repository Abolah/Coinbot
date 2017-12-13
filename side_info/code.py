import datetime
import discord
from random import randint


class Code:
    def __init__(self):
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        return

    def affichage(self):
        source_url = "```css\nhttps://github.com/Abolah/Coinbot```"
        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com")
        embed.add_field(name=":hammer:  You want to see the source code ?",
                        value="You can go to the following URL", inline=False)
        embed.add_field(name=":hammer_pick:    GitHub\n", value=source_url, inline=True)
        return embed

    async def get_code(self):
        embed = self.affichage
        return embed

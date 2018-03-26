import datetime
import discord
from random import randint


class Class_On_join:
    def __init__(self):
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        return

    def function_display(self):
        embed = discord.Embed(title="Hello !", colour=self.color)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/393197371254767616/400637492191035404/bbot.png")
        embed.add_field(name="Nice to meet you :)",
                        value="```I'm Coinbot, you personnal cryptocurrencies assitant.\nTo get started just type the `!infos` command.\nYou might also want to know about the latest updates. Just use the `!updates`command for this.\nAnd finally, the `!bot`command will give you some informations about me.```")

        return embed

    async def function_welcome(self):
        embed = self.function_display()
        return embed

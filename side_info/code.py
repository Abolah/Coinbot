import datetime
import discord
from random import randint


class Code:
    def __init__(self):
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        return

    def affichage(self):
        embed = discord.Embed(title="Github URL", colour=discord.Colour(0x2dca6f),
                              url="https://github.com/Abolah/Coinbot",
                              description=":hammer_pick: I am the developper of CoinBot.```\nYou can check out the source code here,\nhttps://github.com/Abolah/Coinbot```")
        embed.set_thumbnail(url="https://cdn4.iconfinder.com/data/icons/space-and-astronomy-1/800/robot-512.png")
        embed.set_author(name="Abolah", url="https://twitter.com/Abolaah",
                         icon_url="https://vignette.wikia.nocookie.net/epicrapbattlesofhistory/images/e/eb/Deal_with_it_rainbow_style_by_j_brony-d4cwgad.png")
        embed.add_field(name=":star2:Do you like my work ? :star2:",
                        value="```You can donate to theses addresses:\nBTC : 1jc3V3T5mefuD9asa7en976NKVGssQuMq\nETH(ERC20 friendly) : abowallet.eth\nDOGE : DSEaEfD4NQ68xbD92wN9UgcL66qZtwiFJB\nLTC : LQS415ftVrkSjjmFUyKNVBhY1fJzFLSKaz\nDash : XkbrvfjnN1geyBJVe8igNwDYVFRPNWpRuz```")
        embed.add_field(name=":information_source: Do you need help ? :information_source:",
                        value="```Send me a message at :\n@Abolah#6887 on Discord\n@Abolaah on Twitter.```")
        embed.add_field(name=":interrobang:Can I use the Bot on my own server ? :interrobang:",
                        value="```Yes, the bot is and will remain free to use for anyone.\nIf you want me to host the bot for you, send me a message.```")

        return embed

    async def get_code(self):
        embed = self.affichage
        return embed

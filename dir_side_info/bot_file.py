import datetime
import discord
from random import randint


class Class_Bot:
    def __init__(self):
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        return

    @staticmethod
    def function_display(srv_count, user_count):
        embed = discord.Embed(title="CoinBot's Website", colour=discord.Colour(0x2dca6f),
                              url="https://coinbot.ovh",
                              description=":hammer_pick: I am the developer of CoinBot.```\nIf you have requests or issues send me a message on Discord ! @Abolah#1337```")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/393197371254767616/400637492191035404/bbot.png")
        embed.set_author(name="Abolah", url="https://twitter.com/Abolaah",
                         icon_url="https://vignette.wikia.nocookie.net/epicrapbattlesofhistory/images/e/eb/Deal_with_it_rainbow_style_by_j_brony-d4cwgad.png")
        embed.add_field(name=":star2:Do you like my work ? :star2:",
                        value="```You can donate to theses addresses:\nETH(ERC20 friendly) : abowallet.eth\nBTC  : 1jc3V3T5mefuD9asa7en976NKVGssQuMq\nLTC  : LQS415ftVrkSjjmFUyKNVBhY1fJzFLSKaz\nDash : XkbrvfjnN1geyBJVe8igNwDYVFRPNWpRuz```")
        embed.add_field(name=":information_source: Do you need help ? :information_source:",
                        value="```Send me a message at :\n@Abolah#1337 on Discord\n@Abolaah on Twitter.```")
        embed.add_field(name="CoinBot is famous !",
                        value="```CoinBot is installed on " + srv_count + " Discord servers and used by " + str(user_count) + " users !```")

        return embed

    async def function_get_code(self, srv_count, user_count):
        embed = self.function_display(srv_count, user_count)
        return embed

import datetime
import discord
from random import randint

class Donate():
    def __init__(self):
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        return

    def affichage(self):
        value_test = "```css\nBitcoin : [1jc3V3T5mefuD9asa7en976NKVGssQuMq]```"
        value_ETH = "```css\n Ethereum : [abowallet.eth]```"
        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com")
        embed.set_thumbnail(url="https://files.coinmarketcap.com/static/img/coins/32x32/bitcoin.png")
        embed.add_field(name=":slot_machine: Tu veux me donner des sous ?", value="Envoie moi des BTC ou des ETH a ces adresses !", inline=False)
        embed.add_field(name=":dvd: Adresses de donation BTC\n", value=value_test, inline=True)
        embed.add_field(name=":dvd: Adresses de donation ETH\n", value=value_ETH, inline=True)
        return embed


    async def get_donate(self):
        embed = self.affichage
        return embed
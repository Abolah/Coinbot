from random import randint
import datetime
import discord
import random
import requests
import json


class Doge:
    def __init__(self):
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        return

    def affichage(self):
        priceURL = "https://api.coinmarketcap.com/v1/ticker/dogecoin/?convert=EUR"
        paramprice = "price_usd"
        resp = requests.get(url=priceURL, params=paramprice)
        data = json.loads(resp.text)
        price = "```css\n" + "Price : " + "{0:.3f}".format(
            float(data[0]["price_usd"])) + "$\n" + "Target : Moon" + "```"

        haiku1 = "Roses are red, Violet are blue.\nAll in DOGE, he will never fail you."
        haiku2 = "Roses are red, Violet are blue.\nIf you question DOGE, Burn will do you."
        haiku3 = "Roses are red, Violet are blue.\nWith DOGE there is no such thing,\nas too much value"
        haiku4 = "Roses are red, Violet are blue.\nThe only thing that matters,\nis DOGE revenue"
        haiku5 = "Once upon a time,\n A stranger entered the Pack.\n\nDubbed and amazed,\nby the beautiful cryptospace, he asked\n'What coin should I invest? Target Sir?'\n\nOut of the blue,\nOur Saviour Mcgruff came through,\nHe explained what we all knew:\nDOGE is our virtue "
        haiku6 = "Roses are red, Violet are blue.\nI can't really rhyme, but the Shibas are mine"
        haiku7 = "BTC, Ethereum, Litecoin or maybe even Ripple,\nIt doesn't really matter.\nCompared to DOGE,\nEverything is cripple."
        haiku8 = "DOGE is love, DOGE is life,\nIf you wanna make money, Better sell your wife."

        choice = random.choice([haiku1, haiku2, haiku3, haiku4, haiku5, haiku6, haiku7, haiku8])
        choice = "```css\n" + choice + "```"

        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com")
        embed.set_thumbnail(url="http://www.unixstickers.com/image/cache/data/stickers/dogecoin/Doge.sh-600x600.png")
        embed.add_field(name=":star2: Request about our Lord and Savior DOGE :star2:", value="Praise him !",
                        inline=False)
        embed.add_field(name=":information_source: Informations about DOGE", value=price)
        embed.add_field(name=":musical_note: Your Haiku :musical_note: ", value=choice)
        return embed

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
        price = "Price : " + "{0:.3f}".format(float(data[0]["price_usd"])) + "$"

        haiku1 = "Roses are red, Violet are blue.\n All in DOGE, he will never fail you."
        haiku2 = "Roses are red, Violet are blue.\n If you question DOGE, Burn will do you."
        haiku3 = "Roses are red, Violet are blue.\n With DOGE there is no such thing,\n as too much value"
        haiku4 = "Roses are red, Violet are blue.\n The only thing that matters,\n is DOGE revenue"
        haiku5 = "Once upon a time,\n A stranger entered the Pack.\n\n Dubbed and amazed,\n by the beautiful cryptospace, he asked\n'What coin should I invest? Target Sir?'\n\n Out of the blue,\n Our Saviour Mcgruff came through,\n He explained what we all knew:\n DOGE is our virtue "
        haiku6 = "Roses are red, Violet are blue.\n I can't really rhyme, But the Shibas are mine"
        haiku7 = "BTC, Ethereum, Litecoin or maybe even Ripple,\n It doesn't really matter.\n Compared to DOGE,\n Everything is cripple."
        haiku8 = "DOGE is love, DOGE is life,\n If you wanna make money, Better sell your wife."

        choice = random.choice([haiku1, haiku2, haiku3, haiku4, haiku5, haiku6, haiku7,haiku8])

        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com")
        embed.set_thumbnail(url="http://www.stickpng.com/assets/images/5845e770fb0b0755fa99d7f4.png")
        embed.add_field(name="Praise DOGE", value="")
        embed.add_field(name=":star2: Request about our Lord and Savior DOGE", value="", inline=False)
        embed.add_field(name=":information_source: Informations about DOGE", value="price")
        embed.add_field(name="::musical_note: Your Haiku : ", value=choice)
        return embed

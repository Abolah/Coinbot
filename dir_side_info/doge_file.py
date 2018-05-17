from random import randint
import datetime
import discord
import random
import requests


class Class_Doge:
    def __init__(self):
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        self.cmc_url = "https://api.coinmarketcap.com/v2/ticker/74/?convert=EUR"
        self.cmc_btc_url = "https://api.coinmarketcap.com/v2/ticker/74/?convert=BTC"
        return

    def function_display(self):
        r = requests.get(self.cmc_url)
        cmc_json = r.json()
        r_btc = requests.get(self.cmc_btc_url)
        btc_json = r_btc.json()
        price = "```css\n" + "Price : " + "${0:.3f}".format(float(cmc_json["data"]["quotes"]["USD"]["price"])) +" |  {0:.8f} BTC\n".format(float(btc_json["data"]["quotes"]["BTC"]["price"])) + "Target : Moon" + "```"

        haiku1 = "Roses are red, Violet are blue.\nAll IN DOGE, he will never fail you."
        haiku2 = "Roses are red, Violet are blue.\nIf you question DOGE, Burn will do you."
        haiku3 = "Roses are red, Violet are blue.\nWith DOGE there is no such thing,\nas too much value"
        haiku4 = "Roses are red, Violet are blue.\nThe only thing that matters,\nis DOGE revenue"
        haiku5 = "Once upon a time,\nA stranger entered the Pack.\n\nDubbed and amazed,\nby the beautiful cryptospace, he asked\n'What coin should I invest? Target Sir?'\n\nOut of the blue,\nOur Saviour McGruff came through,\nHe explained what we all knew:\nDOGE is our virtue "
        haiku6 = "Roses are red, Violet are blue.\nI can't really rhyme, but the Shibas are mine"
        haiku7 = "BTC, Ethereum, Litecoin or maybe even Ripple,\nIt doesn't really matter.\nCompared to DOGE,\nEverything is cripple."
        haiku8 = "DOGE is love, DOGE is life,\nIf you wanna make money, Better sell your wife."
        haiku9 = "Roses are red, Violet are blue.\nIf you don't like DOGE, F*CK YOU !"
        haiku10 = "Real Wolves from the Pack don’t howl at full moon.\nThey are heading to the moon.\nThey bought DOGE."
        haiku11 = "A Dogecoin a day,\nKeeps bankruptcy away."
        haiku12 = "A wise man once told,\n'God helps those who help themselves'\nGet God on your side.\nBuy DOGE and be wise."
        haiku13 = "When the markets get tough,\nThe toughs buy DOGE."
        haiku14 = "Swaggity Swooty,\nWolf's lofi is so shitty."

        choice = random.choice([haiku1, haiku2, haiku3, haiku4, haiku5, haiku6, haiku7, haiku8, haiku9, haiku10, haiku11, haiku12, haiku13, haiku14])
        choice = "```css\n" + choice + "```"

        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com")
        embed.set_thumbnail(url="http://www.unixstickers.com/image/cache/data/stickers/dogecoin/Doge.sh-600x600.png")
        embed.add_field(name=":star2: Our Lord and Savior DOGE :star2:", value="Praise him !",
                        inline=False)
        embed.add_field(name=":information_source: Informations about DOGE", value=price)
        embed.add_field(name=":musical_note: Your Haiku :musical_note: ", value=choice)
        return embed

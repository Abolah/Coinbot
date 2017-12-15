import datetime
import discord
from random import randint


class Wolf:
    def __init__(self):
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        return

    def affichage(self):
        url_logo = "https://files.coinmarketcap.com/static/img/coins/32x32/bitcoin.png"
        wolf_knowledge = "+ Full access to the channels where The Wolf himself  will come and share some knowledge !\n\n"
        ico_sales = "+ Access to selected Pre-ICO sales where the analysts  picks ICOs with great potential and great pre-sales bonuses !\n\n"
        group = "+ You'll be part of a group focused on learning and empowering the members !\n"
        videos = "+ Access to today markets learning videos\n"
        wolf_trade = "+ Access to Wolf's trades and questions\n"
        news = "+ News and Catalyst\n"
        talks = "+ Various Discussions about pretty much anything\n"
        education = "+ Educations channels\n"
        tech_analysis = "+ TA run by Masons Team\n"
        leverage = "+ Leverage Trading run by Crypto_Core\n"
        fun = "+ The Traderholics channels\n"
        spoonfed = "Blind calls and pump/dump calls\n"
        Howling = "AI-Powered crypto-signals bot\n"
        Trader_bot = "# High-End automated, algorithmic trading bot\n"
        get_vip = "https://wolf.foundation/user/dashboard \n"
        price = "0.025 BTC | ~$400"

        Discord_perks = "```diff\n" + wolf_knowledge + ico_sales + group + "```"
        More_perks = "```diff\n" + videos + wolf_trade + news + talks + education + tech_analysis + leverage + fun + "```"
        NoGo = "```diff\n" + "- " + spoonfed + "```"
        later = "```md\n" + "# " + Howling + Trader_bot + "```"
        pay = "```css\n" + get_vip + "The price is currently at : " + price + "```"

        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com", timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.set_thumbnail(url=url_logo)
        embed.add_field(name=":first_place: : Do you know what you can have by becoming a VIP ?", value="Here are all the advantages !", inline=False)
        embed.add_field(name=":slot_machine: Discord Advantages : \n", value=Discord_perks, inline=True)
        embed.add_field(name=":slot_machine: More Advantages !", value=More_perks, inline=True)
        embed.add_field(name=":track_next: Whats coming next ?  :track_next:", value=later, inline=True)
        embed.add_field(name=":head_bandage: What you won't have.", value=NoGo, inline=True)
        embed.add_field(name=":moneybag: Wanna enter the Pack ? Copy the URL below !  :moneybag:", value=pay, inline=True)
        embed.set_footer(text="Request achieved on")
        return embed

    async def get_wolf(self):
        embed = self.affichage
        return embed

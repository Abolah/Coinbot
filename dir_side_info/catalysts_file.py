import discord
from pymarketcap import Pymarketcap
import datetime
from random import randint
import requests


class Class_Catalysts:
    def __init__(self, auth):
        self.auth = str(auth).split("#")
        self.auth = self.auth[0]
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        self.cmcal_default = "https://api.coinmarketcal.com/v1/events?access_token={}&page=1&max=5"
        self.grant_type = "client_credentials"
        self.client_id = ""
        self.client_secret = ""
        self.access_token = ""
        self.id_coin = ""
        self.event_type = ""
        self.events = ""
        return

    def function_accesstoken(self):
        access_url = "https://api.coinmarketcal.com/oauth/v2/token?grant_type={}&client_id={}&client_secret={}".format(
            self.grant_type, self.client_id, self.client_secret)
        r = requests.get(access_url)
        data_json = r.json()
        token = data_json["access_token"]
        self.access_token = token

    def function_cmc(self, coin):
        if coin == "":
            id_coin = ""
        else:
            coin = coin.upper()
            coinmarketcap = Pymarketcap()
            cmc_json = coinmarketcap.ticker(coin)
            id_coin = cmc_json["data"]["website_slug"]
        self.id_coin = id_coin
        return id_coin

    def function_cmcal(self, id_coin, event_type):
        if event_type == "" and id_coin == "":
            cmcal_url = self.cmcal_default.format(self.access_token)
        elif id_coin == "":
            cmcal_url = "https://api.coinmarketcal.com/v1/events?access_token={}&page=1&max=5&categories={}".format(
                self.access_token, event_type)
        elif event_type == "":
            cmcal_url = "https://api.coinmarketcal.com/v1/events?access_token={}&page=1&max=5&coins={}".format(
                self.access_token, id_coin)
        else:
            cmcal_url = "https://api.coinmarketcal.com/v1/events?access_token={}&page=1&max=5&coins={}&categories={}".format(
                self.access_token, id_coin, event_type)
        r = requests.get(cmcal_url)
        data_json = r.json()
        if "error" not in data_json:
            event = ""
            for i in data_json:
                title = str(i["title"])
                coin_name = str(i["coins"][0]["symbol"])
                date_event = str(i["date_event"])
                date = date_event.split("T")
                date = date[0]
                desc = str(i["description"])
                cat = str(i["categories"][0]["name"])
                event += "[" + coin_name + "] [" + date + "]" + " " + "[" + cat + "]" + "\n[" + title + "] \n" + desc + "\n\n"
            self.events = "```css\n" + event + "```"
        else:
            self.function_accesstoken()
            self.function_cmcal(self.id_coin, self.event_type)

    def function_display(self):
        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/984423152116781056/Z9MUJT_7_400x400.jpg")
        embed.add_field(name=":floppy_disk: Information about the incoming events", value=self.events, inline=True)
        embed.add_field(name="Data retrieved with :heart: from : ", value="```py\nCoinmarketcal.com\n```", inline=False)
        embed.set_footer(text="Request achieved :")
        return embed

    def get_catalysts(self, coin, event_type):
        self.event_type = event_type
        get_coin = self.function_cmc(coin)
        self.function_cmcal(get_coin, event_type)
        embed = self.function_display()
        return embed

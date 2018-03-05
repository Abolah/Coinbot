import datetime
import discord
from random import randint
import requests


class Class_Balance:
    def __init__(self, auth):
        self.auth = str(auth).split("#")
        self.auth = self.auth[0]
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        self.default_print = "Default Print"
        self.btc_blockchain_url = "https://blockchain.info/q/addressbalance/{}"
        self.eth_blockchain_url = "https://api.etherscan.io/api?module=account&action=balance&address={}&tag=latest&apikey={}"
        self.etherscan_api_key = ""
        self.address = "None"
        self.coin = "None"
        self.eth_balance = "None"
        self.btc_balance = "None"
        self.error = "None"
        return

    def function_getbalance_eth(self):
        url = self.eth_blockchain_url.format(self.address,self.etherscan_api_key)
        r = requests.get(url)
        eth_value = r.json()
        value = int(eth_value["result"])
        eth_value = value/1000000000000000000
        self.eth_balance = "```\nYour address : {}\n\nYou have {} ETH in your wallet.\n```".format(self.address, eth_value)

    def function_getbalance_btc(self):
        url = self.btc_blockchain_url.format(self.address)
        r = requests.get(url)
        btc_value = r.json()
        btc_value = btc_value/100000000
        print(btc_value)
        self.btc_balance = "```\nYour address : {}\n\nYou have {} BTC in your wallet.\n```".format(self.address, btc_value)

    def function_display(self):
        if self.coin == "eth":
            url_logo = "https://s2.coinmarketcap.com/static/img/coins/32x32/1027.png"
        elif self.coin == "btc":
            url_logo = "https://s2.coinmarketcap.com/static/img/coins/32x32/1.png"
        else:
            url_logo = ""
        display = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com", timestamp=datetime.datetime.utcfromtimestamp(self.time))
        display.set_thumbnail(url=url_logo)
        display.set_footer(text="Request achieved :")
        display.add_field(name=":star2: Request about your wallet", value="Here are the informations I could retrieve " + self.auth, inline=False)
        if self.coin == "eth":
            display.add_field(name="ETH wallet", value=self.eth_balance, inline=True)
        elif self.coin == "btc":
            display.add_field(name="BTC wallet", value=self.btc_balance, inline=False)
        else:
            display.add_field(name="Something went wrong", value=self.error, inline=False)
        return display

    async def balance(self, coin, address):
        self.coin = coin.lower()
        if self.coin == "eth":
            self.address = address.lower()
            self.function_getbalance_eth()
            embed = self.function_display()
        elif self.coin == "btc":
            self.address = address
            self.function_getbalance_btc()
            embed = self.function_display()
        else:
            self.error = "```css\nCoin Error. Only ETH and BTC are supported currently.\n```"
            embed = self.function_display()
        return embed

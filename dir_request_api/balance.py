import datetime
import discord
from random import randint
import requests
from pymarketcap import Pymarketcap


class Class_Balance:
    def __init__(self, auth):
        self.auth = str(auth).split("#")
        self.auth = self.auth[0]
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        self.default_print = "Default Print"
        self.btc_blockchain_url = "https://blockchain.info/q/addressbalance/{}"
        self.eth_blockchain_url = "https://api.etherscan.io/api?module=account&action=balance&address={}&tag=latest&apikey={}"
        self.ethplorer_api_url = "https://api.ethplorer.io/getAddressInfo/{}?apiKey=freekey"
        self.etherscan_api_key = ""
        self.price_btc = "None"
        self.price_usd = "None"
        self.price_eur = "None"
        self.address = "None"
        self.coin = "None"
        self.eth_balance = "None"
        self.btc_balance = "None"
        self.tokens = "None"
        self.error = "Your Balance equals 0"
        return

    def function_cmc(self, coin):
        self.coin = coin.upper()
        coinmarketcap = Pymarketcap()
        cmc_json = coinmarketcap.ticker(self.coin, convert="EUR")
        btc_json = coinmarketcap.ticker(self.coin, convert="BTC")

        self.price_usd = float(cmc_json["data"]["quotes"]["USD"]["price"])
        self.price_eur = float(cmc_json["data"]["quotes"]["EUR"]["price"])
        self.price_btc = float(btc_json["data"]["quotes"]["BTC"]["price"])
        return

    def function_getbalance_eth(self):
        self.coin = self.coin.lower()
        url = self.eth_blockchain_url.format(self.address, self.etherscan_api_key)
        r = requests.get(url)
        eth_value = r.json()
        value = float(eth_value["result"])
        eth_value = float(value / 1000000000000000000)
        total_usd = float(self.price_usd) * eth_value
        total_btc = float(self.price_btc) * eth_value
        total_eur = float(self.price_eur) * eth_value
        self.eth_balance = "```css\nYour address:\n{}\n\nYou have {} ETH in your wallet.\nYour wallet's value is:\n{} BTC\n$ {}\n{} €.\n```".format(
            self.address, eth_value, total_btc, total_usd, total_eur)
        return

    def function_getbalance_btc(self):
        self.coin = self.coin.lower()
        url = self.btc_blockchain_url.format(self.address)
        r = requests.get(url)
        btc_value = r.json()
        btc_value = btc_value / 100000000
        total_usd = float(self.price_usd) * btc_value
        total_btc = float(self.price_btc) * btc_value
        total_eur = float(self.price_eur) * btc_value
        self.btc_balance = "```css\nYour address:\n{}\n\nYou have {} BTC in your wallet.\nYour wallet's value is:\n{} BTC\n$ {}\n{} €.\n```".format(self.address, btc_value, total_btc, total_usd, total_eur)
        return

    def function_get_token(self):
        url = self.ethplorer_api_url.format(self.address)
        r = requests.get(url)
        tokens_data = r.json()
        data = tokens_data["tokens"]
        tokens_list = []
        for i in data:
            value = int(i["balance"])
            balance = value / 1000000000000000000
            name = i["tokenInfo"]["name"]
            token = "Tkn: {}\nQty: {}\n".format(name, str(balance))
            tokens_list.append(token)
        self.tokens = ''.join(tokens_list)
        self.tokens = "```css\n" + self.tokens + "```"
        return

    def function_display(self):
        if self.coin == "eth" or self.coin == "token":
            url_logo = "https://s2.coinmarketcap.com/static/img/coins/32x32/1027.png"
        elif self.coin == "btc":
            url_logo = "https://s2.coinmarketcap.com/static/img/coins/32x32/1.png"
        else:
            url_logo = ""
        display = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                                timestamp=datetime.datetime.utcfromtimestamp(self.time))
        display.set_thumbnail(url=url_logo)
        if self.coin == "eth":
            display.add_field(name="ETH wallet", value=self.eth_balance, inline=True)
        elif self.coin == "btc":
            display.add_field(name="BTC wallet", value=self.btc_balance, inline=False)
        elif self.coin == "token":
            display.add_field(name="Tokens in your wallet", value=self.tokens, inline=True)
        else:
            display.add_field(name="Something went wrong", value=self.error, inline=False)
        return display

    async def balance(self, coin, address):
        self.coin = coin.lower()
        if self.coin == "eth":
            self.function_cmc(coin)
            self.address = address.lower()
            self.function_getbalance_eth()
            embed = self.function_display()
        elif self.coin == "btc":
            self.function_cmc(coin)
            self.address = address
            self.function_getbalance_btc()
            embed = self.function_display()
        elif self.coin == "token":
            self.address = address
            self.function_get_token()
            embed = self.function_display()
        else:
            self.error = "```css\nCoin Error. Only ETH and BTC are supported currently.\n```"
            embed = self.function_display()
        return embed

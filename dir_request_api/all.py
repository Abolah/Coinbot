import datetime
from random import randint
import discord
from pymarketcap import Pymarketcap
import requests


class Class_All:
    def __init__(self, auth):
        self.auth = str(auth).split("#")
        self.auth = self.auth[0]
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        self.name = "None"
        self.bitfinex_api_url_btc = "https://api.bitfinex.com/v1/pubticker/{}btc"
        self.bitfinex_api_url_usdt = "https://api.bitfinex.com/v1/pubticker/btcusd"
        self.bittrex_api_url_btc = "https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-{}"
        self.bittrex_api_url_usdt = "https://bittrex.com/api/v1.1/public/getmarketsummary?market=usdt-{}"
        self.binance_api_url_usdt = "https://www.binance.com/api/v1/ticker/24hr?symbol={}USDT"
        self.binance_api_url_btc = "https://www.binance.com/api/v1/ticker/24hr?symbol={}BTC"
        self.cryptopia_api_url_btc = "https://www.cryptopia.co.nz/api/GetMarket/{}_BTC"
        self.cryptopia_api_url_usdt = "https://www.cryptopia.co.nz/api/GetMarket/{}_USDT"
        self.hitbtc_api_url_btc = "https://api.hitbtc.com/api/2/public/ticker/{}BTC"
        self.hitbtc_api_url_usdt = "https://api.hitbtc.com/api/2/public/ticker/{}USD"
        self.poloniex_api_url = "https://poloniex.com/public?command=returnTicker"
        self.key = "None"
        self.pair = "None"
        return

    async def function_cmc(self, coin):
        global cmc_json, ticker
        coin = coin.upper()
        coinmarketcap = Pymarketcap()
        cmc_json = coinmarketcap.ticker(coin, convert="EUR")
        rank = str("Rank : [Rank " + str(cmc_json["rank"]) + "]\n")
        marketcap = str("MC : " + "$ " + "{:,}".format(float(cmc_json["market_cap_usd"])) + "\n")
        price = str("Price : " + "$" + "{0:.3f}".format(float(cmc_json["price_usd"])) + " | " + "{0:.3f}".format(
            float(cmc_json["price_eur"])) + "€      \n")
        change_1 = str("1h Swing : " + str(cmc_json["percent_change_1h"]) + "%\n")
        change_24 = str("24h Swing : " + str(cmc_json["percent_change_24h"]) + "%\n")
        change_7 = str("7 days Swing : " + str(cmc_json["percent_change_7d"]) + "%\n")
        value_mc = "```css\n" + rank + marketcap + price + change_1 + change_24 + change_7 + "```"

        self.name = cmc_json["name"]
        return value_mc

    async def function_bitfinex(self, coin):
        global bitfinex_json, value_annex
        if coin == "btc":
            api_url = self.bitfinex_api_url_usdt
        else:
            api_url = self.bitfinex_api_url_btc.format(coin)
        r = requests.get(api_url)
        bitfinex_json = r.json()
        if coin == "btc":
            pair = "Pair : USDT-" + coin.upper() + "\n"
            last = "Last : " + "{0:.2f}".format(float(bitfinex_json["last_price"])) + "\n"
            bid = "Bid : " + "{0:.2f}".format(float(bitfinex_json["bid"])) + "\n"
            ask = "Ask : " + "{0:.2f}".format(float(bitfinex_json["ask"])) + "\n"
            volume = "Volume : " + "{0:.2f}".format(float(bitfinex_json["volume"])) + " BTC" + "\n"
            high = "High : " + "{0:.8f}".format(float(bitfinex_json["low"])) + "\n"
            low = "Low : " + "{0:.8f}".format(float(bitfinex_json["high"])) + "\n"
            value_finex = "```css\n" + pair + volume + last + bid + ask + high + low + "```"
        else:
            pair = "Pair : BTC-" + coin.upper() + "\n"
            last = "Last : " + "{0:.8f}".format(float(bitfinex_json["last_price"])) + "\n"
            bid = "Bid : " + "{0:.8f}".format(float(bitfinex_json["bid"])) + "\n"
            ask = "Ask : " + "{0:.8f}".format(float(bitfinex_json["ask"])) + "\n\n"
            volume = "Volume : " + "{0:.2f}".format(float(bitfinex_json["volume"])) + " BTC" + "\n"
            high = "High : " + "{0:.8f}".format(float(bitfinex_json["low"])) + "\n"
            low = "Low : " + "{0:.8f}".format(float(bitfinex_json["high"])) + "\n"
            value_finex = "```css\n" + pair + volume + last + bid + ask + high + low + "```"

        return value_finex

    async def function_bittrex(self, coin):
        if coin == "btc":
            api_url = self.bittrex_api_url_usdt.format(coin)
        else:
            api_url = self.bittrex_api_url_btc.format(coin)

        r = requests.get(api_url)
        bittrex_json = r.json()
        if coin == "btc":
            name = "Pair :" + str(bittrex_json["result"][0]["MarketName"]) + "\n"
            volume = "Volume : " + "{0:.2f}".format(bittrex_json["result"][0]["BaseVolume"]) + " BTC" + "\n"
            last = "Last : " + "{0:.2f}".format(bittrex_json["result"][0]["Last"]) + "\n"
            bid = "Bid : " + "{0:.2f}".format(bittrex_json["result"][0]["Bid"]) + "\n"
            ask = "Ask : " + "{0:.2f}".format(bittrex_json["result"][0]["Ask"]) + "\n"
            low = "1d Low : " + "{0:.2f}".format(bittrex_json["result"][0]["Low"]) + "\n"
            high = "1d High : " + "{0:.2f}".format(bittrex_json["result"][0]["High"]) + "\n"
            value_rex = "```css\n" + name + volume + last + bid + ask + high + low + "```"
        else:
            name = "Pair :" + str(bittrex_json["result"][0]["MarketName"]) + "\n"
            volume = "Volume : " + "{0:.2f}".format(bittrex_json["result"][0]["BaseVolume"]) + " BTC" + "\n"
            last = "Last : " + "{0:.8f}".format(bittrex_json["result"][0]["Last"]) + "\n"
            bid = "Bid : " + "{0:.8f}".format(bittrex_json["result"][0]["Bid"]) + "\n"
            ask = "Ask : " + "{0:.8f}".format(bittrex_json["result"][0]["Ask"]) + "\n"
            low = "1d Low : " + "{0:.8f}".format(bittrex_json["result"][0]["Low"]) + "\n"
            high = "1d High : " + "{0:.8f}".format(bittrex_json["result"][0]["High"]) + "\n"
            value_rex = "```css\n" + name + volume + last + bid + ask + high + low + "```"

        return value_rex

    async def function_binance(self, coin):
        coin = coin.upper()
        if coin == "BTC":
            api_url = self.binance_api_url_usdt.format(coin)
        else:
            api_url = self.binance_api_url_btc.format(coin)

        r = requests.get(api_url)
        binance_json = r.json()

        if coin == "BTC":
            pair = "Pair : USDT-" + coin + "\n"
            last = "Last : " + "{0:.2f}".format(float(binance_json["lastPrice"])) + "\n"
            bid = "Bid : " + "{0:.2f}".format(float(binance_json["bidPrice"])) + "\n"
            ask = "Ask : " + "{0:.2f}".format(float(binance_json["askPrice"])) + "\n"
            volume = "Volume : " + "{0:.2f}".format(float(binance_json["quoteVolume"])) + " BTC" + "\n"
            high = "24 High : " + binance_json["highPrice"] + "\n"
            low = "24 Low : " + binance_json["lowPrice"] + "\n"
            value_bin = "```css\n" + pair + volume + last + bid + ask + high + low + "```"
        else:
            pair = "Pair : BTC-" + coin + "\n"
            last = "Last : " + "{0:.8f}".format(float(binance_json["lastPrice"])) + "\n"
            bid = "Bid : " + "{0:.8f}".format(float(binance_json["bidPrice"])) + "\n"
            ask = "Ask : " + "{0:.8f}".format(float(binance_json["askPrice"])) + "\n"
            volume = "Volume : " + "{0:.2f}".format(float(binance_json["quoteVolume"])) + " BTC" + "\n"
            high = "1d High : " + binance_json["highPrice"] + "\n"
            low = "1d Low : " + binance_json["lowPrice"] + "\n"
            value_bin = "```css\n" + pair + volume + last + bid + ask + high + low + "```"

        return value_bin

    async def function_cryptopia(self, coin):
        coin = coin.upper()
        if coin == "BTC":
            api_url = self.cryptopia_api_url_usdt.format(coin)
        else:
            api_url = self.cryptopia_api_url_btc.format(coin)

        r = requests.get(api_url)
        topia_json = r.json()

        if coin == "BTC":
            pair = "Pair : BTC-" + coin + "\n"
            last = "Last : " + "{0:.2f}".format(topia_json["Data"]["LastPrice"]) + "\n"
            bid = "Bid : " + "{0:.2f}".format(topia_json["Data"]["BidPrice"]) + "\n"
            ask = "Ask : " + "{0:.2f}".format(topia_json["Data"]["AskPrice"]) + "\n"
            volume = "Volume : " + "{0:.2f}".format(topia_json["Data"]["BaseVolume"]) + " BTC" + "\n"
            high = "24 High : " + "{0:.8f}".format(topia_json["Data"]["High"]) + "\n"
            low = "24 Low : " + "{0:.8f}".format(topia_json["Data"]["Low"]) + "\n"
            value_topia = "```css\n" + pair + volume + last + bid + ask + high + low + "```"
        else:
            pair = "Pair : BTC-" + coin + "\n"
            last = "Last : " + "{0:.8f}".format(topia_json["Data"]["LastPrice"]) + "\n"
            bid = "Bid : " + "{0:.8f}".format(topia_json["Data"]["BidPrice"]) + "\n"
            ask = "Ask : " + "{0:.8f}".format(topia_json["Data"]["AskPrice"]) + "\n"
            volume = "Volume : " + "{0:.2f}".format(topia_json["Data"]["BaseVolume"]) + " BTC" + "\n"
            high = "24 High : " + "{0:.8f}".format(topia_json["Data"]["High"]) + "\n"
            low = "24 Low : " + "{0:.8f}".format(topia_json["Data"]["Low"]) + "\n"
            value_topia = "```css\n" + pair + volume + last + bid + ask + high + low + "```"

        return value_topia

    async def function_hitbtc(self, coin):
        coin = coin.upper()
        if coin == "BTC":
            api_url = self.hitbtc_api_url_usdt.format(coin)
        else:
            api_url = self.hitbtc_api_url_btc.format(coin)

        r = requests.get(api_url)
        hitbtc_json = r.json()

        if coin == "BTC":
            pair = "Pair : BTC-" + coin + "\n"
            last = "Last : " + "{0:.2}".format(hitbtc_json["last"]) + "\n"
            bid = "Bid : " + "{0:.2}".format(hitbtc_json["bid"]) + "\n"
            ask = "Ask : " + "{0:.2}".format(hitbtc_json["ask"]) + "\n"
            volume = "Volume : " + "{0:.2}".format(hitbtc_json["volumeQuote"]) + " BTC" + "\n"
            high = "24 High : " + "{0:.8}".format(hitbtc_json["high"]) + "\n"
            low = "24 Low : " + "{0:.8}".format(hitbtc_json["low"]) + "\n"
            value_hitbtc = "```css\n" + pair + volume + last + bid + ask + high + low + "```"
        else:
            pair = "Pair : BTC-" + coin + "\n"
            last = "Last : " + "{0:.8}".format(hitbtc_json["last"]) + "\n"
            bid = "Bid : " + "{0:.8}".format(hitbtc_json["bid"]) + "\n"
            ask = "Ask : " + "{0:.8}".format(hitbtc_json["ask"]) + "\n"
            volume = "Volume : " + "{0:.2}".format(hitbtc_json["volumeQuote"]) + " BTC" + "\n"
            high = "24 High : " + "{0:.8}".format(hitbtc_json["high"]) + "\n"
            low = "24 Low : " + "{0:.8}".format(hitbtc_json["low"]) + "\n"
            value_hitbtc = "```css\n" + pair + volume + last + bid + ask + high + low + "```"

        return value_hitbtc

    async def function_poloniex(self, coin):
        if coin.upper() == "BTC":
            self.pair = coin + "_USDT"
            self.key = "USDT_BTC"
        else:
            self.pair = coin + "_BTC"
            self.key = "BTC_" + coin.upper()

        api_url = self.poloniex_api_url
        r = requests.get(api_url)
        poloniex_json = r.json()

        if coin == "BTC":

            pair = "Pair :" + self.key.replace("_", "-") + "\n"
            last = "Last : " + "{0:.2f}".format(float(poloniex_json[self.key]["last"])) + "\n"
            bid = "Bid : " + "{0:.2f}".format(float(poloniex_json[self.key]["highestBid"])) + "\n"
            ask = "Ask : " + "{0:.2f}".format(float(poloniex_json[self.key]["lowestAsk"])) + "\n"
            volume = "Volume : " + "{0:.2f}".format(float(poloniex_json[self.key]["baseVolume"])) + " BTC" + "\n"
            high = "1d High : " + poloniex_json[self.key]["high24hr"] + "\n"
            low = "1d Low : " + poloniex_json[self.key]["low24hr"] + "\n"
            value_polo = "```css\n" + pair + volume + last + bid + ask + high + low + "```"
        else:
            pair = "Pair :" + self.key.replace("_", "-") + "\n"
            last = "Last : " + poloniex_json[self.key]["last"] + "\n"
            bid = "Bid : " + poloniex_json[self.key]["highestBid"] + "\n"
            ask = "Ask : " + poloniex_json[self.key]["lowestAsk"] + "\n"
            volume = "Volume : " + "{0:.2f}".format(float(poloniex_json[self.key]["baseVolume"])) + " BTC" + "\n"
            high = "1d High : " + poloniex_json[self.key]["high24hr"] + "\n"
            low = "1d Low : " + poloniex_json[self.key]["low24hr"] + "\n"
            value_polo = "```css\n" + pair + volume + last + bid + ask + high + low + "```"

        return value_polo

    def function_display(self, cmc_value, bitfinex_value, bittrex_value, binance_value, cryptopia_value, hitbtc_value,
                         poloniex_value):
        name_logo = self.name.replace(" ", "-").lower()
        url_logo = "https://files.coinmarketcap.com/static/img/coins/32x32/" + name_logo + ".png"

        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.add_field(name=":star2: Request achieved about " + self.name,
                        value="Here are the informations I could retrieve " + self.auth, inline=False)
        embed.set_thumbnail(url=url_logo)
        embed.add_field(name=":medal: CoinMarketCap Informations", value=cmc_value, inline=False)
        embed.add_field(name=":fleur_de_lis: Bitfinex Informations", value=bitfinex_value, inline=True)
        embed.add_field(name=":dragon: Bittrex Informations", value=bittrex_value, inline=True)
        embed.add_field(name=":game_die: Binance Informations", value=binance_value, inline=True)
        embed.add_field(name=":space_invader: Cryptopia Informations", value=cryptopia_value, inline=True)
        embed.add_field(name=":octopus: HitBTC Informations", value=hitbtc_value, inline=True)
        embed.add_field(name=":crystal_ball: Poloniex Informations", value=poloniex_value, inline=True)
        embed.set_footer(text="Request achieved :")

        return embed

    async def all(self, coin):

        cmc_value = await self.function_cmc(coin)
        bitfinex_value = await self.function_bitfinex(coin)
        bittrex_value = await self.function_bittrex(coin)
        binance_value = await self.function_binance(coin)
        cryptopia_value = await self.function_cryptopia(coin)
        hitbtc_value = await self.function_hitbtc(coin)
        poloniex_value = await self.function_poloniex(coin)
        embed = self.function_display(cmc_value, bitfinex_value, bittrex_value, binance_value, cryptopia_value,
                                      hitbtc_value, poloniex_value)
        return embed

import datetime
from random import randint
import discord
import requests
from pymarketcap import Pymarketcap


class Class_All:
    def __init__(self, auth):
        self.auth = str(auth).split("#")
        self.auth = self.auth[0]
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        self.name = "None"
        self.bitfinex_api_url_btc = "https://api.bitfinex.com/v1/pubticker/{}btc"
        self.bitfinex_api_url_usdt = "https://api.bitfinex.com/v1/pubticker/btcusd"
        self.bitfinex_url_status = "https://api.bitfinex.com/v2/platform/status"
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
        global cmc_json
        if coin == "iota":
            coin = "miota"
        coin = coin.upper()
        coinmarketcap = Pymarketcap(timeout=10)
        try:
            cmc_json = coinmarketcap.ticker(coin, convert="EUR")
            self.name = cmc_json["data"]["name"]
            rank = str("Rank : [Rank " + str(cmc_json["data"]["rank"]) + "]\n")
            if cmc_json["data"]["market_cap_usd"] is None:
                marketcap = "MarketCap : Unknown\n"
            else:
                marketcap = str("MC : " + "$" + "{:,}".format(float(cmc_json["data"]["market_cap_usd"])) + "\n")

            price = str("Price : ${0:.3f}".format(float(cmc_json["data"]["price_usd"])) + " | {0:.3f}€\n".format(
                float(cmc_json["data"]["price_eur"])))
            if cmc_json["data"]["percent_change_1h"] is None:
                change_1 = "1h Swing : Unknown\n"
            else:
                change_1 = str("1h Swing : " + str(cmc_json["data"]["percent_change_1h"]) + "%\n")
            if cmc_json["data"]["percent_change_24h"] is None:
                change_24 = "24h Swing : Unknown\n"
            else:
                change_24 = str("24h Swing : " + str(cmc_json["data"]["percent_change_24h"]) + "%\n")
            if cmc_json["data"]["percent_change_7d"] is None:
                change_7 = "7 days Swing : Unknown\n"
            else:
                change_7 = str("7 days Swing : " + str(cmc_json["data"]["percent_change_7d"]) + "%\n")
            value_mc = "```css\n" + rank + marketcap + price + change_1 + change_24 + change_7 + "```"
        except KeyError:
            value_mc = "```css\nThis ticker does not exist on Coinmarketcap.\nMaybe you made a typo in the coin's ticker.```"

        return value_mc

    async def function_bitfinex(self, coin):
        if coin == "iota" or coin == "miota":
            coin = "iot"
            api_url = self.bitfinex_api_url_btc.format(coin)
        elif coin == "btc":
            api_url = self.bitfinex_api_url_usdt
        else:
            api_url = self.bitfinex_api_url_btc.format(coin)
        r = requests.get(api_url)
        bitfinex_json = r.json()

        if "message" not in bitfinex_json:
            if coin == "btc":
                pair = "Pair : USDT-" + coin.upper() + "\n"
                if bitfinex_json["last_price"] is None:
                    last = "Last : Unknown\n"
                else:
                    last = "Last : {}\n".format(float(bitfinex_json["last_price"]))
                if bitfinex_json["bid"] is None:
                    bid = "Bid : Unknown\n"
                else:
                    bid = "Bid : {}\n".format(float(bitfinex_json["bid"]))
                if bitfinex_json["ask"] is None:
                    ask = "Ask : Unknown\n"
                else:
                    ask = "Ask : {}\n".format(float(bitfinex_json["ask"]))
                if bitfinex_json["volume"] is None:
                    volume = "Volume : Unknown\n"
                else:
                    volume = "Volume : {} BTC\n".format(float(bitfinex_json["volume"]))
                if bitfinex_json["high"] is None:
                    high = "1d High : Unknown\n"
                else:
                    high = "1d High : {}\n".format(float(bitfinex_json["high"]))
                if bitfinex_json["low"] is None:
                    low = "1d Low : Unknown\n"
                else:
                    low = "1d Low : {}\n".format(float(bitfinex_json["low"]))
                value_finex = "```css\n" + pair + volume + last + bid + ask + high + low + "```"
            else:
                pair = "Pair : BTC-" + coin.upper() + "\n"
                if bitfinex_json["last_price"] is None:
                    last = "Last : Unknown\n"
                else:
                    last = "Last : {}\n".format(float(bitfinex_json["last_price"]))
                if bitfinex_json["bid"] is None:
                    bid = "Bid : Unknown\n"
                else:
                    bid = "Bid : {}\n".format(float(bitfinex_json["bid"]))
                if bitfinex_json["ask"] is None:
                    ask = "Ask : Unknown\n"
                else:
                    ask = "Ask : {}\n".format(float(bitfinex_json["ask"]))
                if bitfinex_json["volume"] is None:
                    volume = "Volume : Unknown\n"
                else:
                    volume = "Volume : {} BTC\n".format(float(bitfinex_json["volume"]))
                if bitfinex_json["high"] is None:
                    high = "1d High : Unknown\n"
                else:
                    high = "1d High : {}\n".format(float(bitfinex_json["high"]))
                if bitfinex_json["low"] is None:
                    low = "1d Low : Unknown\n"
                else:
                    low = "1d Low : {}\n".format(float(bitfinex_json["low"]))
                value_finex = "```css\n" + pair + volume + last + bid + ask + high + low + "```"
        else:
            value_finex = "```css\n{} is not listed on Bitfinex.\n```".format(self.name)

        return value_finex

    async def function_bittrex(self, coin):
        if coin == "btc":
            api_url = self.bittrex_api_url_usdt.format(coin)
        else:
            api_url = self.bittrex_api_url_btc.format(coin)
        r = requests.get(api_url)
        bittrex_json = r.json()

        if "INVALID_MARKET" not in bittrex_json["message"]:
            if coin == "btc":
                pair = "Pair : USDT-" + coin.upper() + "\n"
                if bittrex_json["result"][0]["Volume"] is None:
                    volume = "Volume : Unknown\n"
                else:
                    volume = "Volume : {} BTC\n".format(bittrex_json["result"][0]["Volume"])
                if bittrex_json["result"][0]["Last"] is None:
                    last = "Last : Unknown\n"
                else:
                    last = "Last : {}\n".format(bittrex_json["result"][0]["Last"])
                if bittrex_json["result"][0]["Bid"] is None:
                    bid = "Bid : Unknown\n"
                else:
                    bid = "Bid : {}\n".format(bittrex_json["result"][0]["Bid"])
                if bittrex_json["result"][0]["Ask"] is None:
                    ask = "Ask : Unknown\n"
                else:
                    ask = "Ask : {}\n".format(bittrex_json["result"][0]["Ask"])
                if bittrex_json["result"][0]["Low"] is None:
                    low = "1d Low : Unknown\n"
                else:
                    low = "1d Low : {}\n".format(bittrex_json["result"][0]["Low"])
                if bittrex_json["result"][0]["High"] is None:
                    high = "1d High : Unknown\n"
                else:
                    high = "1d High : {}\n".format(bittrex_json["result"][0]["High"])
                value_rex = "```css\n" + pair + volume + last + bid + ask + high + low + "```"
            else:
                pair = "Pair : BTC-" + coin.upper() + "\n"
                if bittrex_json["result"][0]["Volume"] is None:
                    volume = "Volume : Unknown\n"
                else:
                    volume = "Volume : {} BTC\n".format(bittrex_json["result"][0]["Volume"])
                if bittrex_json["result"][0]["Last"] is None:
                    last = "Last : Unknown\n"
                else:
                    last = "Last : {}\n".format(bittrex_json["result"][0]["Last"])
                if bittrex_json["result"][0]["Bid"] is None:
                    bid = "Bid : Unknown\n"
                else:
                    bid = "Bid : {}\n".format(bittrex_json["result"][0]["Bid"])
                if bittrex_json["result"][0]["Ask"] is None:
                    ask = "Ask : Unknown\n"
                else:
                    ask = "Ask : {}\n".format(bittrex_json["result"][0]["Ask"])
                if bittrex_json["result"][0]["Low"] is None:
                    low = "1d Low : Unknown\n"
                else:
                    low = "1d Low : {}\n".format(bittrex_json["result"][0]["Low"])
                if bittrex_json["result"][0]["High"] is None:
                    high = "1d High : Unknown\n"
                else:
                    high = "1d High : {}\n".format(bittrex_json["result"][0]["High"])
                value_rex = "```css\n" + pair + volume + last + bid + ask + high + low + "```"
        else:
            value_rex = "```css\n{} is not listed on Bittrex. ```".format(self.name)
        return value_rex

    async def function_binance(self, coin):
        coin = coin.upper()
        if coin == "MIOTA":
            coin = "IOTA"
            api_url = self.binance_api_url_btc.format(coin)
        elif coin == "BTC":
            api_url = self.binance_api_url_usdt.format(coin)
        else:
            api_url = self.binance_api_url_btc.format(coin)
        r = requests.get(api_url)
        binance_json = r.json()

        if "msg" not in binance_json:
            if coin == "BTC":
                pair = "Pair : USDT-" + coin + "\n"
                if binance_json["lastPrice"] is None:
                    last = "Last : Unknown\n"
                else:
                    last = "Last : {}\n".format(float(binance_json["lastPrice"]))
                if binance_json["bidPrice"] is None:
                    bid = "Bid : Unknown\n"
                else:
                    bid = "Bid : {}\n".format(float(binance_json["bidPrice"]))
                if binance_json["askPrice"] is None:
                    ask = "Ask : Unknown\n"
                else:
                    ask = "Ask : {}\n".format(float(binance_json["askPrice"]))
                if binance_json["volume"] is None:
                    volume = "Volume : Unknown\n"
                else:
                    volume = "Volume : {} BTC\n".format(float(binance_json["volume"]))
                if binance_json["highPrice"] is None:
                    high = "1d High : Unknown\n"
                else:
                    high = "1d High : {}\n".format(float(binance_json["highPrice"]))
                if binance_json["lowPrice"] is None:
                    low = "1d Low : Unknown\n"
                else:
                    low = "1d Low : {}\n".format(float(binance_json["lowPrice"]))
                value_bin = "```css\n" + pair + volume + last + bid + ask + high + low + "```"
            else:
                pair = "Pair : BTC-" + coin + "\n"
                if binance_json["lastPrice"] is None:
                    last = "Last : Unknown\n"
                else:
                    last = "Last : {}\n".format(float(binance_json["lastPrice"]))
                if binance_json["bidPrice"] is None:
                    bid = "Bid : Unknown\n"
                else:
                    bid = "Bid : {}\n".format(float(binance_json["bidPrice"]))
                if binance_json["askPrice"] is None:
                    ask = "Ask : Unknown\n"
                else:
                    ask = "Ask : {}\n".format(float(binance_json["askPrice"]))
                if binance_json["volume"] is None:
                    volume = "Volume : Unknown\n"
                else:
                    volume = "Volume : {} BTC\n".format(float(binance_json["volume"]))
                if binance_json["highPrice"] is None:
                    high = "1d High : Unknown\n"
                else:
                    high = "1d High : {}\n".format(float(binance_json["highPrice"]))
                if binance_json["lowPrice"] is None:
                    low = "1d Low : Unknown\n"
                else:
                    low = "1d Low : {}\n".format(float(binance_json["lowPrice"]))
                value_bin = "```css\n" + pair + volume + last + bid + ask + high + low + "```"
        else:
            value_bin = "```css\n{} is not listed on Binance. ```".format(self.name)

        return value_bin

    async def function_cryptopia(self, coin):
        coin = coin.upper()
        if coin == "BTC":
            api_url = self.cryptopia_api_url_usdt.format(coin)
        else:
            api_url = self.cryptopia_api_url_btc.format(coin)
        r = requests.get(api_url)
        topia_json = r.json()
        error = topia_json["Error"]
        if error is None:
            if coin == "BTC":
                pair = "Pair : USD-" + coin + "\n"
                if topia_json["Data"]["LastPrice"] is None:
                    last = "Last : Unknown\n"
                else:
                    last = "Last : {0:.8f}\n".format(topia_json["Data"]["LastPrice"])
                if topia_json["Data"]["BidPrice"] is None:
                    bid = "Bid : Unknown\n"
                else:
                    bid = "Bid : {0:.8f}\n".format(topia_json["Data"]["BidPrice"])
                if topia_json["Data"]["AskPrice"] is None:
                    ask = "Ask : Unknown\n"
                else:
                    ask = "Ask : {0:.8f}\n".format(topia_json["Data"]["AskPrice"])
                if topia_json["Data"]["Volume"] is None:
                    volume = "Volume : Unknown\n"
                else:
                    volume = "Volume : {0:.2f} BTC\n".format(topia_json["Data"]["Volume"])
                if topia_json["Data"]["High"] is None:
                    high = "1d High : Unknown\n"
                else:
                    high = "1d High : " + "{0:.8f}\n".format(topia_json["Data"]["High"])
                if topia_json["Data"]["Low"] is None:
                    low = "1d Low : Unknown\n"
                else:
                    low = "1d Low : " + "{0:.8f}\n".format(topia_json["Data"]["Low"])
                value_topia = "```css\n" + pair + volume + last + bid + ask + high + low + "\n```"
            else:
                pair = "Pair : BTC-" + coin + "\n"
                if topia_json["Data"]["LastPrice"] is None:
                    last = "Last : Unknown\n"
                else:
                    last = "Last : {0:.8f}\n".format(topia_json["Data"]["LastPrice"])
                if topia_json["Data"]["BidPrice"] is None:
                    bid = "Bid : Unknown\n"
                else:
                    bid = "Bid : {0:.8f}\n".format(topia_json["Data"]["BidPrice"])
                if topia_json["Data"]["AskPrice"] is None:
                    ask = "Ask : Unknown\n"
                else:
                    ask = "Ask : {0:.8f}\n".format(topia_json["Data"]["AskPrice"])
                if topia_json["Data"]["Volume"] is None:
                    volume = "Volume : Unknown\n"
                else:
                    volume = "Volume : {0:.2f} BTC\n".format(topia_json["Data"]["Volume"])
                if topia_json["Data"]["High"] is None:
                    high = "1d High : Unknown\n"
                else:
                    high = "1d High : " + "{0:.8f}\n".format(topia_json["Data"]["High"])
                if topia_json["Data"]["Low"] is None:
                    low = "1d Low : Unknown\n"
                else:
                    low = "1d Low : " + "{0:.8f}\n".format(topia_json["Data"]["Low"])
                value_topia = "```css\n" + pair + volume + last + bid + ask + high + low + "\n```"
        else:
            value_topia = "```css\n{} is not listed on Cryptopia.\n```".format(self.name)
        return value_topia

    async def function_hitbtc(self, coin):
        coin = coin.upper()
        if coin == "MIOTA":
            coin = "IOTA"
            api_url = self.hitbtc_api_url_btc.format(coin)
        elif coin == "BTC":
            api_url = self.hitbtc_api_url_usdt.format(coin)
        else:
            api_url = self.hitbtc_api_url_btc.format(coin)
        r = requests.get(api_url)
        hitbtc_json = r.json()

        if "error" not in hitbtc_json:
            if coin == "BTC":
                pair = "Pair : USD-" + coin + "\n"
                if hitbtc_json["last"] is None:
                    last = "Last : Unknown\n"
                else:
                    last = "Last : {0:.8}\n".format(hitbtc_json["last"])
                if hitbtc_json["bid"] is None:
                    bid = "Bid : Unknown\n"
                else:
                    bid = "Bid : {0:.8}\n".format(hitbtc_json["bid"])
                if hitbtc_json["ask"] is None:
                    ask = "Ask : Unknown\n"
                else:
                    ask = "Ask : {0:.8}\n".format(hitbtc_json["ask"])
                if hitbtc_json["volume"] is None:
                    volume = "Volume : Unknown\n"
                else:
                    volume = "Volume : {0:.2} BTC\n".format(hitbtc_json["volume"])
                if hitbtc_json["high"] is None:
                    high = "1 High : Unknown\n"
                else:
                    high = "1d High : {0:.8}\n".format(hitbtc_json["high"])
                if hitbtc_json["low"] is None:
                    low = "1d Low : Unknown\n"
                else:
                    low = "1d Low : {0:.8}\n".format(hitbtc_json["low"])
                value_hitbtc = "```css\n" + pair + volume + last + bid + ask + high + low + "```"
            else:
                pair = "Pair : BTC-" + coin + "\n"
                if hitbtc_json["last"] is None:
                    last = "Last : Unknown\n"
                else:
                    last = "Last : {0:.8}\n".format(hitbtc_json["last"])
                if hitbtc_json["bid"] is None:
                    bid = "Bid : Unknown\n"
                else:
                    bid = "Bid : {0:.8}\n".format(hitbtc_json["bid"])
                if hitbtc_json["ask"] is None:
                    ask = "Ask : Unknown\n"
                else:
                    ask = "Ask : {0:.8}\n".format(hitbtc_json["ask"])
                if hitbtc_json["volume"] is None:
                    volume = "Volume : Unknown\n"
                else:
                    volume = "Volume : {0:.2} BTC\n".format(hitbtc_json["volume"])
                if hitbtc_json["high"] is None:
                    high = "1 High : Unknown\n"
                else:
                    high = "1d High : {0:.8}\n".format(hitbtc_json["high"])
                if hitbtc_json["low"] is None:
                    low = "1d Low : Unknown\n"
                else:
                    low = "1d Low : {0:.8}\n".format(hitbtc_json["low"])
                value_hitbtc = "```css\n" + pair + volume + last + bid + ask + high + low + "```"
        else:
            value_hitbtc = "```css\n{} is not listed on HitBTC.\n```".format(self.name)
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
        try:
            if coin == "BTC":
                pair = "Pair : " + self.key.replace("_", "-") + "\n"
                if poloniex_json[self.key]["last"] is None:
                    last = "Last : Unknown\n"
                else:
                    last = "Last : {0:.8f}\n".format(float(poloniex_json[self.key]["last"]))
                if poloniex_json[self.key]["highestBid"] is None:
                    bid = "Bid : Unknown\n"
                else:
                    bid = "Bid : {0:.8f}\n".format(float(poloniex_json[self.key]["highestBid"]))
                if poloniex_json[self.key]["lowestAsk"] is None:
                    ask = "Ask : Unknow\n"
                else:
                    ask = "Ask : {0:.8f}\n".format(float(poloniex_json[self.key]["lowestAsk"]))
                if poloniex_json[self.key]["quoteVolume"] is None:
                    volume = "Volume : Unknown\n"
                else:
                    volume = "Volume : {0:.2f} BTC\n".format(float(poloniex_json[self.key]["quoteVolume"]))
                if poloniex_json[self.key]["high24hr"] is None:
                    high = "1d High : Unknown\n"
                else:
                    high = "1d High : {0:.8f}\n".format(poloniex_json[self.key]["high24hr"])
                if poloniex_json[self.key]["low24hr"] is None:
                    low = "1d Low : Unknown\n"
                else:
                    low = "1d Low : {0:.8f}\n".format(poloniex_json[self.key]["low24hr"])
                value_polo = "```css\n" + pair + volume + last + bid + ask + high + low + "```"
            else:
                pair = "Pair : " + self.key.replace("_", "-") + "\n"
                if poloniex_json[self.key]["last"] is None:
                    last = "Last : Unknown\n"
                else:
                    last = "Last : {0:.8}\n".format(float(poloniex_json[self.key]["last"]))
                if poloniex_json[self.key]["highestBid"] is None:
                    bid = "Bid : Unknown\n"
                else:
                    bid = "Bid : {0:.8}\n".format(float(poloniex_json[self.key]["highestBid"]))
                if poloniex_json[self.key]["lowestAsk"] is None:
                    ask = "Ask : Unknown\n"
                else:
                    ask = "Ask : {0:.8}\n".format(float(poloniex_json[self.key]["lowestAsk"]))
                if poloniex_json[self.key]["quoteVolume"] is None:
                    volume = "Volume : Unknown\n"
                else:
                    volume = "Volume : {0:.2} BTC\n".format(poloniex_json[self.key]["quoteVolume"])
                if poloniex_json[self.key]["high24hr"] is None:
                    high = "1d High : Unknown\n"
                else:
                    high = "1d High : {0:.8}\n".format(poloniex_json[self.key]["high24hr"])
                if poloniex_json[self.key]["low24hr"] is None:
                    low = "1d Low : Unknown\n"
                else:
                    low = "1d Low : {0:.8}\n".format(float(poloniex_json[self.key]["low24hr"]))
                value_polo = "```css\n" + pair + volume + last + bid + ask + high + low + "\n```"
        except KeyError:
            value_polo = "```css\n{} is not listed on Poloniex.\n```".format(self.name)
        return value_polo

    def function_display_ok(self, cmc_value, bitfinex_value, bittrex_value, binance_value, cryptopia_value,
                            hitbtc_value, poloniex_value):
        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.add_field(name=":medal: CoinMarketCap Informations", value=cmc_value, inline=False)
        embed.add_field(name=":fleur_de_lis: Bitfinex Informations", value=bitfinex_value, inline=True)
        embed.add_field(name=":dragon: Bittrex Informations", value=bittrex_value, inline=True)
        embed.add_field(name=":game_die: Binance Informations", value=binance_value, inline=True)
        embed.add_field(name=":space_invader: Cryptopia Informations", value=cryptopia_value, inline=True)
        embed.add_field(name=":octopus: HitBTC Informations", value=hitbtc_value, inline=True)
        embed.add_field(name=":crystal_ball: Poloniex Informations", value=poloniex_value, inline=True)
        embed.set_footer(text="Request achieved :")

        return embed

    def function_display_err(self, cmc_value):
        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.add_field(name=":medal: CoinMarketCap Informations", value=cmc_value, inline=False)
        embed.set_footer(text="Request achieved :")

        return embed

    async def all(self, coin):
        cmc_value = await self.function_cmc(coin)
        if cmc_value == "```css\nThis ticker does not exist on Coinmarketcap.\nMaybe you made a typo in the coin's ticker.```":
            embed = self.function_display_err(cmc_value)
        else:
            bitfinex_value = await self.function_bitfinex(coin)
            bittrex_value = await self.function_bittrex(coin)
            binance_value = await self.function_binance(coin)
            cryptopia_value = await self.function_cryptopia(coin)
            hitbtc_value = await self.function_hitbtc(coin)
            poloniex_value = await self.function_poloniex(coin)
            embed = self.function_display_ok(cmc_value, bitfinex_value, bittrex_value, binance_value, cryptopia_value,
                                             hitbtc_value, poloniex_value)

        return embed

import discord
from discord.ext.commands import Bot
import dir_request_api
import dir_side_info
import requests
import threading

client = Bot(command_prefix='!')
channel = None
secret_token = ""

MAXIMUM_COINS = 10


@client.event
async def on_ready():
    """
    Verify that the bot is connected and is working
    """
    global channel
    print("Logged in as :")
    print(client.user.name)
    print(client.user.id)
    client.change_presence(game=discord.Game(name="TEST"))
    # btcgame()


@client.command(pass_context=True)
async def all(ctx, *coin):
    """
    This command is used to know the price of a coin on the following exchanges
    Bitfinex; Bittrex, Cryptopia, Poloniex and Binance

    Example : !all eth
    """
    global channel
    await client.send_typing(ctx.message.channel)
    try:
        for i in coin[:MAXIMUM_COINS]:
            all_coin = dir_request_api.all_file.Class_All(i.lower(), ctx.message.author)
            result = await all_coin.query_all()
            if channel is None:
                await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=result)
            else:
                await client.send_message(channel, ctx.message.author.mention, embed=result)
    except Exception as e:
        print("Global Error on !all\n", e)


@client.command(pass_context=True)
async def rex(ctx, *coin):
    """
    This command is used to know the value of a coin listed on Bittrex
    BTC-Coin Pair only.

    Example : !rex eth
    """
    global channel
    await client.send_typing(ctx.message.channel)
    try:
        for i in coin[:MAXIMUM_COINS]:
            bittrex = dir_request_api.bittrex_file.Class_Bittrex(i.lower(), ctx.message.author)
            result = await bittrex.bittrex_query()
            if channel is None:
                await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=result)
            else:
                await client.send_message(channel, ctx.message.author.mention, embed=result)
    except Exception as e:
        print("Global Error on !rex\n", e)


@client.command(pass_context=True)
async def polo(ctx, *coin):
    """
    This command is used to know the value of a coin listed on Poloniex
    BTC-Coin Pair only.

    Example : !polo eth
    """
    global channel
    await client.send_typing(ctx.message.channel)
    try:
        for i in coin[:MAXIMUM_COINS]:
            poloniex = dir_request_api.poloniex_file.Class_Poloniex(i.lower(), ctx.message.author)
            result = await poloniex.poloniex_query()
            if channel is None:
                await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=result)
            else:
                await client.send_message(channel, ctx.message.author.mention, embed=result)
    except Exception as e:
        print("Global Error on !polo\n", e)


@client.command(pass_context=True)
async def topia(ctx, *coin):
    """
    This command is used to know the value of a coin listed on Cryptopia
    BTC-Coin Pair only.

    Example : !topia eth
    """
    global channel
    await client.send_typing(ctx.message.channel)
    try:
        for i in coin[:MAXIMUM_COINS]:
            cryptopia = dir_request_api.cryptopia_file.Class_Cryptopia(i.lower(), ctx.message.author)
            result = await cryptopia.cryptopia_query()
            if channel is None:
                await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=result)
            else:
                await client.send_message(channel, ctx.message.author.mention, embed=result)
    except Exception as e:
        print("Global Error on !topia\n", e)


@client.command(pass_context=True)
async def finex(ctx, *coin):
    """
    This command is used to know the value of a coin listed on Bitfinex
    BTC-Coin Pair only.

    Example : !finex eth
    """
    global channel
    await client.send_typing(ctx.message.channel)
    try:
        for i in coin[:MAXIMUM_COINS]:
            bitfinex = dir_request_api.bitfinex_file.Class_Bitfinex(i.lower(), ctx.message.author)
            result = await bitfinex.bitfinex_query()
            if channel is None:
                await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=result)
            else:
                await client.send_message(channel, ctx.message.author.mention, embed=result)
    except Exception as e:
        print("Global Error on !finex\n", e)


@client.command(pass_context=True)
async def binance(ctx, *coin):
    """
    This command is used to know the value of a coin listed on Binance
    BTC-Coin Pair only.

    Example : !binance eth
    """
    global channel
    await client.send_typing(ctx.message.channel)
    try:
        for i in coin[:MAXIMUM_COINS]:
            binance_api = dir_request_api.binance_file.Class_Binance(i.lower(), ctx.message.author)
            result = await binance_api.binance_query()
            if channel is None:
                await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=result)
            else:
                await client.send_message(channel, ctx.message.author.mention, embed=result)
    except Exception as e:
        print("Global Error on !binance\n", e)


@client.command(pass_context=True)
async def whale(ctx, arg, limit=4):
    """
    This command is used to know the big orders placed by whales on several exchanges.
    The command return the Number of coin bought at which price and the number of coin sold at which price

    A parameter can be added to set a limit in the number of BTC put in the order (Default is 4)

    NOTE : You can't ask for BTC Whales (because you can buy/sell BTC with/against BTC)

    Example : !whale eth
              !whale eth 10
    """
    global channel
    await client.send_typing(ctx.message.channel)
    try:
        whale_exchange = dir_request_api.whale_file.Class_whale(arg, ctx.message.author)
        result = await whale_exchange.query_whale(limit)
        if channel is None:
            await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=result)
        else:
            await client.send_message(channel, ctx.message.author.mention, embed=result)
    except Exception as e:
        print("Global Error on !whale\n", e)


@client.command(pass_context=True)
async def cmc(ctx):
    """
    This command is used to know the actual state of the market.
    The wesbite used is CoinMarketCap

    Example : !cmc
    """
    global channel
    await client.send_typing(ctx.message.channel)
    try:
        CoinMarketCap = dir_request_api.cmc_file.Class_Coinmarketcap()
        result = await CoinMarketCap.cmc_query(ctx.message.author)
        if channel is None:
            await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=result)
        else:
            await client.send_message(channel, ctx.message.author.mention, embed=result)
    except Exception as e:
        print("Global Error on !cmc\n", e)


@client.command(pass_context=True)
async def top(ctx):
    """
    This command is used to know the biggest gainer and loser since 24h on the marketcap.

    Example : !top
    """
    global channel
    await client.send_typing(ctx.message.channel)
    try:
        top_coin = dir_request_api.top_file.Class_Topcoin()
        result = await top_coin.query_top(ctx.message.author)
        if channel is None:
            await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=result)
        else:
            await client.send_message(channel, ctx.message.author.mention, embed=result)
    except Exception as e:
        print("Global Error on !top\n", e)


@client.command(pass_context=True)
async def btc(ctx):
    """
    This command is used to know the price of the Bitcoin on several exchanges.

    Example : !btc
    """
    global channel
    await client.send_typing(ctx.message.channel)
    Bitcoin = dir_request_api.btc_file.Class_bitcoin()
    json = await Bitcoin.fetch()
    result = Bitcoin.function_display(json, ctx.message.author)
    if channel is None:
        await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=result)
    else:
        await client.send_message(channel, ctx.message.author.mention, embed=result)


@client.command(pass_context=True)
async def order(ctx, price, profit, loss):
    """
    This command is used to calculate the exit point of a trade depending of the profit target and the stop-loss target

    The first parameter is the price of the buy ( ex : 0.015) .You don't need to add the coin
    The second parameter is the percentage of the profit you are aiming ( ex 50% profit)
    The third parameter is the percentage of the stop loss you want ( ex 10% loss)

    Example : !order 0.015 50 10
    """
    await client.send_typing(ctx.message.channel)
    try:
        the_order = dir_side_info.order_file.Class_Order(ctx.message.author)
        embed = the_order.function_order(price, profit, loss)
        await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=embed)
    except Exception as e:
        print("Global Error on !order\n", e)


@client.command(pass_context=True)
async def event(ctx, coin="", event_type=""):
    """
        This command will display the next events to come.
        The events are retrieved from Coinmarketcal.com


        Example : !event [coin]
        """
    if coin == "":
        coin = ""

    if event_type == "":
        event_type = ""

    if event_type == "" and coin == "":
        coin = ""
        event_type = ""

    await client.send_typing(ctx.message.channel)
    var_catalysts = dir_side_info.catalysts_file.Class_Catalysts(ctx.message.author)
    embed = var_catalysts.get_catalysts(coin, event_type)
    await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=embed)


@client.command(pass_context=True)
async def convert(ctx, coin, qty):
    """
    This command is used to convert the amount of coins you have into BTC and US$

    The first parameter is the coin name (ex eth)
    The second parameter is the number of coin you have ( ex 2.5)

    Example : !conv eth 2.5
    """
    await client.send_typing(ctx.message.channel)
    try:
        conv = dir_side_info.convert_file.Class_Conv(ctx.message.author)
        data = await conv.function_price(coin, qty)
        embed = conv.function_display(data, coin, qty)
        await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=embed)
    except Exception as e:
        print("Global Error on !conv\n", e)


@client.command(pass_context=True)
async def name(ctx, coin):
    """
    This command is used to know the full name of a coin and some side informations associated with it.

    Example : !name eth
    """
    await client.send_typing(ctx.message.channel)
    try:
        coin_name = dir_side_info.name_file.Class_Name(ctx.message.author, coin.lower())
        data = await coin_name.function_query_name()
        embed = await coin_name.function_display(data)
        await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=embed)
    except Exception as e:
        print("Global Error on !name\n", e)


@client.command(pass_context=True)
async def infos(ctx):
    """
    This command is used to display all the available commands on the bot.

    Example : !infos
    """
    await client.send_typing(ctx.message.channel)
    try:
        info = dir_side_info.informations_file.Class_Info(ctx.message.author)
        embed = info.function_informations()
        await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=embed)
    except Exception as e:
        print("Global Error on !infos\n", e)


@client.command(pass_context=True)
async def resources(ctx):
    """
    This command is used to display Masons's ref links and resources.

    Example : !resources
    """
    await client.send_typing(ctx.message.channel)
    dona = dir_side_info.resources_file.Class_Resources
    embed = dona.function_display()
    await client.send_message(ctx.message.channel, embed=embed)


@client.command(pass_context=True)
async def bot(ctx):
    """
    This command is used to display some informations about the bot.
    Don't hesitate to Star it and Fork if you want to :)
    The code will remain open source and free for everyone.

    Example : !bot
    """
    await client.send_typing(ctx.message.channel)
    bot_var = dir_side_info.bot_file.Class_Bot()
    embed = bot_var.function_display()
    await client.send_message(ctx.message.channel, embed=embed)


@client.command(pass_context=True)
async def masons(ctx):
    """
    This command is used to know all the advantages of being a VIP in the Bitcoin Masons Discord server.

    Example : !masons
    """
    await client.send_typing(ctx.message.channel)
    vip = dir_side_info.masons_file.Class_Masons()
    embed = vip.function_display()
    await client.send_message(ctx.message.channel, embed=embed)


@client.command(pass_context=True)
async def sum(ctx, url=None, limit=10):
    """
    This command is used to shorten a website article.
    The parameter is the url of the article.

    The result may be unclear or buggy (Discord is limiting the message number of characters at 2000 atm)

    Example : !sum https://www.forbes.com/sites/forbestechcouncil/2017/11/27/five-reasons-bitcoin-will-be-your-best-high-growth-investment-for-2018/#229c706c47e8
    """
    await client.send_typing(ctx.message.channel)
    sum_infos = dir_side_info.sumarize_file.Class_Summarize(ctx.message.author, url, limit)
    list_v = sum_infos.function_sum()
    await client.send_message(ctx.message.channel, list_v[0][0])
    await client.send_message(ctx.message.channel, list_v[0][1])


def btcgame():
    """
    Display the bitcoin price in the user list
    """
    threading.Timer(1.0, btcgame).start()
    bitcoin_price_url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    data = requests.get(bitcoin_price_url).json()
    price_in_usd = data['bpi']['USD']['rate']
    price_in_usd = price_in_usd.split(".")[0]
    btc_text = "BTC : "
    btc_status = btc_text + price_in_usd + " $"
    game = client.change_presence(game=discord.Game(name=btc_status))
    print(btc_status)
    return game


@client.command(pass_context=True)
async def doge(ctx):
    """
        Praise our Lord and Savior, the Mighty DOGE

        Example : !doge
    """
    await client.send_typing(ctx.message.channel)
    dogeLord = dir_side_info.doge_file.Class_Doge()
    embed = dogeLord.function_display()
    await client.send_message(ctx.message.channel, embed=embed)


client.run(secret_token)

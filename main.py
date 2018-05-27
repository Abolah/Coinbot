import discord
from discord.ext.commands import Bot
import dir_request_api
import dir_side_info
import requests
import aiohttp
import asyncio
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = Bot(command_prefix='!')
channel = None
secret_token = ""

# START of Discorbots.org code.
dbltoken = ""
url = "https://discordbots.org/api/bots/367061304042586124/stats"
headers = {"Authorization": dbltoken}
# END of Discorbots.org code.


MAXIMUM_COINS = 5


@client.event
async def on_ready():
    """
    Verify that the bot is connected and is working
    """
    global channel
    print("Logged in as :")
    print(client.user.name)
    print(client.user.id)
    await client.change_presence(game=discord.Game(name="Type !infos to list the commands"))
    payload = {"server_count": len(client.servers)}
    async with aiohttp.ClientSession() as aioclient:
        await aioclient.post(url, data=payload, headers=headers)


@client.event
async def on_server_join(server):
    print("Joining Server : ", server)
    on_join = dir_side_info.welcome.Class_On_join()
    welcome = await on_join.function_welcome()
    await channel.send_message(server, embed=welcome)
    payload = {"server_count": len(client.servers)}
    async with aiohttp.ClientSession() as aioclient:
        await aioclient.post(url, data=payload, headers=headers)


@client.event
async def on_server_remove():
    payload = {"server_count": len(client.servers)}
    async with aiohttp.ClientSession() as aioclient:
        await aioclient.post(url, data=payload, headers=headers)


@client.command(pass_context=True)
async def all(ctx, *coin):
    """
    This command is used to know the price of a coin on the following exchanges
    Bitfinex, Bittrex, Cryptopia, Poloniex, Binance and HitBTC

    You can ask for as much as 5 coins at the same time.

    Example : !all eth
    """
    global channel
    await client.send_typing(ctx.message.channel)
    for i in coin[:MAXIMUM_COINS]:
        all_coin = dir_request_api.all.Class_All(ctx.message.author)
        result = await all_coin.all(i.lower())
        if channel is None:
            await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=result)
        else:
            await client.send_message(channel, ctx.message.author.mention, embed=result)


@client.command(pass_context=True)
async def bnc(ctx, *coin):
    """
        This command is used to know the value of a coin listed on Binance
        BTC-Coin Pair only.

        You can ask for as much as 5 coins at the same time.

        Example : !bnc eth
        """
    await client.send_typing(ctx.message.channel)
    for i in coin[:MAXIMUM_COINS]:
        binance_api = dir_request_api.binance.Class_Binance(ctx.message.author)
        result = await binance_api.binance(i.lower())
        if channel is None:
            await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=result)
        else:
            await client.send_message(channel, ctx.message.author.mention, embed=result)


@client.command(pass_context=True)
async def fnx(ctx, *coin):
    """
    This command is used to know the value of a coin listed on Bitfinex
    BTC-Coin Pair only.

    You can ask for as much as 5 coins at the same time.

    Example : !fnx eth
    """
    await client.send_typing(ctx.message.channel)
    for i in coin[:MAXIMUM_COINS]:
        bitfinex = dir_request_api.bitfinex.Class_Bitfinex(ctx.message.author)
        result = await bitfinex.bitfinex(i.lower())
        if channel is None:
            await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=result)
        else:
            await client.send_message(channel, ctx.message.author.mention, embed=result)


@client.command(pass_context=True)
async def rex(ctx, *coin):
    """
    This command is used to know the value of a coin listed on Bittrex
    BTC-Coin Pair only.

    You can ask for as much as 5 coins at the same time.

    Example : !rex eth
    """
    global channel
    await client.send_typing(ctx.message.channel)
    for i in coin[:MAXIMUM_COINS]:
        bittrex = dir_request_api.bittrex.Class_Bittrex(ctx.message.author)
        result = await bittrex.bittrex(i.lower())
        if channel is None:
            await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=result)
        else:
            await client.send_message(channel, ctx.message.author.mention, embed=result)


@client.command(pass_context=True)
async def polo(ctx, *coin):
    """
    This command is used to know the value of a coin listed on Poloniex
    BTC-Coin Pair only.

    You can ask for as much as 5 coins at the same time.

    Example : !polo eth
    """
    global channel
    await client.send_typing(ctx.message.channel)
    for i in coin[:MAXIMUM_COINS]:
        poloniex = dir_request_api.poloniex.Class_Poloniex(ctx.message.author)
        result = await poloniex.poloniex(i.lower())
        if channel is None:
            await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=result)
        else:
            await client.send_message(channel, ctx.message.author.mention, embed=result)


@client.command(pass_context=True)
async def topia(ctx, *coin):
    """
    This command is used to know the value of a coin listed on Cryptopia
    BTC-Coin Pair only.

    You can ask for as much as 5 coins at the same time.

    Example : !topia eth
    """
    global channel
    await client.send_typing(ctx.message.channel)
    for i in coin[:MAXIMUM_COINS]:
        cryptopia = dir_request_api.cryptopia.Class_Cryptopia(ctx.message.author)
        result = await cryptopia.cryptopia(i.lower())
        if channel is None:
            await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=result)
        else:
            await client.send_message(channel, ctx.message.author.mention, embed=result)


@client.command(pass_context=True)
async def hit(ctx, *coin):
    """
    This command is used to know the value of a coin listed on HitBTC
    BTC-Coin Pair only.

    You can ask for as much as 5 coins at the same time.

    Example : !hit eth
    """
    global channel
    await client.send_typing(ctx.message.channel)
    for i in coin[:MAXIMUM_COINS]:
        hitbtc = dir_request_api.hitbtc.Class_HitBTC(ctx.message.author)
        result = await hitbtc.hitbtc(i.lower())
        if channel is None:
            await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=result)
        else:
            await client.send_message(channel, ctx.message.author.mention, embed=result)


@client.command(pass_context=True)
async def mini(ctx, *coin):
    """
    This command is used to know the value of a coin on coinmarketcap.

    You can ask for as much as 5 coins at the same time.

    Example : !mini eth
    """
    await client.send_typing(ctx.message.channel)
    for i in coin[:MAXIMUM_COINS]:
        mini_call = dir_request_api.mini.Class_mini(ctx.message.author)
        result = await mini_call.mini(i.lower())
        if channel is None:
            await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=result)
        else:
            await client.send_message(channel, ctx.message.author.mention, embed=result)


@client.command(pass_context=True)
async def mexbook(ctx):
    """
    This command display the 10 last Orders on Bitmex OrderBook

    Example : !mexbook
    """
    global channel
    await client.send_typing(ctx.message.channel)
    bitmex_orderbook = dir_request_api.mexbook.Class_BitmexOrderBook(ctx.message.author)
    result = await bitmex_orderbook.bitmex()
    await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=result)


@client.command(pass_context=True)
async def whale(ctx, arg):
    """
    This command is used to know the big orders placed by whales on several exchanges.
    The command return the Number of coin bought at which price and the number of coin sold at which price

    A parameter can be added to set a limit in the number of BTC put in the order (Default is 4)

    NOTE : If you want to see BTC whales just type USD

    Example : !whale eth
              !whale eth 10
    """
    if arg == "usd":
        limit = 100000
    else:
        limit = 1
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
    CoinMarketCap = dir_request_api.coinmarketcap.Class_Coinmarketcap(ctx.message.author)
    result = await CoinMarketCap.cmc_query()
    if channel is None:
        await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=result)
    else:
        await client.send_message(channel, ctx.message.author.mention, embed=result)


@client.command(pass_context=True)
async def top(ctx):
    """
    This command is used to know the biggest gainer and loser since 24h on the marketcap.

    Example : !top
    """
    global channel
    await client.send_typing(ctx.message.channel)
    top_coin = dir_request_api.top.Class_Topcoin(ctx.message.author)
    result = await top_coin.query_top()
    if channel is None:
        await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=result)
    else:
        await client.send_message(channel, ctx.message.author.mention, embed=result)


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
async def balance(ctx, coin, address):
    """
    This command is used to know the balance of an ETH or BTC wallet

    NOTE: Only BTC and ETH are supported yet.

    Example : !balance eth 0x670B7A9497f79Ef57BbFFFB553d979E7aD225344
              !balance btc 1jc3V3T5mefuD9asa7en976NKVGssQuMq
    """
    global channel
    await client.send_typing(ctx.message.channel)
    balances = dir_request_api.balance.Class_Balance(ctx.message.author)
    result = await balances.balance(coin, address)
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
    The second parameter is the number of coin you have (ex 2.5)

    Example : !convert eth 2.5
    """
    await client.send_typing(ctx.message.channel)
    conv_var = dir_side_info.convert.Class_Conv(ctx.message.author)
    embed = await conv_var.function_convert(coin, qty)
    await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=embed)


@client.command(pass_context=True)
async def name(ctx, coin):
    """
    This command is used to know the full name of a coin and some side informations associated with it.

    Example : !name eth
    """
    await client.send_typing(ctx.message.channel)
    coin_name = dir_side_info.name.Class_Name()
    embed = await coin_name.get_name(coin)
    await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=embed)


@client.command(pass_context=True)
async def infos(ctx):
    """
    This command is used to display all the available commands on the bot.

    Example : !infos
    """
    await client.send_typing(ctx.message.channel)
    info = dir_side_info.informations_file.Class_Info(ctx.message.author)
    embed = info.function_informations()
    await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=embed)


@client.command(pass_context=True)
async def bot(ctx):
    """
    This command is used to display some informations about the bot.
    Don't hesitate to Star it and Fork if you want to :)
    The code will remain open source and free for everyone.

    Example : !bot
    """
    global member
    await client.send_typing(ctx.message.channel)
    bot_var = dir_side_info.bot_file.Class_Bot()
    srv_count = str(len(client.servers))
    user_count = 0
    for server in client.servers:
        for member in server.members:
            user_count += 1
    embed = bot_var.function_display(srv_count, user_count)
    await client.send_message(ctx.message.channel, embed=embed)


@client.command(pass_context=True)
async def updates(ctx):
    """
    This command will send the latest updates of the bot in the user's private message

    Example : !updates
    """
    update_var = dir_side_info.updates.Class_update()
    embed = update_var.function_display()
    await client.send_message(ctx.message.author, embed=embed)
    author = str(ctx.message.author).split("#")
    author = author[0]
    message = await client.send_message(ctx.message.channel, "Check your DM's " + author)
    await asyncio.sleep(5)
    await client.delete_message(message)
    await asyncio.sleep(3)


@client.command(pass_context=True)
async def sum(ctx, article_url=None, limit=10):
    """
    This command is used to shorten a website article.
    The parameter is the url of the article.

    The result may be unclear or buggy (Discord is limiting the message number of characters at 2000 atm)

    Example : !sum https://www.forbes.com/sites/forbestechcouncil/2017/11/27/five-reasons-bitcoin-will-be-your-best-high-growth-investment-for-2018/#229c706c47e8
    """
    await client.send_typing(ctx.message.channel)
    sum_infos = dir_side_info.sumarize_file.Class_Summarize(ctx.message.author, article_url, limit)
    list_v = sum_infos.function_sum()
    await client.send_message(ctx.message.channel, list_v[0][0])
    await client.send_message(ctx.message.channel, list_v[0][1])


def btcgame():
    """
    Buggy atm (WIP)
    """
    bitcoin_price_url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    data = requests.get(bitcoin_price_url).json()
    price_in_usd = data['bpi']['USD']['rate'].split(".")[0]
    btc_status = "BTC : ${}".format(price_in_usd)
    client.change_presence(game=discord.Game(name=btc_status))
    asyncio.sleep(5)


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


btcgame()
client.run(secret_token)

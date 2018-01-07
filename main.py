import discord
from discord.ext.commands import Bot
import request_api
import request_database
import side_info
import requests
import time

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
    starttime = time.time()
    await btcgame()
    time.sleep(10 - ((time.time() - starttime) % 10))


@client.command(pass_context=True)
async def all(ctx, *coin):
    """
    This command is used to know the price of a coin on the following exchanges
    Bitfinex; Bittrex, Cryptopia, Poloniex and Binance

    Example : !all eth

    """
    global channel
    await client.send_typing(ctx.message.channel)
    statistiques = request_database.stats_sql.Stats(ctx.message.author)
    try:
        for i in coin[:MAXIMUM_COINS]:
            await statistiques.stats_add("!all", i.lower())
            all_coin = request_api.request_all.all_currencies(i.lower(), ctx.message.author)
            result = await all_coin.query_all()
            if channel is None:
                await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=result)
            else:
                await client.send_message(channel, ctx.message.author.mention, embed=result)
    except Exception as e:
        print("Global Error on !all\n", e)


@client.command(pass_context=True)
async def rex(ctx, *coin):

    print(coin[:1])
    """
    This command is used to know the value of a coin listed on Bittrex
    BTC-Coin Pair only.

    Example : !rex eth
    """
    global channel
    await client.send_typing(ctx.message.channel)
    statistiques = request_database.stats_sql.Stats(ctx.message.author)
    try:
        for i in coin[:MAXIMUM_COINS]:
            await statistiques.stats_add("!rex", i.lower())
            bittrex = request_api.request_bittrex.bittrex(i.lower(), ctx.message.author)
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
    statistiques = request_database.stats_sql.Stats(ctx.message.author)
    try:
        for i in coin[:MAXIMUM_COINS]:
            await statistiques.stats_add("!polo", i.lower())
            poloniex = request_api.request_poloniex.Poloniex(i.lower(), ctx.message.author)
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
    statistiques = request_database.stats_sql.Stats(ctx.message.author)
    try:
        for i in coin[:MAXIMUM_COINS]:
            await statistiques.stats_add("!topia", i.lower())
            cryptopia = request_api.request_cryptopia.Cryptopia(i.lower(), ctx.message.author)
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
    statistiques = request_database.stats_sql.Stats(ctx.message.author)
    try:
        for i in coin[:MAXIMUM_COINS]:
            await statistiques.stats_add("!finex", i.lower())
            bitfinex = request_api.request_bitfinex.Bitfinex(i.lower(), ctx.message.author)
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
    statistiques = request_database.stats_sql.Stats(ctx.message.author)
    try:
        for i in coin[:MAXIMUM_COINS]:
            await statistiques.stats_add("!binance", i.lower())
            binance_api = request_api.request_binance.Binance(i.lower(), ctx.message.author)
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

    Example : !whale eth
              !whale eth 10
    """
    global channel
    await client.send_typing(ctx.message.channel)
    statistiques = request_database.stats_sql.Stats(ctx.message.author)
    try:
        await statistiques.stats_add("!whale", "")
        whale_exchange = request_api.request_whale.whale(arg, ctx.message.author)
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
    statistiques = request_database.stats_sql.Stats(ctx.message.author)
    try:
        await statistiques.stats_add("!cmc", "")
        CoinMarketCap = request_api.request_marketcap.Coinmarketcap()
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
    statistiques = request_database.stats_sql.Stats(ctx.message.author)
    try:
        await statistiques.stats_add("!top", "")
        top_coin = request_api.request_top.Topcoin()
        result = await top_coin.query_top(ctx.message.author)
        if channel is None:
            await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=result)
        else:
            await client.send_message(channel, ctx.message.author.mention, embed=result)
    except Exception as e:
        print("Global Error on !top\n", e)


@client.command(pass_context=True)
async def db(ctx, arg, rank=None, coin=None, *comment):
    """
    This command is used to make several request on the database.

    Use !db info for more informations

    Example : !db info
    """
    await client.send_typing(ctx.message.channel)
    try:
        comment = ' '.join(comment)
        database = request_database.list_sql.Listsql(ctx.message.author)
        embed = database.db_query(arg, rank, coin, comment)
        await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=embed)
    except Exception as e:
        print("Global Error on !db\n", e)


@client.command(pass_context=True)
async def btc(ctx):
    """
    This command is used to know the price of the Bitcoin on several exchanges.

    Example : !btc
    """
    global channel
    await client.send_typing(ctx.message.channel)
    statistiques = request_database.stats_sql.Stats(ctx.message.author)
    await statistiques.stats_add("!btc", "")
    Bitcoin = request_api.request_btc.bitcoin()
    json = await Bitcoin.fetch()
    result = Bitcoin.affichage(json, ctx.message.author)
    if channel is None:
        await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=result)
    else:
        await client.send_message(channel, ctx.message.author.mention, embed=result)


@client.command(pass_context=True)
async def stats(ctx, arg=None):
    """
    This command is used to know which command and which coin was asked the most on the server.

    Example : !stats
    """
    await client.send_typing(ctx.message.channel)
    try:
        database = request_database.stats_sql.Stats(ctx.message.author)
        conn = database.connect(arg)
        data = database.get(conn, arg)
        embed = database.get_affichage(data, arg)
        await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=embed)
    except Exception as e:
        print("Global Error on !db\n", e)


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
    statistiques = request_database.stats_sql.Stats(ctx.message.author)
    await statistiques.stats_add("!order", "")
    try:
        the_order = side_info.order_info.Order(ctx.message.author)
        embed = the_order.order(price, profit, loss)
        await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=embed)
    except Exception as e:
        print("Global Error on !order\n", e)


@client.command(pass_context=True)
async def conv(ctx, coin, qty):
    """
    This command is used to convert the amount of coins you have into BTC and US$

    The first parameter is the coin name (ex eth)
    The second parameter is the number of coin you have ( ex 2.5)

    Example : !conv eth 2.5
    """
    await client.send_typing(ctx.message.channel)
    statistiques = request_database.stats_sql.Stats(ctx.message.author)
    await statistiques.stats_add("!conv", "")
    try:
        convert = side_info.conv_price.Conv(ctx.message.author)
        data = await convert.price(coin, qty)
        embed = convert.affichage(data, coin, qty)
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
    statistiques = request_database.stats_sql.Stats(ctx.message.author)
    await statistiques.stats_add("!name", "")
    try:
        coin_name = side_info.name.Name(ctx.message.author, coin.lower())
        data = await coin_name.query_name()
        embed = await coin_name.affichage(data)
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
    statistiques = request_database.stats_sql.Stats(ctx.message.author)
    await statistiques.stats_add("!infos", "")
    try:
        info = side_info.info.Info(ctx.message.author)
        embed = info.info()
        await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=embed)
    except Exception as e:
        print("Global Error on !infos\n", e)


@client.command(pass_context=True)
async def event(ctx, limit=0):
    """
    This command is used to know the incoming events
    The website used is coincalendar.

    The limit of the command is the page displayed

    Example : !event | !event 3
    """
    await client.send_typing(ctx.message.channel)
    statistiques = request_database.stats_sql.Stats(ctx.message.author)
    await statistiques.stats_add("!event", "")

    events = side_info.event_crypto.Event_Crypto(ctx.message.author)
    embed = await events.get_event(limit)
    await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=embed)


@client.command(pass_context=True)
async def resources(ctx):
    """
    This command is used to display Abolah's donation addresses.
    If you like this bot you can donate to help me improving the bot :)

    Example : !money
    """
    await client.send_typing(ctx.message.channel)
    dona = side_info.donate.Donate()
    embed = dona.affichage()
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
    source_code = side_info.code.Code()
    embed = source_code.affichage()
    await client.send_message(ctx.message.channel, embed=embed)


@client.command(pass_context=True)
async def masons(ctx):
    """
    This command is used to know all the advantages of being a VIP in the Bitcoin Masons Discord server.

    Example : !masons
    """
    await client.send_typing(ctx.message.channel)
    vip = side_info.wolf.Wolf()
    embed = vip.affichage()
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
    statistiques = request_database.stats_sql.Stats(ctx.message.author)
    await statistiques.stats_add("!order", "")
    sum_infos = side_info.sumarize.Sumarize(ctx.message.author, url, limit)
    list_v = sum_infos.sum()
    await client.send_message(ctx.message.channel, list_v[0][0])
    await client.send_message(ctx.message.channel, list_v[0][1])


async def btcgame():
    """
    Display the bitcoin price in the user list

    """
    bitcoin_price_url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    data = requests.get(bitcoin_price_url).json()
    price_in_usd = data['bpi']['USD']['rate']
    price_in_usd = price_in_usd.split(".")[0]
    btc_text = "BTC Price : "
    btc_status = btc_text + price_in_usd
    await client.change_presence(game=discord.Game(name=btc_status))


@client.command(pass_context=True)
async def voc(ctx):
    """
    This command is used to know all the advantages of being a VIP in Wolf of Poloniex's Discord server.

    Example : !voc rsi
    """
    await client.send_typing(ctx.message.channel)
    vocab = side_info.wolf.Wolf()
    embed = vocab.affichage()
    await client.send_message(ctx.message.channel, embed=embed)


@client.command(pass_context=True)
async def doge(ctx):
    """
        Praise our Lord and Savior, the Mighty DOGE

        Example : !doge
    """
    await client.send_typing(ctx.message.channel)
    dogeLord = side_info.doge.Doge()
    embed = dogeLord.affichage()
    await client.send_message(ctx.message.channel, embed=embed)


client.run(secret_token)

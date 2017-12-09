import twitty
import discord
from discord.ext.commands import Bot
import request_api
import request_database
import side_info

client = Bot(command_prefix='!')
channel = None

@client.event
async def on_ready():
    """
    Verify that the bot is connected and is working
    :return:
    """
    global channel
    print("Logged in as :")
    print(client.user.name)
    print(client.user.id)
    channel = await redirect_chan()

@client.command(pass_context=True)
async def all(ctx,*coin):
    """
    Request on a cryptocurrency on all the exchanges which are supported by the bot ||  ex : ?all xzc
    :param ctx: Context i.e metadata of the message
    :param coin: The coin symbol
    :return: The whole message (embed)
    """
    global channel
    await client.send_typing(ctx.message.channel)
    stats = request_database.stats_sql.Stats(ctx.message.author)
    try:
        for i in coin:
            await stats.stats_add("?all",i.lower())
            all = request_api.request_all.all_currencies(i.lower(),ctx.message.author)
            result = await all.query_all()
            if channel == None :
                await client.send_message(ctx.message.channel,ctx.message.author.mention,embed=result)
            else:
                await client.send_message(channel, ctx.message.author.mention, embed=result)
    except Exception as e:
        print("Global Error on ?all\n",e)

@client.command(pass_context=True)
async def rex(ctx,*coin):
    """
    Request on a cryptocurrency which is on Bittrex ||  ex : ?rex xzc
    :param ctx: Context i.e metadata of the message
    :param coin: The coin symbol
    :return: The whole message (embed)
    """
    global channel
    await client.send_typing(ctx.message.channel)
    stats = request_database.stats_sql.Stats(ctx.message.author)
    try:
        for i in coin:
            await stats.stats_add("?rex",i.lower())
            bittrex = request_api.request_bittrex.bittrex(i.lower(),ctx.message.author)
            result = await bittrex.bittrex_query()
            if channel == None :
                await client.send_message(ctx.message.channel,ctx.message.author.mention,embed=result)
            else:
                await client.send_message(channel, ctx.message.author.mention, embed=result)
    except Exception as e:
        print("Global Error on ?rex\n",e)

@client.command(pass_context=True)
async def polo(ctx,*coin):
    """
    Request on a cryptocurrency which is on Poloniex ||  ex : ?polo xzc
    :param ctx: Context i.e metadata of the message
    :param coin: The coin symbol
    :return: The whole message (embed)
    """
    global channel
    await client.send_typing(ctx.message.channel)
    stats = request_database.stats_sql.Stats(ctx.message.author)
    try:
        for i in coin:
            await stats.stats_add("?polo", i.lower())
            poloniex = request_api.request_poloniex.Poloniex(i.lower(), ctx.message.author)
            result = await poloniex.poloniex_query()
            if channel == None:
                await client.send_message(ctx.message.channel,ctx.message.author.mention,embed=result)
            else:
                await client.send_message(channel, ctx.message.author.mention, embed=result)
    except Exception as e:
        print("Global Error on ?polo\n",e)

@client.command(pass_context=True)
async def topia(ctx,*coin):
    """
    Request on a cryptocurrency which is on Cryptopia ||  ex : ?topia sumo
    :param ctx: Context i.e metadata of the message
    :param coin: The coin symbol
    :return: The whole message (embed)
    """
    global channel
    await client.send_typing(ctx.message.channel)
    stats = request_database.stats_sql.Stats(ctx.message.author)
    try:
        for i in coin:
            await stats.stats_add("?topia", i.lower())
            cryptopia = request_api.request_cryptopia.Cryptopia(i.lower(),ctx.message.author)
            result = await cryptopia.cryptopia_query()
            if channel == None:
                await client.send_message(ctx.message.channel,ctx.message.author.mention,embed=result)
            else:
                await client.send_message(channel, ctx.message.author.mention, embed=result)
    except Exception as e:
        print("Global Error on ?topia\n",e)

@client.command(pass_context=True)
async def finex(ctx,*coin):
    """
    Request on a cryptocurrency which is on Bitfinex ||  ex : ?finex eth
    :param ctx: Context i.e metadata of the message
    :param coin: The coin symbol
    :return: The whole message (embed)
    """
    global channel
    await client.send_typing(ctx.message.channel)
    stats = request_database.stats_sql.Stats(ctx.message.author)
    try:
        for i in coin:
            await stats.stats_add("?finex", i.lower())
            bitfinex = request_api.request_bitfinex.Bitfinex(i.lower(),ctx.message.author)
            result = await bitfinex.bitfinex_query()
            if channel == None:
                await client.send_message(ctx.message.channel,ctx.message.author.mention,embed=result)
            else:
                await client.send_message(channel, ctx.message.author.mention, embed=result)
    except Exception as e:
        print("Global Error on ?finex\n",e)

@client.command(pass_context=True)
async def binance(ctx,*coin):
    """
    Request on a cryptocurrency which is on Binance ||  ex : ?binance eth
    :param ctx: Context i.e metadata of the message
    :param coin: The coin symbol
    :return: The whole message (embed)
    """
    global channel
    await client.send_typing(ctx.message.channel)
    stats = request_database.stats_sql.Stats(ctx.message.author)
    try:
        for i in coin:
            await stats.stats_add("?binance",i.lower())
            binance = request_api.request_binance.Binance(i.lower(),ctx.message.author)
            result = await binance.binance_query()
            if channel == None:
                await client.send_message(ctx.message.channel,ctx.message.author.mention,embed=result)
            else:
                await client.send_message(channel, ctx.message.author.mention, embed=result)
    except Exception as e:
        print("Global Error on ?binance\n",e)

@client.command(pass_context=True)
async def whale(ctx,arg,limit=4):
    """
    Request for all the whale order || ex : ?whale xzc 6
    :param ctx: Context i.e metadata of the message
    :param arg: The coin symbol
    :param limit: The limit in BTC
    :return: The whole message (embed)
    """
    global channel
    await client.send_typing(ctx.message.channel)
    stats = request_database.stats_sql.Stats(ctx.message.author)
    try:
        await stats.stats_add("?whale", "")
        whale = request_api.request_whale.whale(arg,ctx.message.author)
        result = await whale.query_whale(limit)
        if channel == None:
            await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=result)
        else:
            await client.send_message(channel, ctx.message.author.mention, embed=result)
    except Exception as e:
        print("Global Error on ?whale\n",e)

@client.command(pass_context=True)
async def cmc(ctx):
    """
    Request for the global data of coinmarketcap || ex : ?cmc
    :param ctx: Context i.e metadata of the message
    :return: The whole message (embed)
    """
    global channel
    await client.send_typing(ctx.message.channel)
    stats = request_database.stats_sql.Stats(ctx.message.author)
    try:
        await stats.stats_add("?cmc", "")
        cmc = request_api.request_marketcap.Coinmarketcap()
        result = await cmc.cmc_query(ctx.message.author)
        if channel == None:
            await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=result)
        else:
            await client.send_message(channel, ctx.message.author.mention, embed=result)
    except Exception as e:
        print("Global Error on ?cmc\n",e)

@client.command(pass_context=True)
async def top(ctx):
    """
    Request for the highest change of the day (neg and pos) || ex : ?top
    :param ctx: Context i.e metadata of the message
    :return: The whole message (embed)
    """
    global channel
    await client.send_typing(ctx.message.channel)
    stats = request_database.stats_sql.Stats(ctx.message.author)
    try:
        await stats.stats_add("?top", "")
        top = request_api.request_top.Topcoin()
        result = await top.query_top(ctx.message.author)
        if channel == None:
            await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=result)
        else:
            await client.send_message(channel, ctx.message.author.mention, embed=result)
    except Exception as e:
        print("Global Error on ?top\n",e)

@client.command(pass_context=True)
async def db(ctx,arg,rank=None,coin=None,*comment):
    """
    See ?db info for more info
    :param ctx: Context i.e metadata of the message
    :param arg: The coin
    :param rank: The rank that we want
    :param coin: The coin symbol
    :param comment: The comment of the coin
    :return: The whole message (embed)
    """
    await client.send_typing(ctx.message.channel)
    try:
        comment = ' '.join(comment)
        db = request_database.list_sql.Listsql(ctx.message.author)
        embed = db.db_query(arg,rank,coin,comment)
        await client.send_message(ctx.message.channel,ctx.message.author.mention,embed=embed)
    except Exception as e:
        print("Global Error on ?db\n",e)

@client.command(pass_context=True)
async def btc(ctx):
    """
    Request the price of the btc from many exchanges || ex : ?btc
    :param ctx: Context i.e metadata of the message
    :return: The whole message (embed)
    """
    global channel
    await client.send_typing(ctx.message.channel)
    stats = request_database.stats_sql.Stats(ctx.message.author)
    await stats.stats_add("?btc", "")
    btc = request_api.request_btc.bitcoin()
    json = await btc.fetch()
    result = btc.affichage(json,ctx.message.author)
    if channel == None:
        await client.send_message(ctx.message.channel, ctx.message.author.mention, embed=result)
    else:
        await client.send_message(channel, ctx.message.author.mention, embed=result)

@client.command(pass_context=True)
async def stats(ctx,arg=None):
    """
    The stats of the command which has been used on the discord ||ex ?stats
    :param ctx: Context i.e metadata of the message
    :param arg: No arg
    :return: The whole message (embed)
    """
    await client.send_typing(ctx.message.channel)
    try:
        db = request_database.stats_sql.Stats(ctx.message.author)
        conn = db.connect(arg)
        data = db.get(conn,arg)
        embed = db.get_affichage(data,arg)
        await client.send_message(ctx.message.channel,ctx.message.author.mention,embed=embed)
    except Exception as e:
        print("Global Error on ?db\n",e)

@client.command(pass_context=True)
async def order(ctx,price,profit,loss):
    """
    To simulate an order on Bittrex with a TP and SL || ex : ?order 0.005 5 5
    :param ctx: Context i.e metadata of the message
    :param price: The price in satoshi or bitcoin
    :param profit: The % of profit needed
    :param loss: The % of loss needed
    :return: The whole message (emebed)
    """
    await client.send_typing(ctx.message.channel)
    stats = request_database.stats_sql.Stats(ctx.message.author)
    await stats.stats_add("?order", "")
    try:
        the_order = side_info.order_info.Order(ctx.message.author)
        embed = the_order.order(price,profit,loss)
        await client.send_message(ctx.message.channel,ctx.message.author.mention,embed=embed)
    except Exception as e:
        print("Global Error on ?order\n",e)

@client.command(pass_context=True)
async def conv(ctx,coin,qty):
    """
    To convert an amount of cryptocurrency in dollars ||ex ?conv xzc 100
    :param ctx: Context i.e metadata of the message
    :param coin: The coin
    :param qty: The quantity
    :return: The whole message (embed)
    """
    await client.send_typing(ctx.message.channel)
    stats = request_database.stats_sql.Stats(ctx.message.author)
    await stats.stats_add("?conv", "")
    try:
        conv = side_info.conv_price.Conv(ctx.message.author)
        data = await conv.price(coin,qty)
        embed = conv.affichage(data,coin,qty)
        await client.send_message(ctx.message.channel,ctx.message.author.mention, embed=embed)
    except Exception as e:
        print("Global Error on ?conv\n",e)

@client.command(pass_context=True)
async def name(ctx,coin):
    """
    Ask for the full name of a symbol
    :param ctx: Context i.e metadata of the message
    :param coin: The symbol of the coin
    :return: The whole message (embed)
    """
    await client.send_typing(ctx.message.channel)
    stats = request_database.stats_sql.Stats(ctx.message.author)
    await stats.stats_add("?name", "")
    try:
        coin_name = side_info.name.Name(ctx.message.author,coin.lower())
        data = await coin_name.query_name()
        embed = await coin_name.affichage(data)
        await client.send_message(ctx.message.channel,ctx.message.author.mention, embed=embed)
    except Exception as e:
        print("Global Error on ?name\n",e)

@client.command(pass_context=True)
async def infos(ctx):
    """
    The help command in embed version || ex : ?help
    :param ctx: Context i.e metadata of the message
    :return: The whole message (embed)
    """
    await client.send_typing(ctx.message.channel)
    stats = request_database.stats_sql.Stats(ctx.message.author)
    await stats.stats_add("?info", "")
    try:
        info = side_info.info.Info(ctx.message.author)
        embed = info.info()
        await client.send_message(ctx.message.channel,ctx.message.author.mention, embed=embed)
    except Exception as e:
        print("Global Error on ?info\n",e)

@client.command(pass_context=True)
async def event(ctx,limit=0):
    """
    Query coincalendar to get the last event ||ex : ?event ?event 1
    :param ctx: Context i.e metadata of the message
    :param limit: The next page
    :return: The whole message (embed)
    """
    await client.send_typing(ctx.message.channel)
    stats = request_database.stats_sql.Stats(ctx.message.author)
    await stats.stats_add("?event", "")
    try:
        event = side_info.event_crypto.Event_Crypto(ctx.message.author)
        embed = await event.get_event(limit)
        await client.send_message(ctx.message.channel,ctx.message.author.mention, embed=embed)
    except Exception as e:
        print("Global Error on ?event\n",e)

@client.command(pass_context=True)
async def money(ctx,limit=0):
    await client.send_typing(ctx.message.channel)
    dona = side_info.donate.Donate()
    embed = dona.affichage()
    await client.send_message(ctx.message.channel,embed=embed)
    print("Global error on ?donate\n",e)

@client.command(pass_context=True)
async def sum(ctx,url=None,limit=4):
    """
    To get a summary of an article || ex : ?sum http://www.lemonde.fr 5
    :param ctx: Context i.e metadata of the message
    :param url: The url of the article
    :param limit: The limit in lines lower = shorter
    :return: The whole message (embed)
    """
    await client.send_typing(ctx.message.channel)
    stats = request_database.stats_sql.Stats(ctx.message.author)
    await stats.stats_add("?order", "")
    sum = side_info.sumarize.Sumarize(ctx.message.author,url,limit)
    list_v = sum.sum()
    await client.send_message(ctx.message.channel,list_v[0][0])
    await client.send_message(ctx.message.channel,list_v[0][1])

@client.command(pass_context=True)
async def twitter(ctx,param):
    """
    Need some fix, don't use it
    :param ctx:
    :param param:
    :return:
    """
    if param == "enable":
        chan_id = await get_chan_chan()
        channel = discord.Object(id=chan_id)
        twit = twitty.twittos.Twittos(client, channel)
        await client.send_message(ctx.message.channel, "```Le twitter est maintenant activé!```")
        try:
            client.loop.create_task(background_twitter(chan_id,twit))
        except Exception as e :
            print("Erreur Twitter",e)

'''            
@client.command(pass_context=True)
async def members(ctx):
    serv_val = "La CryptoSphère"
    for serv in client.servers:
        j=0
        for i in serv.members:
            print(j,i)
            j+=1
        await client.send_message(ctx.message.channel, "Nombre de personnes : " + str(j) + " Serv : "+ str(serv.name))
'''

"""
Fonction hors scope du bot
get_chan_chan = récupérer le chan pour le twitter
background_twitter = lancer le process de fond twitter
redirect_chan = = récupérer un chan pour redirection
"""

async def get_chan_chan():
    serv_val = "Unknown"
    chan_val = "Unknown"
    chan_id = -1
    with open("twitter.config", "r", encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i == 8:
                value = line.split('"')
                serv_val = value[1].rstrip()
            if i == 9 :
                value = line.split('"')
                chan_val = value[1].rstrip()
    for serv in client.servers:
        if serv.name == serv_val:
            for i in serv.channels:
                if i.name == chan_val:
                    return i.id
                else:
                    chan_id = -1
    return chan_id

async def background_twitter(chan,twit):
    await client.wait_until_ready()
    twit.launch_listener()
    return twit

async def redirect_chan():
    with open("twitter.config", "r", encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i == 8:
                value = line.split('"')
                serv_val = value[1].rstrip()
            if i ==11:
                value = line.split('"')
                chan_val = value[1]
        for serv in client.servers:
            if serv.name == serv_val:

                for i in serv.channels:
                    if i.name == chan_val:
                        channel = discord.Object(id=i.id)
                        return channel
                    else:
                        pass
    return -1

#Put your secret Discord Dev App Token between the quotes
client.run('')
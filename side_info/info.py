from random import randint
import datetime
import discord

class Info():
    def __init__(self,auth):
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        self.auth = str(auth).split("#")
        self.auth = self.auth[0]
        return

    def info(self):
        all = "!all [coins(s)] : Request on all Exchanges\n"
        rex = "!rex [coin(s)] : Request on Bittrex\n"
        finex = "!finex [coin(s)] : Request on Bitfinex\n"
        polo = "!polo [coin(s)] : Request on Poloniex\n"
        topia = "!topia [coin(s)] : Request on Cryptopia\n"
        binance = "!binance [coin(s)] : Request on Binance\n\n"
        btc = "!btc : Request on BTC price\n"
        top= "!top : Request about the best/worst tendancies\n"
        cmc = "!cmc : Request on the MarketCap\n\n"
        order = "!order [price][win][lose] : To estimate your possible wins/losses\n"
        conv = "!conv [coin][nombre_coin] : To know the coin's price in BTC/USD\n"
        name = "!name [coin] : Request about the Coin itself and some side infos    KO POUR LE MOMENT\n"
        stats = "!stats {Coin OU Command} : Retrieve the stats of a coin/command\n"
        whale = "!whale [Coin]{Limit in BTC} : Retrieve the big order\n"
        info = "!info : Know all the bot commands\n"
        list = "!db info : Retrieve data about the commands used on the server\n"
        donate = "!donate : Give me money please ...\n"
        event = "!event {If following page : 1,2,3,etc} : Display the next events\n\n"
        sum = "!sum [lien url]{Nombre de phrases à retourner} : Fait le résumé d'un article\n"


        data_info = "```css\n" + all + rex + finex + polo + topia + binance + btc + top + cmc + order + conv + name + stats + whale +  event + list + info + donate + sum +  "```"

        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.set_thumbnail(url="")
        embed.set_footer(text="Request achieved on")
        embed.add_field(name=":star2: Request about Coinbot's commands",
                        value="Here are the informations I could retrieve " + self.auth,
                        inline=False)
        embed.add_field(name=":information_source: Informations about Coinbot", value=data_info)
        return embed


    '''
    def info2(self):
        sum = "?sum [lien url]{Nombre de phrases à retourner} : Fait le résumé d'un article\n"
        data_info = "```css\n" + sum + "```"

        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.set_thumbnail(url="")
        embed.set_footer(text="Requête en date du")
        embed.add_field(name=":information_source: Informations sur Celestina", value=data_info)
        return embed
    '''
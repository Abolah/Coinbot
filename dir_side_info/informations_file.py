from random import randint
import datetime
import discord


class Class_Info:
    def __init__(self, auth):
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        self.auth = str(auth).split("#")
        self.auth = self.auth[0]
        return

    def function_informations(self):
        btc = "!btc\n"
        mexbook = "!mexbook\n"
        all = "!all [coins(s)]\n"
        finex = "!fnx [coin(s)]\n"
        binance = "!bnc [coin(s)]\n"
        rex = "!rex [coin(s)]\n"
        polo = "!polo [coin(s)]\n"
        topia = "!topia [coin(s)]\n"
        hitbtc = "!hit [coin(s)]\n\n"
        top = "!top\n"
        cmc = "!cmc\n"
        mini = "!mini [coin(s)]\n"
        order = "!order [price][profit][stop-loss]\n"
        whale = "!whale [Coin][Limit in BTC]\n"
        event = "!event\n\n"
        infos = "!infos\n"
        help = "!help [command name]\n"
        conv = "!convert [coin][number of coins]\n"
        balance = "!balance [coin][address]\n"
        name = "!name [coin]\n"
        sum = "!sum [url]\n"
        bot = "!bot\n"
        updates = "!updates\n"
        help_cmd = "Type !help followed by the name of the command (without the '!'). \n For Example: !help order."
        update = " Please type !updates regularly to know about Coinbot's latest updates. This way you wont miss any new feature."

        data_info = "```css\n" + btc + mexbook + all + finex + binance + rex + polo + topia + hitbtc + "```"
        coins_info = "```css\n" + top + cmc + mini + order + whale + event + "```"
        side_info = "```css\n" + infos + help + conv + balance + name + sum + bot + updates + "```"
        help_info = "```" + help_cmd + "```"
        update_info = "```" + update + "```"
        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/393197371254767616/400637492191035404/bbot.png")
        embed.set_footer(text="Request achieved :")
        embed.add_field(name=":hammer: Version", value="4.2", inline=False)
        embed.add_field(name=":moneybag: Exchanges Commands", value=data_info)
        embed.add_field(name=":money_with_wings: Coins Commands", value=coins_info)
        embed.add_field(name=":robot: Side Commands", value=side_info)
        embed.add_field(name=":information_source: Do you need help about a command ?", value=help_info)
        embed.add_field(name=":information_source: Coinbot has updates !", value=update_info)

        return embed

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
        all = "!all [coins(s)]\n"
        finex = "!fnx [coin(s)]\n"
        binance = "!bnc [coin(s)]\n"
        rex = "!rex [coin(s)]\n"
        polo = "!polo [coin(s)]\n"
        topia = "!topia [coin(s)]\n"
        hitbtc = "!hit [coin(s)]\n\n"
        top = "!top\n"
        cmc = "!cmc\n"
        order = "!order [price] [profit][stop-loss]\n"
        whale = "!whale [Coin] [Limit in BTC]\n"
        event = "!event\n\n"
        infos = "!infos\n"
        help = "!help [command name]\n"
        conv = "!convert [coin][number of coins]\n"
        name = "!name [coin]\n"
        sum = "!sum [url]\n"
        bot = "!bot\n"
        help_cmd = "Type !help followed by the name of the command (without the '!'). \n For Example: !help order \n This will display the help about the order command"

        data_info = "```css\n" + all + rex + finex + polo + topia + binance + hitbtc + btc + top + cmc + order + whale + event + infos + help + conv + name + sum + bot + "```"
        help_info = "```" + help_cmd + "```"
        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/393197371254767616/400637492191035404/bbot.png")
        embed.set_footer(text="Request achieved :")
        embed.add_field(name=":hammer: Version", value="2.7")
        embed.add_field(name=":star2: Request about Coinbot's commands",
                        value="Here are the informations I could retrieve " + self.auth,
                        inline=False)
        embed.add_field(name=":information_source: Informations about Coinbot", value=data_info)

        embed.add_field(name=":information_source: Do you need help about a command ?", value=help_info)
        return embed

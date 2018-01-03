from random import randint
import datetime
import discord


# event = "!event {If following page : 1,2,3,etc} : Display the next events\n\n"


class Info:
    def __init__(self, auth):
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        self.auth = str(auth).split("#")
        self.auth = self.auth[0]
        return

    def info(self):
        all = "!all [coins(s)]\n"
        btc = "!btc\n"
        rex = "!rex [coin(s)]\n"
        finex = "!finex [coin(s)]\n"
        polo = "!polo [coin(s)]\n"
        topia = "!topia [coin(s)]\n"
        binance = "!binance [coin(s)]\n\n"
        top = "!top\n"
        cmc = "!cmc\n"
        order = "!order [price] [profit][stop-loss]\n"
        whale = "!whale [Coin] [Limit in BTC]\n"
        event = "!event\n\n"
        info = "!infos\n"
        help = "!help [command name]\n"
        conv = "!conv [coin][number of coins]\n"
        name = "!name [coin]\n"
        sum = "!sum [url]\n\n"
        stats = "!stats\n"
        list = "!db info\n\n"
        wolf = "!wolf\n"
        code = "!bot\n"
        money = "!ressources\n"
        help_cmd = "Type !help followed by the name of the command (without the '!'). \n For Example: !help order \n This will display the help about the order command"

        data_info = "```css\n" + all + btc + rex + finex + polo + topia + binance + top + cmc + order + whale + event + info + help + conv + name + sum + stats + list + wolf + code + money + "```"
        help_info = "```" + help_cmd + "```"
        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.set_thumbnail(url="https://cdn4.iconfinder.com/data/icons/space-and-astronomy-1/800/robot-512.png")
        embed.set_footer(text="Request achieved on")
        embed.add_field(name=":hammer: Version", value="1.9")
        embed.add_field(name=":star2: Request about Coinbot's commands",
                        value="Here are the informations I could retrieve " + self.auth,
                        inline=False)
        embed.add_field(name=":information_source: Informations about Coinbot", value=data_info)

        embed.add_field(name=":information_source: Do you need help about a command ?", value=help_info)
        return embed

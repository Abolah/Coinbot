import discord
import datetime
from random import randint


class Class_Order:
    def __init__(self, auth):
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        self.auth = str(auth).split("#")
        self.auth = self.auth[0]
        return

    def function_order(self, price, profit, loss):
        print("Price : " + price)
        if float(price) > 1:
            price = float(float(price) / (10 ** 8))

        fees = 0.0025 * float(price)
        price = float(price) + fees
        name = "\n0.25% Trading fee included"
        fees_sl1 = (float(price) + float(float(loss) / 100) * float(price)) * 0.0025
        fees_sl2 = (float(price) + float(float(loss) / 200) * float(price)) * 0.0025
        sl1 = float(price) - float(float(loss) / 100) * float(price) - fees_sl1 + 2 * fees
        sl2 = float(price) - float(float(loss) / 200) * float(price) - fees_sl2 + 2 * fees
        stop_loss2 = "-{0:.2f}".format(float(loss) / 2.0) + "% Stop loss : {0:.8f}".format(sl2) + "\n"
        stop_loss1 = "-{0:.2f}".format(float(loss) / 1.0) + "% Stop loss : {0:.8f}".format(sl1) + "\n"

        fees_tp1 = (float(price) + float(float(profit) / 100) * float(price)) * 0.0025
        fees_tp2 = (float(price) + float(float(profit) / 200) * float(price)) * 0.0025
        tp1 = float(price) + float(float(profit) / 100) * float(price) + fees_tp1
        tp2 = float(price) + float(float(profit) / 200) * float(price) + fees_tp2
        take_profit1 = "{0:.2f}".format(float(profit) / 1.0) + "% Take profit : {0:.8f}".format(tp1) + "\n"
        take_profit2 = "{0:.2f}".format(float(profit) / 2.0) + "% Take profit : {0:.8f}".format(tp2) + "\n"
        achat = "No Gain : {0:.8f}".format(float(price + fees))

        data_achat = "```css\n" + take_profit1 + take_profit2 + "```"
        data_vente = "```css\n" + stop_loss2 + stop_loss1 + "```"
        data_annexe = "```css\n" + achat + name + "```"

        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.set_thumbnail(url="https://files.coinmarketcap.com/static/img/coins/32x32/bitcoin.png")
        embed.set_footer(text="Request achieved :")
        embed.add_field(name=":star2: Request about the orders of " + self.auth,
                        value="Here are the information that I could retrieve " + self.auth,
                        inline=False)
        embed.add_field(name=":chart_with_upwards_trend: Information about your take profit", value=data_achat,
                        inline=True)
        embed.add_field(name=":chart_with_downwards_trend: Information about your stop loss", value=data_vente,
                        inline=True)
        embed.add_field(name=":information_source: Additional information", value=data_annexe, inline=True)
        return embed

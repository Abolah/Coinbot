import sqlite3
import discord
import datetime
from random import randint
from string import capwords

class Stats():
    def __init__(self,author):
        auth = str(author).split("#")
        self.author = capwords(str(auth[0]))
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        return

    def connect(self,arg=None):
        """
        Connection à la BDD
        :param arg: Si jamais on doit créer la première table
        :return: Le connecteur à la bdd
        """
        conn = sqlite3.connect("stats.sqlite")
        if arg =="init":
            self.create(conn)
        return conn
    def create(self,conn):
        """
        Création de la table pour la première initialisation de la bdd
        :param conn: Le connecteur à la base de donnée
        :return: Return 0 si tout ok
        """
        c = conn.cursor()
        try:
            c.execute('''   
                CREATE TABLE IF NOT EXISTS stats (id INTEGER PRIMARY KEY , command TEXT,
                                   coin TEXT)
            ''')
            conn.commit()
            create = 0
        except Exception as e:
            print("Create erorr : ",e)
            create = e
        return create

    def add(self,conn,command,coin):
        """
        Rajoute une commande à la bdd dans le but de faire des stats
        :param conn: Le connecteur à la bdd
        :param command: La commande en question
        :param coin: Si il y a un coin en argument on le rajoute
        :return: 0 si tout ok
        """
        task = (command,coin)
        sql = """INSERT INTO stats (command,coin) VALUES (?,?)"""
        c = conn.cursor()
        try:
            c.execute(sql, task)
            conn.commit()
        except Exception as e:
            print("Add error : ", e)
        return 0

    def get(self,conn,arg):
        """
        Retourne les stats voulus : TODO
        :param conn:
        :return:
        """
        c = conn.cursor()
        data = []
        try:
            if arg == None:
                c.execute("SELECT command,count(*) FROM stats GROUP BY command")
                conn.commit()
                data.append(c.fetchall())
                c.execute("SELECT coin,count(*) FROM stats GROUP BY coin")
                conn.commit()
                data.append(c.fetchall())
            elif "?" in arg:
                c.execute("SELECT count(*) FROM stats WHERE command = '" + str(arg) +"'")
                conn.commit()
                data = c.fetchall()
            else:
                c.execute("SELECT count(*) FROM stats WHERE coin = '" + str(arg) +"'")
                conn.commit()
                data = c.fetchall()
        except Exception as e:
            return e

        return data

    def get_affichage(self,data,arg):

        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.set_thumbnail(url="https://files.coinmarketcap.com/static/img/coins/32x32/bitcoin.png")
        embed.set_footer(text="has been succesfully removed")
        embed.add_field(name=":star2: Request on the coin on the server",
                        value="Here are the informations I could retrieve" + str(self.author),
                        inline=False)

        if arg == None:
            limit = 4
            rank = 1
            list_command = sorted(data[0], key=lambda x: x[1], reverse=True)
            value_command = "Most used commands are:\n\n"
            for i in range(0,len(list_command)):
                if i > 4:
                    break
                else:
                    value_command = value_command + "[Rank " + str(i+1) + "] " + str(list_command[i][0]) + " has been asked " + str(list_command[i][1]) + " time\n"
            list_coin = sorted(data[1], key=lambda x: x[1], reverse=True)
            value_coin = "Most asked coins :\n\n"
            for i in range(0,len(list_coin)):
                if i > limit:
                    break
                else:
                    if list_coin[i][0] == "":
                        limit += 1
                    else:
                        value_coin = value_coin + "[Rank " + str(rank) + "] " + str(list_coin[i][0]).upper() + " has been asked " + str(list_coin[i][1]) + " time \n"
                        rank += 1
            result_command = "```css\n" + value_command + "```"
            result_coin = "```css\n" + value_coin + "```"
            embed.add_field(name=":boom: Commands Informations", value=result_command, inline=True)
            embed.add_field(name=":boom: Coin Informations", value=result_coin, inline=True)

        elif "?" in arg:
            result = "```css\nCommands " + arg + " has been asked " + str(data[0][0]) + " times on the bot```"
            embed.add_field(name=":boom: Command Information " + arg, value=result, inline=True)
        else:
            result = "```css\nCoin " + arg.upper() + " ahas been asked " + str(data[0][0]) + " times on the bot```"
            embed.add_field(name=":boom: Coin Informations" + arg.upper(), value=result, inline=True)

        return embed

    async def stats_add(self,command,coin):
        """
        Commande à utiliser depuis l'extérieur pour rajouter la query à chaque fois
        :param command: La commande à rajouter
        :param coin: Le coin si jamais il y en a un
        :return: 0
        """
        conn = self.connect()
        self.add(conn,command,coin)
        return 0
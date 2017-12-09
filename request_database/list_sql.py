import sqlite3
import discord
import datetime
from string import capwords
from random import randint


class Listsql:
    def __init__(self, author):
        auth = str(author).split("#")
        self.author = capwords(str(auth[0]))
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        return

    @staticmethod
    def connect():
        """
        Initialise la connection à la base de donnée
        :return: Le connecteur à la bdd
        """
        conn = sqlite3.connect("crypto.sqlite")
        return conn

    @staticmethod
    def create(conn):
        c = conn.cursor()
        try:
            c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY , rank INTEGER, coin TEXT, pseudo TEXT, comment TEXT)''')
            conn.commit()
            create = "Database initialisé"
        except Exception as e:
            print("Create erorr : ", e)
            create = str(e)
        return create

    @staticmethod
    def close(conn):
        """
        Fermeture de la connexion à la base de donnée
        :param conn: Le connecteur à la bdd
        :return: 0 / Error
        """
        try:
            conn.close()
            close = 0
        except Exception as e:
            print("Close error : ", e)
            close = e
        return close

    def check_add(self, conn, rank, coin, comment):
        try:
            c = conn.cursor()
            c.execute("SELECT rank FROM users WHERE pseudo='" + self.author + "'")
            conn.commit()
            for i in c.fetchall():
                if int(i[0]) == int(rank):
                    return "You already have a coin at this rank, delete it first!\n"
        except Exception as e:
            print(e)

        try:
            if len(comment) > 120:
                return "Your comment can't excess 280 chars.\n"
            int(rank)
            if 6 > int(rank) > 0:
                if len(coin) < 8:
                    return 0
                else:
                    return "This coin isn't valid\n"
        except Exception as e:
            print(e)

        return "This rank isn't valid\n"

    def add(self, conn, rank, coin, comment):
        check = self.check_add(conn, rank, coin, comment)
        if check != 0:
            return "```" + check + "```"
        task = (rank, coin.upper(), self.author, comment)
        sql = """INSERT INTO users (rank,coin,pseudo,comment) VALUES (?,?,?,?)"""
        c = conn.cursor()
        try:
            c.execute(sql, task)
            conn.commit()
            add = "Your coin is added!\n"
        except Exception as e:
            print("Add error : ", e)
            add = e
        return "```" + str(add) + "```"

    def delete(self, conn, arg):
        """
        Supprime un coin de la base de donnée à partir du rank ou du coin pour l'utilisateur ayant fait la requête
        :param conn:
        :param arg:
        :return:
        """
        c = conn.cursor()
        try:
            int(arg)
            stat = " rank = " + arg
            delete = "Your coin ranked" + arg + " has been succesfully removed\n"
        except:
            stat = " coin = '" + arg.upper() + "'"
            delete = "Your coin " + arg.upper() + " has been succesfully removed\n"

        sql = "DELETE FROM users WHERE pseudo = '" + self.author + "' AND " + stat
        try:
            c.execute(sql)
            if c.rowcount == 0:
                delete = "Sorry but this coin or rank isn't in the ranking\n"
            conn.commit()
        except Exception as e:
            print("Delete error : ", e)
            delete = e
        return "```" + delete + "```"

    def get(self, conn, arg):
        """
        Retourne la liste du coin en question ou du pseudo avec les coins liés à ce pseudo
        :param conn: Le connecteur à db
        :param arg: coin ou pseudo
        :return:
        """
        pseudo = capwords(arg)
        coin = arg.upper()
        c = conn.cursor()
        try:
            c.execute("SELECT * FROM users WHERE coin = '" + coin + "'")
            get = c.fetchall()
            if not get:
                c.execute("SELECT * FROM users WHERE pseudo = '" + pseudo + "'")
                get = c.fetchall()
            if not get:
                return "```Sorry but I don't have any informations about this coin/nickname```"
            conn.commit()
        except Exception as e:
            print("Get error : ", e)
            return e
        data = self.format_get(get)
        return data

    @staticmethod
    def format_get(list):
        data = ""
        sort_l = sorted(list, key=lambda x: x[1])
        for i in sort_l:
            data = data + "Rank: " + str(i[1]) + " [" + str(i[2]) + "] " + str(i[3]) + " \nComment : " + str(
                i[4]) + "\n"
        return "```css\n" + data + "```\n"

    def affichage(self, data):
        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.set_thumbnail(url="https://files.coinmarketcap.com/static/img/coins/32x32/bitcoin.png")
        embed.set_footer(text="Request achieved on")
        embed.add_field(name=":star2: Request on the coin on the server",
                        value="Here are the informations I could retrieve" + str(self.author),
                        inline=False)
        embed.add_field(name=":boom: DataBase Informations", value=data, inline=True)
        return embed

    def db_query(self, arg, rank, coin, comment):
        conn = self.connect
        if arg.lower() == "add":
            data = self.add(conn, rank, coin, comment)
            result = self.affichage(data)
        elif arg.lower() == "create":
            data = self.create(conn)
            result = self.affichage(data)
        elif arg.lower() == "del":
            data = self.delete(conn, rank)
            result = self.affichage(data)
        elif arg.lower() == "get":
            data = self.get(conn, rank)
            result = self.affichage(data)
        elif arg.lower() == "info":
            data = self.info()
            result = self.affichage(data)
        elif arg.lower() == "init":
            data = self.create(conn)
            result = self.affichage(data)
        else:
            result = "Command isn't valid. Type !db for more informations"
        self.close(conn)
        return result

    @staticmethod
    def info():
        db = "?db [command]\n"
        add = "\r?db add [Rank] [Coin] {Comment}\nExemple ?db add 5 eth I like Vitalik\n"
        delete = "\r?db del [Rank] OU [Coin]\nExemple : ?db del 5\n"
        get = "\r?db get [Coin] OU [Nickname]\nExemple : ?db get xzc\n"
        info = "\r?db info\n"
        return "```css\n" + db + add + delete + get + info + "```"

    @staticmethod
    def debug(conn):
        c = conn.cursor()
        c.execute("SELECT * FROM users")
        conn.commit()
        print(c.fetchall())
        return

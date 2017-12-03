from twitty import stream_twitter
from tweepy import Stream
import tweepy
import os.path
import asyncio

class Twittos():
    def __init__(self,client,channel):
        """
        Initialisation de toutes les variables
        :param client: Le client discord
        :param channel: Le channel pour envoyer les messages
        """
        self.followers = []
        self.followers_id = []
        self.hashtag = []
        self.consumer_key = ''
        self.consumer_secret = ''
        self.access_token = ''
        self.access_secret = ''
        self.get_config()
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_secret)
        self.api = tweepy.API(self.auth)  # create an API object
        self.get_all_id()
        self.credential = self.api.verify_credentials()
        self.bot = client
        self.channel = channel
        return

    def get_config(self):
        """
        Permet de lire le fichier de config pour avoir les tokens
        :return:
        """
        with open(os.path.dirname(__file__) + "/../twitter.config","r") as f:
            for i,line in enumerate(f):
                if i == 0:
                    value = line.split('"')
                    self.consumer_key = value[1]
                elif i == 1:
                    value = line.split('"')
                    self.consumer_secret = value[1]
                elif i == 2:
                    value = line.split('"')
                    self.access_token = value[1]
                elif i == 3:
                    value = line.split('"')
                    self.access_secret = value[1]
                elif i == 5:
                    value = line.split('"')
                    hashtag = value[1].split(",")
                    for i in hashtag:
                        self.hashtag.append(i)
                elif i == 6:
                    value = line.split('"')
                    followers = value[1].split(",")
                    for i in followers:
                        self.followers.append(i)
                    break
        return

    def launch_listener(self):
        """
        Lancer le listener, rien de particulier
        :return:
        """
        self.l = stream_twitter.StdOutListener()
        self.l.set_discord(self.bot)
        self.l.set_channel(self.channel)
        self.l.set_id(self.followers_id)
        self.stream = Stream(self.auth, self.l)
        self.stream.filter(track=self.hashtag,follow=self.followers_id,async=True)
        return 0

    def kill_listener(self):
        self.stream.disconnect()
        return 0


    def get_all_id(self):
        for i in self.followers:
            try:
                user = self.api.get_user(i)
                self.followers_id.append(user.id_str)
            except:
                print(i,"No ID")
        print(self.followers_id)
        return

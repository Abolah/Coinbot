from bs4 import BeautifulSoup
import json
import discord
import datetime
import aiohttp
import async_timeout
import asyncio
import re
from random import randint


class Class_Events:
    def __init__(self, auth):
        self.auth = str(auth).split("#")
        self.auth = self.auth[0]
        self.time = datetime.datetime.now().timestamp()
        self.color = randint(0, 0xffffff)
        return

    async def function_get_html(self):
        data_http = ""
        generalevent = "http://www.coincalendar.info/"
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
            try:
                async with async_timeout.timeout(10):
                    async with session.get(generalevent) as resp:
                        if resp.status == 200:
                            data_http = await resp.text()
            except asyncio.TimeoutError as e:
                print(e)
                data_http = -1
        return data_http

    def function_stripwhite(self, text):
        lst = text.split('"')
        for i, item in enumerate(lst):
            if not i % 2:
                lst[i] = re.sub("\s+", "", item)
        return '"'.join(lst)

    def function_parsing(self, data):
        list_event = []
        if data == -1:
            return list_event.append(-1)

        soup = BeautifulSoup(data, "html.parser")
        for i in soup.find_all('script', attrs={"type": u"application/ld+json"}):
            data = str(i).replace('<script type="application/ld+json">', "						  	").replace(
                "</script>", "")
            try:
                data = json.loads(self.function_stripwhite(data).replace(",}", "}").replace("\n", "").replace("\r", ""))
                if data not in list_event:
                    list_event.append(data)
            except json.decoder.JSONDecodeError:
                try:
                    data = json.loads(self.function_stripwhite(data).replace(",}", "}"))
                    if data not in list_event:
                        list_event.append(data)
                except json.decoder.JSONDecodeError:
                    print("Invalid event : Delete")
        return list_event

    def function_display(self, list_event, limit):
        global date_2
        event_value = ""
        list_event_final = []
        date_now = datetime.datetime.now()
        date_1 = datetime.datetime.strptime(str(str(date_now.year) + "-" + str(date_now.month) + "-" + str(date_now.day)), "%Y-%m-%d")
        limit = limit * 10
        for i in list_event:
            try:
                date = str(i["startDate"]).split("T")
                date_2 = datetime.datetime.strptime(date[0], "%Y-%m-%d")
                print("Date_2 : " + date_2)
            except Exception as e:
                print("startdate", e)
            try:
                if date_2 >= date_1:
                    list_event_final.append(i)
            except Exception as e:
                print("No date available", e)
        if limit < len(list_event_final):
            for i in range(limit, len(list_event_final)):
                if i <= limit + 10:
                    date_event = str(list_event_final[i]["startDate"]).split("T")
                    event_value += "[" + date_event[0] + "] " + list_event_final[i]["name"] + "\n"
                else:
                    break
        else:
            event_value = "No more event to come sorry"

        event_value = "```css\n" + event_value + "```"
        embed = discord.Embed(colour=discord.Colour(self.color), url="https://discordapp.com",
                              timestamp=datetime.datetime.utcfromtimestamp(self.time))
        embed.set_thumbnail(url="https://files.coinmarketcap.com/static/img/coins/32x32/bitcoin.png")
        embed.set_footer(text="Request achieved on")
        embed.add_field(name=":star2: Request about the incoming events",
                        value="Here are the informations I could retrieve " +
                              self.auth, inline=False)
        embed.add_field(name=":floppy_disk: Information about the incoming event", value=event_value,
                        inline=True)
        return embed

    async def get_event(self, limit):
        data = await self.function_get_html()
        list_event = self.function_parsing(data)
        embed = self.function_display(list_event, limit)
        return embed

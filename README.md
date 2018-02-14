![CoinBot](https://cdn.discordapp.com/attachments/212339499076681739/408983409478598665/CoinBot_little.png)

# CoinBot

[![Build Status](https://travis-ci.org/Abolah/Coinbot.svg?branch=master)](https://travis-ci.org/Abolah/Coinbot)    [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![Discord Bots](https://discordbots.org/api/widget/367061304042586124.svg)](https://discordbots.org/bot/367061304042586124)

Coinbot is a Discord bot created in Python and used to display some useful informations about CryptoMarket trading.

Send me a discord message to @Abolah#1337 or @Abolaah on Twitter if you want informations about the hosting.

## If you want to test it, you can join this server :
* [CoinBot Test Server](https://discord.gg/PVyNRca)

## Getting Started

The bot is ready to deploy. Just add your Bot Secret token you created with your discord dev account.

### Prerequisites

You'll need python3.6 installed and some dependencies.

To Install Python3.6 you can follow this tutorial :

* [Tutorial](https://unix.stackexchange.com/questions/332641/how-to-install-python-3-6)

## Install dependencies

If you do not have pip, you can use the following

```
curl https://bootstrap.pypa.io/get-pip.py | python3.6
```

Install all the requirements :
```
python3.6 -m pip install -r requirements.txt
```

Those dependencies are :
```
discord aiohttp asyncio requests aylien-apiclient pymarketcal

```

### Installation

You don't need to install anything, just git clone the repository, put your secret token and launch main.py


```
python3.6 main.py
```
If you want to run the bot on a VPS you should install Screen and run the bot on another detached screen to not stop the bot.

```
screen -S CoinBot
python3.6 main.py
Ctrl A + D
```


To see if the bot is running correctly just run the command !infos
```
!infos
```
# The commands

```
!infos : List of all the available commands
```
```
!all [coin(s)] : Get the value of the coin on all exchanges it's listed on
```
```
!polo [coin(s)] : Get the value of the coin on Poloniex
```
```
!bnc [coin(s)] : Get the value of the coin on Binance
```
```
!topia [coin(s)] : Get the value of the coin on Cryptopia
```
```
!fnx [coin(s)] : Get the value of the coin on Bitfinex
```
```
!rex [coin(s)] : Get the value of the coin on Bittrex
```
```
!hit [coin(s)] : Get the value of the coin on HitBTC
```
```
!top : Get the highest gain and loss of the coins
```
```
!cmc : Get the MarketCap of all CryptoCoins
```
```
!btc : Get the value of the BTC on all major exchanges
```
```
!order [price][% win][% lose] :  To estimate a win/loss trade
Example : !order 750 5 10
```
```
!whale [coin] {Limit in BTC, based with 4 BTC}  :  Retrieve the Whale orders on the differents exchanges
Example : !whale xzc || !whale xzc 5
```
```
!stats  :  Retrieve the most used commands
Example : !stats || !stats !rex || !stats xzc
```
```
!name [name] :  Get the full name of the coin and some additionnal infos
Example : !name eth
```
```
!event {next page :1,2,3 etc} :  Retrieve the incoming events
Example : !event  || !event 2
```
```
!bot :  Display some informations about me and the bot
Example : !bot
```
```
!conv [coin][quantity] :  To convert the coin value in BTC/USD
Example : !conv eth 10.245
```
```
!sum [url]{limit} :  Shorten an article from a website
Example : !sum www.url.com
```

## Tools Used:

* [PyCharm](https://www.jetbrains.com/pycharm/) - Python IDE
* [Discord.py](https://github.com/Rapptz/discord.py) - Python wrapper for Discord


## Donation

If you want to help me with this bot. You can donate BTC and ETH to the following addresses
```
ETH(ERC20 friendly)  [abowallet.eth]
BTC  [1jc3V3T5mefuD9asa7en976NKVGssQuMq]
DOGE [D9zKYJgqnTWcu8ZCVzzKrqQkjzwuhymHh9]
LTC  [LQS415ftVrkSjjmFUyKNVBhY1fJzFLSKaz]
DASH [XkbrvfjnN1geyBJVe8igNwDYVFRPNWpRuz]
```

## Author
* **Abolah** - [Abolah](https://twitter.com/Abolaah)

## License

This project is under the GNU General Public License as seen in license.md

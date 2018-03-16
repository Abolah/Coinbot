![CoinBot](https://cdn.discordapp.com/attachments/212339499076681739/408983409478598665/CoinBot_little.png)

# CoinBot

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)   [![Codacy Badge](https://api.codacy.com/project/badge/Grade/4fea7d74f6ad46b8986776d4614bd612)](https://www.codacy.com/app/Abolah/Coinbot?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Abolah/Coinbot&amp;utm_campaign=Badge_Grade)

[![Discord Bots](https://discordbots.org/api/widget/367061304042586124.svg)](https://discordbots.org/bot/367061304042586124)

If you Like CoinBot don't forget to upvote it on clicking on the widget above.

Coinbot is a Discord bot created in Python and used to display some useful informations about CryptoMarket trading.


## If you want to test it or help me in the development, you can join this server :
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
If you want to run the bot on a VPS you should install Supervisor and run the bot on a supervisor instance so that the bot will automatically relaunch if it stop.

```
supervisorctl start CoinBot
```


To see if the bot is running correctly just run the command !infos
```
!infos
```

## The commands
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
!name [name] :  Get the full name of the coin and some additionnal infos
Example : !name eth
```
```
!event [coin] :  Retrieve the incoming events. Adding a coin is optional
Example : !event  || !event eth
```
```
!bot :  Display some informations about me and the bot
Example : !bot
```
```
!convert [coin][quantity] :  To convert the coin value in BTC/USD
Example : !convert eth 10.245
```
```
!balance [coin] [Address]
NOTE: Only BTC and ETH (with ERC20 tokens) are supported yet.
Example : !balance eth 0x670B7A9497f79Ef57BbFFFB553d979E7aD225344
          !balance token 0x670b7a9497f79ef57bbfffb553d979e7ad225344
          !balance btc 1jc3V3T5mefuD9asa7en976NKVGssQuMq
```
```
!sum [url]{limit} :  Shorten an article from a website
Example : !sum www.url.com
```
```
!updates : Display the Changelog in your Privates Messages
Example : !updates
```


## Donations
If you want to help me with this bot. You can donate to the following addresses
```
ETH(ERC20 friendly)  [abowallet.eth]
BTC  [1jc3V3T5mefuD9asa7en976NKVGssQuMq]
DOGE [D9zKYJgqnTWcu8ZCVzzKrqQkjzwuhymHh9]
LTC  [LQS415ftVrkSjjmFUyKNVBhY1fJzFLSKaz]
DASH [XkbrvfjnN1geyBJVe8igNwDYVFRPNWpRuz]
```

## Author
* **Abolah** - [Abolah](https://twitter.com/Abolaah)
* **Pridwen** - [Pridwen](https://github.com/Pridwen)

## License
This project is under the GNU General Public License as seen in license.md

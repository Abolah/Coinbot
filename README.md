# CoinBot

Coinbot is a Discord bot created in Python and used to display some usefull informations about CryptoMarket trading.

## Getting Started

The bot is ready to deploy. Just add your Bot Secret token you created with your discord dev account.

### Prerequisites

You'll need python3.6 installed and some dependancies.

To Install Python3.6 you can follow this tutorial :

* [Tutorial](https://unix.stackexchange.com/questions/332641/how-to-install-python-3-6)

```
discord aiohttp asyncio requests aylien-apiclient beautifulsoup4

beautifulsoup4 is used only for !event
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
!binance [coin(s)] : Get the value of the coin on Binance
```
```
!topia [coin(s)] : Get the value of the coin on Cryptopia
```
```
!finex [coin(s)] : Get the value of the coin on Bitfinex
```
```
!rex [coin(s)] : Get the value of the coin on Bittrex
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
!money :  Get the donation informations
Example : !money
If you want to modify the donation addresses you can go to Coinbot/side_info/donate.py
```
```
!conv [coin][quantité] :  To convert the coin value in BTC/USD
Example : !conv eth 10.245
```
```
!sum [url]{limit} :  Shorten an article from a website
Example : !sum www.url.com
```
```
!db [command] : Can stock someone favorite coin (up to 5 coin/person)

!db add [Rank] [Coin] {Commentaire} : Add a coin for the person using the command in the Database
Example !db add 5 eth I like Vitalik

!db del [Rank] OU [Coin] : Delete the coin depending on the rank or the coin itself for the person who uses the command
Example : !db del 5

!db get [coin] or [nickname] : Allow to retrieve the coin or the nickname of a person
Example : !db get xzc

!db info : Command's information
```

## Warning

Using the !stats command needs to init the database to start registering the stats
```
!stats init
```

Using the !db command needs to init the database to start registering the coins
```
!db init
```

## Tools Used:

* [PyCharm](https://www.jetbrains.com/pycharm/) - L'IDE de développement 
* [DIscord.py](https://github.com/Rapptz/discord.py) - Le wrapper de communication Discord pour python


## Donation

If you want to help me with this bot. You can donate BTC and ETH to the following addresses
```
ETH  [abowallet.eth]
BTC  [1jc3V3T5mefuD9asa7en976NKVGssQuMq]
```

## Autors

* **Pridwen** - *Forked from* [Pridwen](https://github.com/Pridwen/Celestina)
* **Abolah** - *Initial work* - [Abolah](https://github.com/Abolah)


## License

This project is under the GNU General Public License as seen in license.md
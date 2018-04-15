import binance_price_fetcher as BinancePriceFetcher
import bittrex_price_fetcher as BittrexPriceFetcher
import bot_db_functions as BotDbFunctions


#Fetch Fresh Data
db_helper = BotDbFunctions.BotDbFunctions()
db_helper.clear_db()


#Fetch Binance Data
binance_worker = BinancePriceFetcher.BinancePriceFetcher()
binance_worker.update_price_all()

#Fetch Bittrex Data
bittrex_worker = BittrexPriceFetcher.BittrexPriceFetcher()
bittrex_worker.update_price_all()

markets = db_helper.get_symbols()

for pairs in markets:
    db_helper.get_prices_from_markets(pairs[0])

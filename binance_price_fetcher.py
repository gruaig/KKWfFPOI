#!/usr/bin/python

class BinancePriceFetcher:


    from binance.client import Client
    import datetime
    from datetime import datetime
    import json
    import sqlite3
    from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, create_engine
    from sqlalchemy.sql import insert
    global datetime,sqlite3,requests,json,create_engine,MetaData,Table,insert,select,client


    exchange = 'BINANCE'



    client = Client(api_key, secret_key)

    def update_price_all(self):
        db = create_engine('sqlite:///:prices:', echo=False)
        metadata = MetaData(db)
        conn = db.connect()
        prices = Table('prices', metadata, autoload=True)

        ticker_data = client.get_all_tickers()
        for x in ticker_data:
            symbol = x['symbol']
            price  = x['price']

            ins = prices.insert().values(exchange=self.exchange, symbol=symbol,date=str(datetime.now()),price=price)
            ins.compile().params
            result = conn.execute(ins)
            #print self.exchange + ' ' + str(datetime.now()),symbol , price
            #Write to two tables one for historical one to overide


    def update_price(self,symbol):
        conn = sqlite3.connect('example.db')
        c = conn.cursor()
        #c.execute('''CREATE TABLE stocks
        #     (date text, symbol text, lastPrice real, lowPrice real, askPrice real)''')
        try:
            ticker = client.get_ticker(symbol=symbol)
            lastPrice = ticker['lastPrice']
            lowPrice  = ticker['lowPrice']
            askPrice  = ticker['askPrice']

            #c.execute("INSERT INTO stocks VALUES (str(datetime.now()),symbol,askPrice ,lowPrice,lastPrice)")
            print str(datetime.now())+ ' ' + symbol + ' askPrice: ' + askPrice + ' lowPrice: ' + lowPrice + ' lastPrice: ' + lastPrice
        except BinanceApiException as e:
            print(e)

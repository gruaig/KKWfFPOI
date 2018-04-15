#!/usr/bin/python

class BittrexPriceFetcher:


    from binance.client import Client
    import datetime
    from datetime import datetime
    from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, create_engine
    from sqlalchemy.sql import insert
    import json
    import sqlite3
    import requests
    

    global datetime,sqlite3,requests,json,create_engine,MetaData,Table,insert,select


    exchange = "BITTREX"

    def update_price_all(self):
        db = create_engine('sqlite:///:prices:', echo=False)
        metadata = MetaData(db)
        conn = db.connect()
        prices = Table('prices', metadata, autoload=True)



        ticker_data = requests.get("https://bittrex.com/api/v1.1/public/getmarketsummaries")
        json_data = json.loads(ticker_data.text)
        for name in json_data['result']:
            temp_name = name['MarketName'].split("-")
            symbol = temp_name[1]+temp_name[0]
            price = name['Last']

            ins = prices.insert().values(exchange=self.exchange, symbol=symbol,date=str(datetime.now()),price=price)
            ins.compile().params
            result = conn.execute(ins)
            #print self.exchange + ' ' + str(datetime.now()),symbol , price

            #print str(datetime.now()), x['symbol'] , x['price']
            #Write to two tables one for historical one to overide

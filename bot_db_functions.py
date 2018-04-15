class BotDbFunctions:

    import datetime
    from datetime import datetime
    from var_dump import var_dump
    from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, create_engine
    from sqlalchemy.sql import insert, select
    import sqlite3
    import logging

    logging.basicConfig()
    logging.getLogger('sqlalchemy').setLevel(logging.ERROR)

    global datetime,sqlite3,create_engine,MetaData,Table,insert,select

    def clear_db(self):
        db = create_engine('sqlite:///:prices:', echo=False)
        metadata = MetaData(db)
        conn = db.connect()
        conn.execute('delete from prices')

    def get_symbols(self):
        symbol_list = []
        db = create_engine('sqlite:///:prices:', echo=False)
        metadata = MetaData(db)
        conn = db.connect()
        result = conn.execute('select symbol from prices')
        for row in result:
            symbol_list.append(row)

        result.close()
        return symbol_list

    def get_prices_from_markets(self,symbol):
        db = create_engine('sqlite:///:prices:', echo=False)
        metadata = MetaData(db)
        s = 'select * from prices where price="' + str(symbol) + '"'
        conn = db.connect()
        result = conn.execute(s)
        for v in result:
            print v



         

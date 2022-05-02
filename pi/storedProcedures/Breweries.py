#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

from storedProcedures.Helpers import unpack_sqlite3_objects, unpack_sqlite3_object


class Breweries:

    def __init__(self, db_name: str, db_loc: str):
        database_location = db_loc + db_name
        self.conn = lite.connect(database_location, check_same_thread=False)
        self.conn.row_factory = lite.Row
        self.curs = self.conn.cursor()

    def __del__(self):
        self.curs.close()
        self.conn.close()

    def get_brewery(self, brewery_id: int):
        select_brewery_command = 'select id, breweryName from breweries where id = ?'
        self.curs.execute(select_brewery_command, (brewery_id,))
        result = self.curs.fetchone()
        brewery = unpack_sqlite3_object(result)

        return brewery

    def get_breweries(self):
        select_breweries_command = 'select id, breweryName from breweries'
        self.curs.execute(select_breweries_command, ())
        results = self.curs.fetchall()
        breweries = unpack_sqlite3_objects(results)

        return breweries

    def insert_brewery(self, name: str):
        insert_brewery_command = 'insert into breweries (breweryName) values (?)'
        brewery_id = self.curs.execute(insert_brewery_command, (name,)).lastrowid
        self.conn.commit()

        return brewery_id

    def delete_brewery(self, brewery_id: int):
        delete_notes_command = 'delete from notesToBeer where beerId = (select id from beer where breweryId = ?)'
        self.curs.execute(delete_notes_command, (brewery_id,))
        self.conn.commit()

        delete_beer_command = 'delete from beer where id = ?'
        self.curs.execute(delete_beer_command, (brewery_id,))
        self.conn.commit()

        delete_brewery_command = 'delete from breweries where id = ?'
        self.curs.execute(delete_brewery_command, (brewery_id,))
        self.conn.commit()

    def update_brewery(self, brewery_id: int, new_name: str):
        update_brewery_command = 'update breweries set breweryName = ? where id = ?'
        self.curs.execute(update_brewery_command, (new_name, brewery_id))
        self.conn.commit()

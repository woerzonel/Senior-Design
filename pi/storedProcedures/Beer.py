#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

from storedProcedures.Helpers import unpack_sqlite3_objects, unpack_sqlite3_object


class Beer:

    def __init__(self, db_name: str, db_loc: str):
        database_location = db_loc + db_name
        self.conn = lite.connect(database_location, check_same_thread=False)
        self.conn.row_factory = lite.Row
        self.curs = self.conn.cursor()

    def __del__(self):
        self.curs.close()
        self.conn.close()

    def get_beer(self, beer_id: int):
        select_beer_command = 'select id, beerName, breweryId, typeId, abv from beer where id = ?'
        self.curs.execute(select_beer_command, (beer_id,))
        result = self.curs.fetchone()
        beer = unpack_sqlite3_object(result)
        return beer

    def get_all_beer(self):
        select_all_beer_command = 'select id, beerName, breweryId, typeId, abv from beer'
        self.curs.execute(select_all_beer_command, ())
        results = self.curs.fetchall()
        beer_list = unpack_sqlite3_objects(results)

        return beer_list

    def insert_beer(self, name: str, brewery: int, beer_type: int, abv: float):
        insert_beer_command = 'insert into beer (beerName, breweryId, typeId, abv) values (?, ?, ?, ?)'
        beer_id = self.curs.execute(insert_beer_command, (name, brewery, beer_type, abv)).lastrowid
        self.conn.commit()

        return beer_id

    def update_beer(self, beer_id: int, new_name: str, new_brewery_id: int, new_beer_type_id: int, new_abv: float):
        update_beer_command = 'update beer set beerName = ?, breweryId = ?, typeId = ?, abv = ? where id = ?'
        self.curs.execute(update_beer_command, (new_name, new_brewery_id, new_beer_type_id, new_abv, beer_id))
        self.conn.commit()

    def delete_beer(self, beer_id: int):
        beer_delete_command = 'delete from beer where id = ?'
        self.curs.execute(beer_delete_command, (beer_id,))
        self.conn.commit()

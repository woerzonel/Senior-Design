#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

from storedProcedures.Helpers import unpack_sqlite3_objects, unpack_sqlite3_object


class BeerTypes:

    def __init__(self, db_name: str, db_loc: str):
        database_location = db_loc + db_name
        self.conn = lite.connect(database_location, check_same_thread=False)
        self.conn.row_factory = lite.Row
        self.curs = self.conn.cursor()

    def __del__(self):
        self.curs.close()
        self.conn.close()

    def get_beer_type(self, beer_type_id: int):
        select_beer_type_command = 'select * from beerTypes where id = ?'
        self.curs.execute(select_beer_type_command, (beer_type_id,))
        result = self.curs.fetchone()
        beer_type = unpack_sqlite3_object(result)

        return beer_type

    def get_beer_types(self):
        select_beer_types_command = 'select * from beerTypes'
        self.curs.execute(select_beer_types_command, ())
        result = self.curs.fetchall()
        beer_types = unpack_sqlite3_objects(result)

        return beer_types

    def insert_beer_type(self, type_name: str):
        insert_beer_type_command = 'insert into beerTypes (typeName) values (?)'
        note_id = self.curs.execute(insert_beer_type_command, (type_name,)).lastrowid
        self.conn.commit()

        return note_id

    def update_beer_type(self, beer_type_id: int, new_type: str):
        update_beer_type_command = 'update beerTypes set typeName = ? where id = ?'
        self.curs.execute(update_beer_type_command, (new_type, beer_type_id))
        self.conn.commit()

    def delete_beer_type(self, beer_type_id: int):
        delete_beer_type_command = 'delete from beerTypes where id = ?'
        self.curs.execute(delete_beer_type_command, (beer_type_id,))
        self.conn.commit()

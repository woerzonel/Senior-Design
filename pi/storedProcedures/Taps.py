#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

from storedProcedures.Helpers import unpack_sqlite3_objects, unpack_sqlite3_object


class Taps:

    def __init__(self, db_name: str, db_loc: str):
        database_location = db_loc + db_name
        self.conn = lite.connect(database_location, check_same_thread=False)
        self.conn.row_factory = lite.Row
        self.curs = self.conn.cursor()

    def __del__(self):
        self.curs.close()
        self.conn.close()

    def get_tap(self, tap_id: int):
        select_tap_command = 'select * from onTap where id = ?'
        self.curs.execute(select_tap_command, (tap_id,))
        result = self.curs.fetchone()
        tap = unpack_sqlite3_object(result)

        return tap

    def get_taps(self):
        select_taps_command = 'select * from onTap'
        self.curs.execute(select_taps_command, ())
        results = self.curs.fetchall()
        taps = unpack_sqlite3_objects(results)

        return taps

    def insert_tap(self, sensor_id: int):
        insert_tap_command = 'insert into onTap (sensorId, beerId, volumeRecord, initialVolume) values (?, -1, 0, -1)'
        tap_id = self.curs.execute(insert_tap_command, (sensor_id,)).lastrowid
        self.conn.commit()

        return tap_id

    def delete_tap(self, tap_id: int):
        delete_tap_command = 'delete from onTap where id = ?'
        self.curs.execute(delete_tap_command, (tap_id,))
        self.conn.commit()

    def set_tap(self, tap_id: int, beer_id: int, initial_volume: int):
        update_tap_command = 'update onTap set beerId = ?, volumeRecord = 0, initialVolume = ? where id = ?'
        self.curs.execute(update_tap_command, (beer_id, initial_volume, tap_id))
        self.conn.commit()

    def empty_tap(self, tap_id: int):
        empty_tap_command = 'update onTap set beerId = -1, volumeRecord = 0, initialVolume = -1 where id = ?'
        self.curs.execute(empty_tap_command, (tap_id,))
        self.conn.commit()

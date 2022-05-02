#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

from storedProcedures.Helpers import unpack_sqlite3_objects


class NotesToBeer:

    def __init__(self, db_name: str, db_loc: str):
        database_location = db_loc + db_name
        self.conn = lite.connect(database_location, check_same_thread=False)
        self.conn.row_factory = lite.Row
        self.curs = self.conn.cursor()

    def __del__(self):
        self.curs.close()
        self.conn.close()

    def find_link_notes(self, beer_id: int):
        get_notes_command = 'select noteId from notesToBeer where beerId = ?'
        self.curs.execute(get_notes_command, (beer_id,))
        lite_objects = self.curs.fetchall()
        note_ids = unpack_sqlite3_objects(lite_objects)

        return note_ids

    def link_note(self, beer_id: int, note_id: int):
        add_note_command = 'insert into notesToBeer (beerId, noteId) values (?, ?)'
        self.curs.execute(add_note_command, (beer_id, note_id))
        self.conn.commit()

    def link_notes(self, beer_id: int, note_ids: [int]):
        if len(note_ids) > 0:
            for note_id in note_ids:
                self.link_note(beer_id, note_id)

    def delete_link_note(self, beer_id: int, note_id: int):
        remove_note_command = 'delete from notesToBeer where beerId = ? and noteId = ?'
        self.curs.execute(remove_note_command, (beer_id, note_id))
        self.conn.commit()

    def delete_link_notes(self, beer_id: int):
        remove_notes_command = 'delete from notesToBeer where beerId = ?'
        self.curs.execute(remove_notes_command, (beer_id,))
        self.conn.commit()

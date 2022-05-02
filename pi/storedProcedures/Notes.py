#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

from storedProcedures.Helpers import unpack_sqlite3_objects, unpack_sqlite3_object


class Notes:

    def __init__(self, db_name: str, db_loc: str):
        database_location = db_loc + db_name
        self.conn = lite.connect(database_location, check_same_thread=False)
        self.conn.row_factory = lite.Row
        self.curs = self.conn.cursor()
        # TODO: add global config variables

    def __del__(self):
        self.curs.close()
        self.conn.close()

    def get_note(self, note_id: int):

        select_note_command = 'select * from notes where id = ?'
        self.curs.execute(select_note_command, (note_id,))
        result = self.curs.fetchone()
        note = unpack_sqlite3_object(result)

        return note

    def get_notes(self):
        select_notes_command = 'select id, note from notes'
        self.curs.execute(select_notes_command, ())
        results = self.curs.fetchall()
        notes = unpack_sqlite3_objects(results)

        return notes

    def insert_note(self, note: str):
        insert_note_command = 'insert into notes (note) values (?)'
        note_id = self.curs.execute(insert_note_command, (note,)).lastrowid
        self.conn.commit()

        return note_id

    def update_note(self, note_id: int, new_note: str):
        update_note_command = 'update notes set note = ? where id = ?'
        self.curs.execute(update_note_command, (new_note, note_id))
        self.conn.commit()

    def delete_note(self, note_id: int):
        delete_note_command = 'delete from notes where id = ?'
        self.curs.execute(delete_note_command, (note_id,))
        self.conn.commit()

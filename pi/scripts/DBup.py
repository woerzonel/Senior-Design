#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import os

databaseName = 'BeerTapSystem'
dataBaseLocation = '/home/pi/sqlite3/%s.db' % databaseName
schemaPath = 'schema'
dataPath = 'data'


def create_new_database():
    try:
        con = lite.connect(dataBaseLocation)
        con.commit

    except lite.Error as e:
        if con:
            con.rollback()
            print('Error %s:' % e.args[0])
            sys.exit(1)

    finally:
        if con:
            con.close()


def run_scripts(path):
    # Connect or Create DB File
    conn = lite.connect(dataBaseLocation)
    curs = conn.cursor()

    for script in os.listdir(path):
        scriptLocation = '%s/%s' % (path, script)
        TableSchema = ''
        with open(scriptLocation, 'r') as SchemaFile:
            TableSchema = SchemaFile.read().replace('\n', ' ')
        # Create Tables
        lite.complete_statement(TableSchema)
        curs.executescript(TableSchema)

    # Close DB
    curs.close()
    conn.close()


create_new_database()
run_scripts(schemaPath)
run_scripts(dataPath)

#!/usr/bin/python
# -*- coding: utf-8 -*-

from storedProcedures.Taps import Taps


class ManageTapController:
	#db_name = 'BeerTapSystem.db'
    #db_loc = 'C:\sqlite\dbs\\'
    taps_procedures = None

    def __init__(self, db_loc: str, db_name: str):
        # TODO: pass this in as parameter to keep instances down, maintain them in the main
        self.taps_procedures = Taps(db_name, db_loc)

    def set_tap(self, tap_id: int, beer_id: int, initial_volume: int):
        self.taps_procedures.set_tap(tap_id, beer_id, initial_volume)

    # TODO: this method will hold the logic for pairing a new sensor
    def add_tap(self, sensor_id: int):
        self.taps_procedures.insert_tap(sensor_id)

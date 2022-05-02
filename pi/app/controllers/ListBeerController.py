#!/usr/bin/python
# -*- coding: utf-8 -*-

from storedProcedures.Beer import Beer
from storedProcedures.BeerTypes import BeerTypes
from storedProcedures.Breweries import Breweries


class ListBeerController:

    def __init__(self, db_loc: str, db_name: str):
        self.beer_procedures = Beer(db_name, db_loc)
        self.beer_types_procedures = BeerTypes(db_name, db_loc)
        self.breweries_procedures = Breweries(db_name, db_loc)

    def get_beer_list(self):
        beer_list = self.beer_procedures.get_all_beer()
        self.get_brewery_names(beer_list)
        self.get_type_name(beer_list)
        return beer_list

    def get_brewery_names(self, beer_list: []):
        for beer in beer_list:
            beer['breweryName'] = self.breweries_procedures.get_brewery(beer['breweryId'])['breweryName']
            del beer['breweryId']  # removes unused key:value

    def get_type_name(self, beer_list: []):
        for beer in beer_list:
            beer['typeName'] = self.beer_types_procedures.get_beer_type(beer['typeId'])['typeName']
            del beer['typeId']  # removes unused key:value

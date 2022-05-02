#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv

from storedProcedures.Beer import Beer
from storedProcedures.BeerTypes import BeerTypes
from storedProcedures.Breweries import Breweries
from storedProcedures.Notes import Notes
from storedProcedures.NotesToBeer import NotesToBeer


class CreateBeerController:

    def __init__(self, db_loc: str, db_name: str):
        self.beer_procedures = Beer(db_name, db_loc)
        self.beer_types_procedures = BeerTypes(db_name, db_loc)
        self.breweries_procedures = Breweries(db_name, db_loc)
        self.notes_procedures = Notes(db_name, db_loc)
        self.notes_to_beer_procedures = NotesToBeer(db_name, db_loc)

    # this method returns a tuple of brewery_names
    def get_breweries(self):
        return tuple(brewery['breweryName'] for brewery in self.breweries_procedures.get_breweries())

    def create_brewery(self, brewery: str):
        return self.breweries_procedures.insert_brewery(brewery)

    def update_brewery(self, brewery_id: int, new_name: str):
        self.breweries_procedures.update_brewery(brewery_id, new_name)

    def get_notes(self):
        return self.notes_procedures.get_notes()

    def create_note(self, note: str):
        return self.notes_procedures.insert_note(note)

    def update_note(self, note_id: int, new_note: str):
        self.notes_procedures.update_note(note_id, new_note)

    # this method returns a tuple of the beer_type_names
    def get_beer_types(self):
        return tuple(beer_type['typeName'] for beer_type in self.beer_types_procedures.get_beer_types())

    def create_beer_type(self, name: str):
        return self.beer_types_procedures.insert_beer_type(name)

    def update_beer_type(self, type_id: int, new_name: str):
        self.beer_types_procedures.update_beer_type(type_id, new_name)

    # this method takes the names of a beer object, finds the ids or created new attributes to obtain the id,
    # and inserts the new beer with the other create_single_beer method
    # param:
    #     beerName: str,
    #     breweryId: int,
    #     notes: [int],
    #     typeId: int,
    #     abv: float
    # return: no return
    def create_individual_beer(self, beer_name: str, brewery_name: str, notes: [str], type_name: str, abv: float):
        new_beer = {
            'beerName': beer_name,
            'breweryId': self.get_brewery_id(brewery_name),
            'notes': self.get_note_ids(notes),
            'typeId': self.get_beer_type_id(type_name),
            'abv': abv
        }
        self.create_single_beer(new_beer)

    # this method takes a beer object and inserts the new beer and then links the notes associated
    # param: new_beer: {
    #     beerName: str,
    #     breweryId: int,
    #     notes: [int],
    #     typeId: int,
    #     abv: float
    # }
    # return: no return
    def create_single_beer(self, new_beer: {}):
        beer_id = self.beer_procedures.insert_beer(
            new_beer['beerName'],
            new_beer['breweryId'],
            new_beer['typeId'],
            new_beer['abv'])
        self.notes_to_beer_procedures.link_notes(
            beer_id,
            new_beer['notes'])

    # Public method for importing multiple beers in a csv file.
    # duplicate beers are not handled
    # rogue commas are not handled
    # param: file: str; location and name of the file to be imported
    # return: no return
    def create_multiple_beer(self, file: str):
        try:
            with open(file, mode='r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                counter = 0
                column_names = None
                for row in csv_reader:
                    if counter == 0:
                        if len(row) == 5 \
                                and 'name' in row \
                                and 'brewery' in row\
                                and 'notes' in row\
                                and 'type' in row\
                                and 'abv' in row:
                            column_names = row
                        else:
                            raise KeyError
                    else:
                        # TODO: add value validation to have correct input and secure from SQL injection
                        # TODO: log malformed rows and continue to next row
                        new_beer = {}
                        for idx, column_data in enumerate(row):
                            if column_names[idx] == 'name':
                                new_beer['beerName'] = column_data
                            if column_names[idx] == 'brewery':
                                new_beer['breweryId'] = self.get_brewery_id(column_data)
                            if column_names[idx] == 'notes':
                                note_ids = []
                                if len(column_data) > 0:
                                    note_ids = self.get_note_ids(column_data.split('|'))
                                new_beer['notes'] = note_ids
                            if column_names[idx] == 'type':
                                new_beer['typeId'] = self.get_beer_type_id(column_data)
                            if column_names[idx] == 'abv':
                                new_beer['abv'] = float(column_data)
                        self.create_single_beer(new_beer)
                    counter += 1
        except FileNotFoundError:
            print("The file at " + file + " does not exist.")
        except KeyError:
            print('The csv headers are not formatted properly.')

    # Private method retrieves note ids: int by the name: str
    # param: new_notes:
    # [str]
    # return: note_ids: [int]
    def get_note_ids(self, new_notes: [str]):
        notes = self.get_notes()
        new_notes = list(dict.fromkeys(new_notes))  # removes possible duplicates
        note_ids = []

        for new_note in new_notes:
            new_id = -1
            for note in notes:
                if note['note'] == new_note:
                    new_id = note['id']
                    break
            if new_id is -1:
                new_id = self.create_note(new_note)
            note_ids.append(new_id)

        return note_ids

    # Private method retrieves brewery id: int by the name: str
    # param: brewery_name: str
    # return: brewery_id: int
    def get_brewery_id(self, brewery_name: str):
        breweries = self.breweries_procedures.get_breweries()
        for brewery in breweries:
            if brewery['breweryName'] == brewery_name:
                return brewery['id']
        return self.create_brewery(brewery_name)

    # Private method retrieves beer type id: int by the name: str
    # param: type_name: str
    # return: beer_type_id: int
    def get_beer_type_id(self, type_name: str):
        beer_types = self.beer_types_procedures.get_beer_types()
        for beer_type in beer_types:
            if beer_type['typeName'] == type_name:
                return beer_type['id']
        return self.create_beer_type(type_name)

import unittest
from unittest.mock import MagicMock
from app.controllers.CreateBeerController import CreateBeerController


class TestCreateBeerController(unittest.TestCase):
    db_loc = 'foo'
    db_name = 'bar'

    def test_createSingleBeer(self):
        test_beer = {
            'beerName': 'foo',
            'breweryId': 0,
            'notes': [0],
            'typeId': 0,
            'abv': 0.0
        }
        test_new_beer_id = 0
        create_beer_controller = CreateBeerController(self.db_loc, self.db_name)
        create_beer_controller.beer_procedures.insert_beer = MagicMock(return_value=test_new_beer_id)
        create_beer_controller.notes_to_beer_procedures.link_notes = MagicMock()

        create_beer_controller.create_single_beer(test_beer)

        create_beer_controller\
            .beer_procedures\
            .insert_beer\
            .assert_called_once()
        create_beer_controller\
            .beer_procedures\
            .insert_beer\
            .assert_called_with(
                test_beer['beerName'],
                test_beer['breweryId'],
                test_beer['typeId'],
                test_beer['abv'])
        create_beer_controller\
            .notes_to_beer_procedures\
            .link_notes.assert_called_once()
        create_beer_controller\
            .notes_to_beer_procedures\
            .link_notes.assert_called_with(
                test_new_beer_id,
                test_beer['notes'])

    def test_createMultipleBeer_ok(self):
        test_csv_file = '..\\..\\..\\test_files\\test_csv.csv'
        create_beer_controller = CreateBeerController(self.db_loc, self.db_name)
        create_beer_controller.get_brewery_id = MagicMock(return_value=1)
        create_beer_controller.get_note_ids = MagicMock(return_value=[])
        create_beer_controller.get_beer_type_id = MagicMock(return_value=1)
        create_beer_controller.create_single_beer = MagicMock()

        create_beer_controller.create_multiple_beer(test_csv_file)

        create_beer_controller.get_brewery_id.assert_called()
        create_beer_controller.get_note_ids.assert_called()
        create_beer_controller.get_beer_type_id.assert_called()
        create_beer_controller.create_single_beer.assert_called()

    def test_createMultipleBeer_missingFile(self):
        test_csv_file = ''
        create_beer_controller = CreateBeerController(self.db_loc, self.db_name)

        self.assertRaises(FileNotFoundError, create_beer_controller.create_multiple_beer(test_csv_file))

    def test_createMultipleBeer_badHeaders(self):
        test_csv_file = '..\\..\\..\\test_files\\test_csv_bad_headers.csv'
        create_beer_controller = CreateBeerController(self.db_loc, self.db_name)

        self.assertRaises(KeyError, create_beer_controller.create_multiple_beer(test_csv_file))

    def test_getNoteIds_knownNote(self):
        test_notes = [
            {'id': 1, 'note': 'foo'},
            {'id': 2, 'note': 'jon'},
            {'id': 3, 'note': 'bar'}
        ]
        test_new_notes = ['foo']
        create_beer_controller = CreateBeerController(self.db_loc, self.db_name)
        create_beer_controller.get_notes = MagicMock(return_value=test_notes)

        result_note_ids = create_beer_controller.get_note_ids(test_new_notes)

        create_beer_controller.get_notes.assert_called_once()
        self.assertEqual(test_notes[0]['id'], result_note_ids[0])

    def test_getNoteIds_notKnownNote(self):
        test_notes = [
            {'id': 2, 'note': 'jon'},
            {'id': 3, 'note': 'bar'}
        ]
        test_new_notes = ['foo']
        expected_note_id = 0
        create_beer_controller = CreateBeerController(self.db_loc, self.db_name)
        create_beer_controller.get_notes = MagicMock(return_value=test_notes)
        create_beer_controller.create_note = MagicMock(return_value=expected_note_id)

        result_note_ids = create_beer_controller.get_note_ids(test_new_notes)

        create_beer_controller.get_notes.assert_called_once()
        create_beer_controller.create_note.assert_called_once()
        create_beer_controller.create_note.assert_called_with(test_new_notes[0])
        self.assertEqual(expected_note_id, result_note_ids[0])

    def test_getBreweryId_knownBrewery(self):
        test_breweries = [
            {'id': 1, 'breweryName': 'foo'},
            {'id': 2, 'breweryName': 'jon'},
            {'id': 3, 'breweryName': 'bar'}
        ]
        test_brewery = 'foo'
        create_beer_controller = CreateBeerController(self.db_loc, self.db_name)
        create_beer_controller.breweries_procedures.get_breweries = MagicMock(return_value=test_breweries)

        result_brewery_id = create_beer_controller.get_brewery_id(test_brewery)

        create_beer_controller.breweries_procedures.get_breweries.assert_called_once()
        self.assertEqual(test_breweries[0]['id'], result_brewery_id)

    def test_getBreweryId_notKnownBrewery(self):
        test_breweries = [
            {'id': 2, 'breweryName': 'jon'},
            {'id': 3, 'breweryName': 'bar'}
        ]
        test_brewery = 'foo'
        expected_brewery_id = 0
        create_beer_controller = CreateBeerController(self.db_loc, self.db_name)
        create_beer_controller.breweries_procedures.get_breweries = MagicMock(return_value=test_breweries)
        create_beer_controller.create_brewery = MagicMock(return_value=expected_brewery_id)

        result_brewery_id = create_beer_controller.get_brewery_id(test_brewery)

        create_beer_controller.breweries_procedures.get_breweries.assert_called_once()
        create_beer_controller.create_brewery.assert_called_once()
        create_beer_controller.create_brewery.assert_called_with(test_brewery)
        self.assertEqual(expected_brewery_id, result_brewery_id)

    def test_getBeerTypeId_knownType(self):
        test_types = [
            {'id': 1, 'typeName': 'foo'},
            {'id': 2, 'typeName': 'jon'},
            {'id': 3, 'typeName': 'bar'}
        ]
        test_type = 'foo'
        create_beer_controller = CreateBeerController(self.db_loc, self.db_name)
        create_beer_controller.beer_types_procedures.get_beer_types = MagicMock(return_value=test_types)

        result_type_id = create_beer_controller.get_beer_type_id(test_type)

        create_beer_controller.beer_types_procedures.get_beer_types.assert_called_once()
        self.assertEqual(test_types[0]['id'], result_type_id)

    def test_getBeerTypeId_notKnownType(self):
        test_types = [
            {'id': 2, 'typeName': 'jon'},
            {'id': 3, 'typeName': 'bar'}
        ]
        test_type = 'foo'
        expected_type_id = 0
        create_beer_controller = CreateBeerController(self.db_loc, self.db_name)
        create_beer_controller.beer_types_procedures.get_beer_types = MagicMock(return_value=test_types)
        create_beer_controller.create_beer_type = MagicMock(return_value=expected_type_id)

        result_type_id = create_beer_controller.get_beer_type_id(test_type)

        create_beer_controller.beer_types_procedures.get_beer_types.assert_called_once()
        create_beer_controller.create_beer_type.assert_called_once()
        create_beer_controller.create_beer_type.assert_called_with(test_type)
        self.assertEqual(expected_type_id, result_type_id)


if __name__ == '__main__':
    unittest.main()

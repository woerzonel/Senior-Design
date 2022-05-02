import unittest
from unittest.mock import MagicMock
from app.controllers.ListBeerController import ListBeerController


class TestListBeerController(unittest.TestCase):
    db_loc = 'foo'
    db_name = 'bar'

    def test_getBreweryNames(self):
        test_brewery = {'id': 1, 'breweryName': 'foo'}
        test_beer_list = [{'breweryId': 1}, {'breweryId': 1}]
        list_beer_controller = ListBeerController(self.db_loc, self.db_name)
        list_beer_controller.breweries_procedures.get_brewery = MagicMock(return_value=test_brewery)

        list_beer_controller.get_brewery_names(test_beer_list)

        list_beer_controller.breweries_procedures.get_brewery.assert_called()
        self.assertEqual(test_beer_list[0]['breweryName'], test_brewery['breweryName'])
        self.assertEqual(test_beer_list[1]['breweryName'], test_brewery['breweryName'])
        self.assertFalse('breweryId' in test_beer_list[0])
        self.assertFalse('breweryId' in test_beer_list[1])

    def test_getTypeNames(self):
        test_type = {'id': 1, 'typeName': 'foo'}
        test_beer_list = [{'typeId': 1}, {'typeId': 1}]
        list_beer_controller = ListBeerController(self.db_loc, self.db_name)
        list_beer_controller.beer_types_procedures.get_beer_type = MagicMock(return_value=test_type)

        list_beer_controller.get_type_name(test_beer_list)

        list_beer_controller.beer_types_procedures.get_beer_type.assert_called()
        self.assertEqual(test_beer_list[0]['typeName'], test_type['typeName'])
        self.assertEqual(test_beer_list[1]['typeName'], test_type['typeName'])
        self.assertFalse('typeId' in test_beer_list[0])
        self.assertFalse('typeId' in test_beer_list[1])


if __name__ == '__main__':
    unittest.main()

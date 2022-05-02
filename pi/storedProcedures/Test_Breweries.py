import unittest
from storedProcedures.Breweries import Breweries


class TestBreweries(unittest.TestCase):
    # TODO: make these variables dependant to environment
    db_name = 'BeerTapSystem.db'
    db_loc = 'C:\sqlite\dbs\\'
    test_brewery_name = 'foo'
    test_brewery_id = -1

    def test_insert_brewery(self):
        breweries = Breweries(db_name=self.db_name, db_loc=self.db_loc)
        result_brewery_id = breweries.insert_brewery(self.test_brewery_name)
        result_brewery = breweries.get_brewery(result_brewery_id)
        self.assertEqual(result_brewery_id, result_brewery['id'])
        self.assertEqual(self.test_brewery_name, result_brewery['breweryName'])
        breweries.delete_brewery(result_brewery_id)

    def test_get_brewery(self):
        breweries = Breweries(db_name=self.db_name, db_loc=self.db_loc)
        result_brewery = breweries.get_brewery(self.test_brewery_id)
        self.assertEqual(self.test_brewery_id, result_brewery['id'])
        self.assertEqual('MKE', result_brewery['breweryName'])

    def test_get_breweries(self):
        breweries = Breweries(db_name=self.db_name, db_loc=self.db_loc)
        result_breweries = breweries.get_breweries()
        self.assertLess(1, len(result_breweries))

    def test_delete_brewery(self):
        breweries = Breweries(db_name=self.db_name, db_loc=self.db_loc)
        result_brewery_id = breweries.insert_brewery(self.test_brewery_name)
        result_brewery = breweries.get_brewery(result_brewery_id)
        self.assertEqual(result_brewery_id, result_brewery['id'])
        breweries.delete_brewery(result_brewery_id)
        empty_result = breweries.get_brewery(result_brewery_id)
        self.assertIsNone(empty_result)

    def test_update_brewery(self):
        breweries = Breweries(db_name=self.db_name, db_loc=self.db_loc)
        original_brewery = breweries.get_brewery(self.test_brewery_id)
        breweries.update_brewery(self.test_brewery_id, self.test_brewery_name)
        result_brewery = breweries.get_brewery(self.test_brewery_id)
        self.assertEqual(self.test_brewery_name, result_brewery['breweryName'])
        breweries.update_brewery(self.test_brewery_id, original_brewery['breweryName'])


if __name__ == '__main__':
    unittest.main()

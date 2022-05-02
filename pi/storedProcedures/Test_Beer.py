import unittest
from storedProcedures.Beer import Beer


class TestBeer(unittest.TestCase):
    # TODO: make these variables dependant to environment
    db_name = 'BeerTapSystem.db'
    db_loc = 'C:\sqlite\dbs\\'
    test_beer_id = -1
    test_beer = {
        'beerName': 'test name',
        'breweryId': -1,
        'typeId': -1,
        'abv': 4.5
    }

    def test_insert_beer(self):
        beer = Beer(db_name=self.db_name, db_loc=self.db_loc)
        result_id = beer.insert_beer(
            self.test_beer['beerName'],
            self.test_beer['breweryId'],
            self.test_beer['typeId'],
            self.test_beer['abv']
        )
        result_beer = beer.get_beer(result_id)
        self.assertEqual(result_id, result_beer['id'])
        self.assertEqual(self.test_beer['beerName'], result_beer['beerName'])
        self.assertEqual(self.test_beer['breweryId'], result_beer['breweryId'])
        self.assertEqual(self.test_beer['typeId'], result_beer['typeId'])
        self.assertEqual(self.test_beer['abv'], result_beer['abv'])
        beer.delete_beer(result_id)

    def test_get_beer(self):
        beer = Beer(db_name=self.db_name, db_loc=self.db_loc)
        result_beer = beer.get_beer(-1)
        self.assertEqual(self.test_beer_id, result_beer['id'])
        self.assertEqual('Louies Resurection', result_beer['beerName'])
        self.assertEqual(-1, result_beer['breweryId'])
        self.assertEqual(-3, result_beer['typeId'])
        self.assertEqual(0.089, result_beer['abv'])

    def test_get_all_beer(self):
        beer = Beer(db_name=self.db_name, db_loc=self.db_loc)
        result_beer = beer.get_all_beer()
        self.assertLess(1, len(result_beer))

    def test_delete_beer(self):
        beer = Beer(db_name=self.db_name, db_loc=self.db_loc)
        result_id = beer.insert_beer(
            self.test_beer['beerName'],
            self.test_beer['breweryId'],
            self.test_beer['typeId'],
            self.test_beer['abv']
        )
        result_beer = beer.get_beer(result_id)
        self.assertEqual(result_id, result_beer['id'])
        beer.delete_beer(result_id)
        empty_result = beer.get_beer(result_id)
        self.assertIsNone(empty_result)

    def test_update_beer(self):
        beer = Beer(db_name=self.db_name, db_loc=self.db_loc)
        test_beer_id = -3
        test_name = 'foo'
        test_brewery = -1
        test_beer_type = -1
        test_abv = 10.0
        original_beer = beer.get_beer(test_beer_id)
        beer.update_beer(test_beer_id, test_name, test_brewery, test_beer_type, test_abv)
        result_beer = beer.get_beer(test_beer_id)
        self.assertEqual(result_beer['beerName'], test_name)
        self.assertEqual(result_beer['breweryId'], test_brewery)
        self.assertEqual(result_beer['typeId'], test_beer_type)
        self.assertEqual(result_beer['abv'], test_abv)
        beer.update_beer(
            original_beer['id'],
            original_beer['beerName'],
            original_beer['breweryId'],
            original_beer['typeId'],
            original_beer['abv'])


if __name__ == '__main__':
    unittest.main()

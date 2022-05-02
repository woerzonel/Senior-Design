import unittest
from storedProcedures.BeerTypes import BeerTypes


class TestBeerTypes(unittest.TestCase):
    # TODO: make these variables dependant on environment
    db_name = 'BeerTapSystem.db'
    db_loc = 'C:\sqlite\dbs\\'
    test_type_id = -1
    test_beer_type = "beer type"

    def test_insert_beer_type(self):
        beer_types = BeerTypes(db_name=self.db_name, db_loc=self.db_loc)
        result_index = beer_types.insert_beer_type(self.test_beer_type)
        result_beer_type = beer_types.get_beer_type(result_index)
        self.assertEqual(self.test_beer_type, result_beer_type['typeName'])
        beer_types.delete_beer_type(result_index)

    def test_get_beer_type(self):
        test_beer_type = 'Lager'
        beer_types = BeerTypes(db_name=self.db_name, db_loc=self.db_loc)
        result = beer_types.get_beer_type(self.test_type_id)
        self.assertEqual(test_beer_type, result['typeName'])

    def test_get_beer_types(self):
        beer_types = BeerTypes(db_name=self.db_name, db_loc=self.db_loc)
        results = beer_types.get_beer_types()
        self.assertLess(1, len(results))

    def test_delete_beer_type(self):
        beer_types = BeerTypes(db_name=self.db_name, db_loc=self.db_loc)
        result_index = beer_types.insert_beer_type(self.test_beer_type)
        result_beer_type = beer_types.get_beer_type(result_index)
        self.assertEqual(self.test_beer_type, result_beer_type['typeName'])
        beer_types.delete_beer_type(result_index)
        result_beer_type = beer_types.get_beer_type(result_index)
        self.assertIsNone(result_beer_type)

    def test_update_beer_type(self):
        beer_types = BeerTypes(db_name=self.db_name, db_loc=self.db_loc)
        original_beer_type = beer_types.get_beer_type(self.test_type_id)
        beer_types.update_beer_type(self.test_type_id, self.test_beer_type)
        result_beer_type = beer_types.get_beer_type(self.test_type_id)
        self.assertEqual(self.test_beer_type, result_beer_type['typeName'])
        beer_types.update_beer_type(original_beer_type['id'], original_beer_type['typeName'])


if __name__ == '__main__':
    unittest.main()

import unittest
from storedProcedures.Taps import Taps


class TestTaps(unittest.TestCase):
    # TODO: make these variables dependant to environment
    db_name = 'BeerTapSystem.db'
    db_loc = 'C:\sqlite\dbs\\'
    test_tap_id = -1
    test_beer_id = -2
    test_beer_volume = 500
    test_sensor_id_1 = 1234
    test_sensor_id_2 = 1233

    def test_insert_tap(self):
        taps = Taps(db_name=self.db_name, db_loc=self.db_loc)
        result_tap_id = taps.insert_tap(self.test_sensor_id_2)
        result_tap = taps.get_tap(result_tap_id)
        self.assertEqual(result_tap_id, result_tap['id'])
        self.assertEqual(self.test_sensor_id_2, result_tap['sensorId'])
        # This verifies the presets are set when inserting the tap
        self.assertEqual(-1, result_tap['beerId'])
        self.assertEqual(0, result_tap['volumeRecord'])
        self.assertEqual(-1, result_tap['initialVolume'])
        taps.delete_tap(result_tap_id)

    def test_get_tap(self):
        taps = Taps(db_name=self.db_name, db_loc=self.db_loc)
        result_tap = taps.get_tap(self.test_tap_id)
        self.assertEqual(self.test_tap_id, result_tap['id'])
        self.assertEqual(self.test_sensor_id_1, result_tap['sensorId'])
        self.assertEqual(-1, result_tap['beerId'])
        self.assertEqual(0, result_tap['volumeRecord'])
        self.assertEqual(100, result_tap['initialVolume'])

    def test_get_taps(self):
        taps = Taps(db_name=self.db_name, db_loc=self.db_loc)
        result_taps = taps.get_taps()
        self.assertLess(1, len(result_taps))

    def test_delete_tap(self):
        taps = Taps(db_name=self.db_name, db_loc=self.db_loc)
        result_tap_id = taps.insert_tap(self.test_sensor_id_2)
        result_tap = taps.get_tap(result_tap_id)
        self.assertEqual(result_tap_id, result_tap['id'])
        taps.delete_tap(result_tap_id)
        empty_result = taps.get_tap(result_tap_id)
        self.assertIsNone(empty_result)

    def test_set_tap(self):
        taps = Taps(db_name=self.db_name, db_loc=self.db_loc)
        original_tap_data = taps.get_tap(self.test_tap_id)
        taps.set_tap(self.test_tap_id, self.test_beer_id, self.test_beer_volume)
        result_tap = taps.get_tap(self.test_tap_id)
        self.assertEqual(self.test_beer_id, result_tap['beerId'])
        self.assertEqual(0, result_tap['volumeRecord'])
        self.assertEqual(self.test_beer_volume, result_tap['initialVolume'])
        taps.set_tap(self.test_tap_id, original_tap_data['beerId'], original_tap_data['initialVolume'])

    def test_empty_tap(self):
        taps = Taps(db_name=self.db_name, db_loc=self.db_loc)
        original_tap_data = taps.get_tap(self.test_tap_id)
        taps.empty_tap(self.test_tap_id)
        result_tap = taps.get_tap(self.test_tap_id)
        self.assertEqual(-1, result_tap['beerId'])
        self.assertEqual(0, result_tap['volumeRecord'])
        self.assertEqual(-1, result_tap['initialVolume'])
        taps.set_tap(self.test_tap_id, original_tap_data['beerId'], original_tap_data['initialVolume'])


if __name__ == '__main__':
    unittest.main()

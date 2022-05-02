import unittest
from storedProcedures.NotesToBeer import NotesToBeer


class TestNotesToBeer(unittest.TestCase):
    # TODO: make these variables dependant to environment
    db_name = 'BeerTapSystem.db'
    db_loc = 'C:\sqlite\dbs\\'
    test_beer_id = -1
    test_beer_note_id = -3
    test_note_ids = [test_beer_note_id]

    def test_find_notes(self):
        notes_to_beer = NotesToBeer(db_name=self.db_name, db_loc=self.db_loc)
        result_links = notes_to_beer.find_link_notes(self.test_beer_id)
        self.assertLess(1, len(result_links))
        self.assertTrue({'noteId': -2} in result_links)
        self.assertTrue({'noteId': -1} in result_links)

    def test_link_note(self):
        notes_to_beer = NotesToBeer(db_name=self.db_name, db_loc=self.db_loc)
        test_beer_id = -5
        test_note_id = -1
        notes_to_beer.link_note(test_beer_id, test_note_id)
        result_note_link = notes_to_beer.find_link_notes(test_beer_id)
        self.assertEqual(len(result_note_link), 1)
        self.assertDictEqual(result_note_link[0], {'noteId': test_note_id})
        notes_to_beer.delete_link_notes(test_beer_id)

    def test_link_notes(self):
        notes_to_beer = NotesToBeer(db_name=self.db_name, db_loc=self.db_loc)
        test_beer_id = -5
        test_note_ids = [-1, -2]
        notes_to_beer.link_notes(test_beer_id, test_note_ids)
        result_note_links = notes_to_beer.find_link_notes(test_beer_id)
        self.assertEqual(len(result_note_links), len(test_note_ids))
        self.assertTrue({'noteId': test_note_ids[0]} in result_note_links)
        self.assertTrue({'noteId': test_note_ids[1]} in result_note_links)
        notes_to_beer.delete_link_notes(test_beer_id)

    def test_delete_link_note(self):
        notes_to_beer = NotesToBeer(db_name=self.db_name, db_loc=self.db_loc)
        test_beer_id = -5
        test_note_id = -1
        notes_to_beer.link_note(test_beer_id, test_note_id)
        result_note_link = notes_to_beer.find_link_notes(test_beer_id)
        self.assertIsNotNone(result_note_link)
        notes_to_beer.delete_link_note(test_beer_id, test_note_id)
        empty_result = notes_to_beer.find_link_notes(test_beer_id)
        self.assertEqual(len(empty_result), 0)

    def test_delete_link_notes(self):
        notes_to_beer = NotesToBeer(db_name=self.db_name, db_loc=self.db_loc)
        test_beer_id = -5
        test_note_ids = [-1, -2]
        notes_to_beer.link_notes(test_beer_id, test_note_ids)
        result_note_links = notes_to_beer.find_link_notes(test_beer_id)
        self.assertIsNotNone(result_note_links)
        notes_to_beer.delete_link_notes(test_beer_id)
        empty_result = notes_to_beer.find_link_notes(test_beer_id)
        self.assertEqual(len(empty_result), 0)


if __name__ == '__main__':
    unittest.main()

import unittest
from storedProcedures.Notes import Notes


class TestNotes(unittest.TestCase):
    # TODO: make these variables dependant on environment
    db_name = 'BeerTapSystem.db'
    db_loc = 'C:\sqlite\dbs\\'
    test_note_id = -1
    test_note = 'note 1'

    def test_insert_note(self):
        notes = Notes(db_name=self.db_name, db_loc=self.db_loc)
        result_index = notes.insert_note(self.test_note)
        result_note = notes.get_note(result_index)
        self.assertEqual(self.test_note, result_note['note'])
        notes.delete_note(result_index)

    def test_get_note(self):
        test_note = 'toasty'
        notes = Notes(db_name=self.db_name, db_loc=self.db_loc)
        result = notes.get_note(self.test_note_id)
        self.assertEqual(test_note, result['note'])

    def test_get_notes(self):
        notes = Notes(db_name=self.db_name, db_loc=self.db_loc)
        results = notes.get_notes()
        self.assertLess(1, len(results))

    def test_delete_note(self):
        notes = Notes(db_name=self.db_name, db_loc=self.db_loc)
        result_index = notes.insert_note(self.test_note)
        result_note = notes.get_note(result_index)
        self.assertEqual(self.test_note, result_note['note'])
        notes.delete_note(result_index)
        result_note = notes.get_note(result_index)
        self.assertIsNone(result_note)

    def test_update_note(self):
        notes = Notes(db_name=self.db_name, db_loc=self.db_loc)
        original_note = notes.get_note(self.test_note_id)
        notes.update_note(self.test_note_id, self.test_note)
        result_note = notes.get_note(self.test_note_id)
        self.assertEqual(self.test_note, result_note['note'])
        notes.update_note(original_note['id'], original_note['note'])


if __name__ == '__main__':
    unittest.main()

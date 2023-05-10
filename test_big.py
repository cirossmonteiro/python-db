import unittest

import main

class TestBigDatabase(unittest.TestCase):
    def setUp(self):
        self.database = main.Database("test_database")
        self.len_collections = 1000
        self.len_documents = 1000
        self.document_obj = {"a": 123}
        for i in range(self.len_collections):
            self.database.create_collection(f"test_collection_{i}")
            for j in range(self.len_documents):
                self.database.collections[i].insert({
                    **self.document_obj,
                    "b": i*self.len_collections+j
                })
        self.database.dump()

    def test_big_creation(self):
        self.assertEqual(self.len_collections, len(self.database.collections))

if __name__ == '__main__':
    unittest.main()
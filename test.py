import unittest

import main

class TestCreation(unittest.TestCase):
    def setUp(self):
        self.database = main.Database("test_database")
        self.collection = main.Collection("test_collection")
        self.document = main.Document({})
        
        self.database.create_collection("test_collection"),
        self.database.collections[0].insert({})
    
    def tearDown(self):
        for collection in self.database.collections:
            collection.documents = []
        self.database.collections = []

    def test_document(self):
        self.assertEqual(self.document, self.database.collections[0].documents[0])
    
    def test_collection(self):
        self.assertEqual(self.collection, self.database.collections[0])

    def test_database(self):
        self.assertEqual(self.database.name, "test_database")
        self.database.dump()
        database_other = main.Database("test_database")
        database_other.load()
        self.assertEqual(self.database, database_other)
    

if __name__ == '__main__':
    unittest.main()
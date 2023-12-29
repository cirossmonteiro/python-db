import unittest

import avl
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
        self.assertEqual(
            main.fix_query({ "field1": 123 }),
            { "field1": { "$eq": 123 } }
        )

        # remark: ordered as in MAP_OPERATORS
        self.assertTrue(main.condition({ "field1": 3 }, "field1", "$eq", 3))
        self.assertFalse(main.condition({ "field1": 3 }, "field1", "$ne", 3))
        self.assertFalse(main.condition({ "field1": 3 }, "field1", "$lt", 3))
        self.assertTrue(main.condition({ "field1": 3 }, "field1", "$le", 3))
        self.assertFalse(main.condition({ "field1": 3 }, "field1", "$gt", 3))
        self.assertTrue(main.condition({ "field1": 3 }, "field1", "$ge", 3))

        self.assertEqual(self.document, self.database.collections[0].documents[0])
    
    def test_collection(self):
        self.assertEqual(self.collection, self.database.collections[0])

    def test_database(self):
        self.assertEqual(self.database.name, "test_database")
        self.database.dump()
        database_other = main.Database("test_database")
        database_other.load()
        self.assertEqual(self.database, database_other)

    def test_avl_tree(self):
        self.root_number = 5
        self.left_number = 4
        self.right_number = 6
        self.left_number2 = 3
        self.right_number2 = 7
        self.right_number3 = 8

        # create and insert 5 values
        self.avl_tree = avl.AVLTree()
        self.avl_tree.insert(self.root_number)
        self.avl_tree.insert(self.left_number)
        self.avl_tree.insert(self.right_number)
        self.avl_tree.insert(self.left_number2)
        self.avl_tree.insert(self.right_number2)
        
        # check position of each value
        self.assertEqual(self.avl_tree.root.value, self.root_number)
        self.assertEqual(self.avl_tree.root.left.value, self.left_number)
        self.assertEqual(self.avl_tree.root.right.value, self.right_number)
        self.assertEqual(self.avl_tree.root.left.left.value, self.left_number2)
        self.assertEqual(self.avl_tree.root.right.right.value, self.right_number2)
        self.assertEqual(self.avl_tree.height(), 3)

        # check balance factor of each node
        self.assertEqual(self.avl_tree.root.balance_factor, 0)
        self.assertEqual(self.avl_tree.root.left.balance_factor, -1)
        self.assertEqual(self.avl_tree.root.right.balance_factor, 1)
        self.assertEqual(self.avl_tree.root.left.left.balance_factor, 0)
        self.assertEqual(self.avl_tree.root.right.right.balance_factor, 0)

if __name__ == '__main__':
    unittest.main()
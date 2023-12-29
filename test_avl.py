import unittest

import avl

class TestAVL(unittest.TestCase):
    def setUp(self):
        self.tree = avl.AVLTree()
    
    def tearDown(self):
        del self.tree

    def test_basic(self):
        # create and insert 5 values
        self.tree.insert(5)
        self.tree.insert(4)
        self.tree.insert(6)
        self.tree.insert(3)
        self.tree.insert(8)
        
        # check position of each value
        print(21, self.tree)
        self.assertEqual(self.tree.root.value, 5)
        self.assertEqual(self.tree.root.left.value, 4)
        self.assertEqual(self.tree.root.right.value, 6)
        self.assertEqual(self.tree.root.left.left.value, 3)
        self.assertEqual(self.tree.root.right.right.value, 8)
        self.assertEqual(self.tree.height(), 3)

        # check balance factor of each node
        self.assertEqual(self.tree.root.balance_factor, 0)
        self.assertEqual(self.tree.root.left.balance_factor, -1)
        self.assertEqual(self.tree.root.right.balance_factor, 1)
        self.assertEqual(self.tree.root.left.left.balance_factor, 0)
        self.assertEqual(self.tree.root.right.right.balance_factor, 0)

    def test_all_rotations(self):
        # pass
        for n in range(20):
            self.tree.insert(n)
        print(40, self.tree)
        self.assertTrue(self.tree.is_balanced())
    
    def test_rotation_left(self):
        x = avl.Node("x")
        z = avl.Node("z")
        t1 = avl.Node("t1")
        t23 = avl.Node("t23")
        t4 = avl.Node("t4")
        x.left = t1
        x.right = z
        z.left = t23
        z.right = t4
        root = avl.rotate_left(x)
        self.assertEqual(root.value, "z")
        self.assertEqual(root.left.value, "x")
        self.assertEqual(root.right.value, "t4")
        self.assertEqual(root.left.left.value, "t1")
        self.assertEqual(root.left.right.value, "t23")
    
    def test_rotation_right(self):
        x = avl.Node("x")
        z = avl.Node("z")
        t1 = avl.Node("t1")
        t23 = avl.Node("t23")
        t4 = avl.Node("t4")
        x.left = t1
        x.right = t23
        z.left = x
        z.right = t4
        root = avl.rotate_right(z)
        self.assertEqual(root.value, "x")
        self.assertEqual(root.left.value, "t1")
        self.assertEqual(root.right.value, "z")
        self.assertEqual(root.right.left.value, "t23")
        self.assertEqual(root.right.right.value, "t4")

    # source: https://panda.ime.usp.br/pythonds/static/pythonds_pt/06-Arvores/AVLTreeImplementation.html

    def test_insert_bf_plus2_right_minus1(self):
        # tree = avl.AVLTree()
        self.tree.insert("a")
        self.tree.insert("c")
        self.tree.insert("b")
        self.assertTrue(self.tree.is_balanced())

    def test_insert_bf_minus2_left_minus1(self):
        # tree = avl.AVLTree()
        self.tree.insert("c")
        self.tree.insert("a")
        self.tree.insert("b")
        self.assertTrue(self.tree.is_balanced())
    
    # def test_rotation_right_fig4(self):
    #     a = avl.Node("a")
    #     b = avl.Node("b")
    #     c = avl.Node("c")
    #     d = avl.Node("d")
    #     e = avl.Node("e")
    #     f = avl.Node("f")
    #     b.left = a
    #     c.left = b
    #     c.right = d
    #     e.left = c
    #     e.right = f
    #     root = avl.rotate_right(e)
    #     self.assertEqual(root.value, "c")
    #     self.assertEqual(root.left.value, "b")
    #     self.assertEqual(root.right.value, "e")
    #     self.assertEqual(root.left.left.value, "a")
    #     self.assertEqual(root.right.left.value, "d")
    #     self.assertEqual(root.right.right.value, "f")

if __name__ == '__main__':
    unittest.main()
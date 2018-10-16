import unittest
from unionFind import *

class TestUnionFind(unittest.TestCase):
    def test_node_empty(self):
        n = Node()
        self.assertTrue(n.value == None)
        self.assertTrue(n.parent == None)
        #self.assertFalse(n.children)
        self.assertEqual(n.size, 1)

    def test_unionfind_empty(self):
        uf = UnionFind()
        self.assertFalse(uf.elements)
        self.assertEqual(len(uf.elements), 0)

    def test_unionfind_simple(self):
        n0 = Node()
        n1 = Node()
        l = [n0, n1]
        uf = UnionFind(l)
        self.assertEqual(len(uf.elements), 2)

    def test_unionfind_join(self):
        l = [0, 1]
        uf = UnionFind(l)
        uf.join(0, 1)
        self.assertEqual(uf.find(1), uf.find(0))

    def test_unionfind_find(self):
        l = range(0, 4)
        uf = UnionFind(l)
        uf.join(0, 1)
        uf.join(1, 2)
        self.assertEqual(uf.find(0), uf.find(1))
        self.assertEqual(uf.find(0), uf.find(2))
        self.assertEqual(uf.find(3), uf.find(3))


if __name__ == '__main__':
    unittest.main()

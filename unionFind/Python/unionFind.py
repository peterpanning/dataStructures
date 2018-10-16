class Node:
    def __init__(self, value=None):
        self.value = value
        self.size = 1
        self.parent = None
        

class UnionFind:
    # A Union-Find is used for connecting and searching 
    # disjoint sets, such as when you have many items and want to find
    # connections between them. 

    # It supports minimum three operations:

    # MakeSet, which eliminates duplicates and makes each item a node in its own tree.
    # We effectively implement MakeSet in UnionFind's __init__. 

    # Join, which joins two sets by making the root node of one the root of the other

    # Find, which identifies the set to which an element belongs

    # The rules for when to conduct a join are dependent on the application
    # of this data struture I.e. when two people become friends or when adding an edge to a MST. 

    def __init__(self, iterable=[]):
        s = set(iterable)
        self.elements = {} 
        # TODO: Storing elements in a dictionary allows us to easily refer to 
        # them by value, returning the relevant node without 
        # need for an additional data structure. BUT, it also means we can only use
        # immutable values as keys--we can't use objects, for example. Might
        # be worth pursuing an alternative implementation which allows for 
        # greater flexibility. 
        for x in s:
            n = Node(x)
            n.parent = n
            self.elements[x] = n

    def join(self, a, b):
        # TODO: This join only joins by size of the trees, not by their rank.
        # An implementation of this which joins by rank will be useful in the future.
        a = self.find(a)
        b = self.find(b)

        if a == b:
            return # They are already in the same set
        
        if b.size > a.size: # Works because of path compression
            a, b = b, a
        
        b.parent = a
        a.size += b.size

    def find(self, element):
        e = self.elements[element]
        if e.parent != e:
            e.parent = self.find(e.parent.value)
        return e.parent

    def add(self, item): 
        if item not in self.elements:
            n = Node(item)
            n.parent = n
            self.elements[item] = n 
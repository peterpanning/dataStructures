class Node:
    def __init__(self, value=None):
        self.value = value 
        self.nextNode = None

class LinkedList:
    def __init__(self, node=None):
        self.firstNode = node 
    
    def addNode(self, node):
        node.nextNode = self.firstNode 
        self.firstNode = node 
    
    def findValue(self, value, node=None):
        if not node:
            if self.firstNode.value == value:
                return self.firstNode
        elif node.value == value:
            return node 
        elif node.nextNode:
            return self.findValue(value, node.nextNode)
        else:
            return False

    def deleteNode(self, value, prev=None, curr=None):
        if not curr and prev:
            return 
        elif not curr and not prev:
            if self.firstNode.value == value:
                self.firstNode = self.firstNode.nextNode 
            else: 
                self.deleteNode(value, self.firstNode, self.firstNode.nextNode) 
        else:
            if curr.value == value:
                prev.nextNode = curr.nextNode 
                else:
                    self.deleteNode(value, curr, curr.nextNode)


    # These make our LinkedList an iterable, so we can use for _ in LinkedList
    def __iter__(self):
        self.current = self.first 
        return self 

    def __next__(self):
        if self.current == None:
            raise StopIteration 
        else: 
            n = self.current 
            self.current = self.current.nextNode 
            return n


    def deleteDupes(self, prev=None, curr=None):
        if not curr and prev:
            return
        elif not curr and not prev:
            buffer = []
            buffer.append(self.first.value)
            deleteDupes(self.first, self.nextNode)
        else:
            if curr.value in buffer:
                prev.nextNode = curr.nextNode 
                deleteDupes(prev, curr.nextNode)
            else:
                buffer.append(curr.value)
                deleteDupes(curr, curr.nextNode)
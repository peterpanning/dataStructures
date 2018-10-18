from collections import deque
class Queue:
    def __init__(self):
        self.que = deque()
    def push(self, element):
        self.que.append(element)
    def pop(self):
        self.que.popleft()
    def peek(self):
        self.que[0]
    def isEmpty(self):
        return not self.que
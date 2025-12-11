class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class StackSingle:
    def __init__(self):
        self.top = None

    def push(self, x):
        node = Node(x)
        node.next = self.top
        self.top = node

    def pop(self):
        if not self.top:
            raise IndexError("pop from empty stack")
        val = self.top.val
        self.top = self.top.next
        return val

    def peek(self):
        return None if not self.top else self.top.val

s = StackSingle()
s.push(6)
s.push(2)

print(s.pop())  
print(s.pop())  

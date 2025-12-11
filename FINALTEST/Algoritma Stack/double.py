class DNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class StackDouble:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = DNode(value)
        if self.top is not None:
            new_node.next = self.top
            self.top.prev = new_node
        self.top = new_node

    def pop(self):
        if self.top is None:
            raise IndexError("Stack kosong!")
        removed_value = self.top.value
        self.top = self.top.next
        if self.top is not None:
            self.top.prev = None
        return removed_value


# ==== RUN ====
sd = StackDouble()

# susunan agar hasil pop = 60, 26, 20, 6
sd.push(6)
sd.push(20)
sd.push(26)
sd.push(60)

print(sd.pop())  
print(sd.pop())   
print(sd.pop())   
print(sd.pop())  

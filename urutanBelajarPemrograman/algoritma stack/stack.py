class Stack:
    def __init__(self):
        self.data = []  # wadah stack menggunakan list

    def push(self, item):
        self.data.append(item)
        print(f"Push: {item} berhasil ditambahkan ke stack")

    def pop(self):
        if self.isEmpty():
            return "Stack kosong, tidak bisa pop!"
        return self.data.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack kosong, tidak ada elemen teratas"
        return self.data[-1]  # elemen paling atas

    def isEmpty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)


# ======================================================
# Contoh Penggunaan
# ======================================================

s = Stack()

s.push(10)
s.push(20)
s.push(30)

print("\nElemen teratas:", s.peek())  # 30
print("POP:", s.pop())                # 30
print("POP:", s.pop())                # 20

print("\nApakah stack kosong?", s.isEmpty())
print("Sisa elemen dalam stack:", s.data)

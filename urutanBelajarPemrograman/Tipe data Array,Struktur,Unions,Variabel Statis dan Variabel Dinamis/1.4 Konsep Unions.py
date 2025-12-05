from ctypes import Union, c_int, c_float

# Membuat union seperti di bahasa C
class MyUnion(Union):
    _fields_ = [
        ("angka_int", c_int),
        ("angka_float", c_float)
    ]

# Membuat objek union
data = MyUnion()

# Menyimpan nilai integer
data.angka_int = 100
print("Nilai sebagai INT   :", data.angka_int)
print("Nilai sebagai FLOAT :", data.angka_float)  # nilai float akan berubah karena memory sama

print("\n--- Mengisi FLOAT ---")
# Menyimpan nilai float
data.angka_float = 3.14
print("Nilai sebagai FLOAT :", data.angka_float)
print("Nilai sebagai INT   :", data.angka_int)  # integer berubah mengikuti nilai float


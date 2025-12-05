from ctypes import Union, c_int, c_float

# ============================================================
# 1. PERANCANGAN ARRAY (1D dan 2D)
# ============================================================

print("=== PERANCANGAN ARRAY ===")

# ARRAY 1 DIMENSI
array_1d = [5, 10, 15, 20, 25]
print("Array 1 Dimensi :", array_1d)
print("Akses elemen index 3 :", array_1d[3])

# ARRAY 2 DIMENSI (MATRIKS)
array_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\nArray 2 Dimensi :")
for baris in array_2d:
    print(baris)

print("Akses elemen [2][1] :", array_2d[2][1])


# ============================================================
# 2. PERANCANGAN STRUKTUR (STRUCTURE)
# ============================================================

print("\n=== PERANCANGAN STRUKTUR ===")

class Mahasiswa:
    def __init__(self, nama, nim, prodi):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi

# Membuat objek struktur
mhs = Mahasiswa("Irsan", "230500123", "Teknik Informatika")

print("Nama Mahasiswa :", mhs.nama)
print("NIM            :", mhs.nim)
print("Program Studi  :", mhs.prodi)


# ============================================================
# 3. PERANCANGAN UNION (ctypes.Union)
# ============================================================

print("\n=== PERANCANGAN UNION ===")

class AngkaUnion(Union):
    _fields_ = [
        ("nilai_int", c_int),
        ("nilai_float", c_float)
    ]

# Membuat objek union
u = AngkaUnion()

# Mengisi integer
u.nilai_int = 150
print("Isi sebagai INT   :", u.nilai_int)
print("Isi sebagai FLOAT :", u.nilai_float)  # nilai berubah karena 1 memori

# Mengisi float
u.nilai_float = 7.25
print("\nIsi sebagai FLOAT :", u.nilai_float)
print("Isi sebagai INT   :", u.nilai_int)     # nilai berubah lagi


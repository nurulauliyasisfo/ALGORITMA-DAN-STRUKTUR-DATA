# Konsep Struktur menggunakan class sebagai representasi data terstruktur

class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

# Membuat objek dari struktur
mhs1 = Mahasiswa("Irsan", "230501002", "Teknik Informatika")

# Menampilkan data
print("Data Mahasiswa:")
print("Nama    :", mhs1.nama)
print("NIM     :", mhs1.nim)
print("Jurusan :", mhs1.jurusan)


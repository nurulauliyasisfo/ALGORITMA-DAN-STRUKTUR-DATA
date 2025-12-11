# dictionary di Python
mhs = {
    "nim": "D0425324",
    "nama": "Nurul Auliya",
    "jurusan": "Sistem Informasi",
    "nilai": {"algoritma": 90, "matematika": 95}
}

# akses
print(mhs["nama"])         
print(mhs.get("nim"))     

# iterasi
for k, v in mhs.items():
    print(k, "->", v)

# menambah / mengubah
mhs["tahun"] = 2025
mhs["nilai"]["algoritma"] = 88

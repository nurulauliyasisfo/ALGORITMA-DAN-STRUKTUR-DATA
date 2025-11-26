#NAMA : Nurul auliya
#NIM : D0425324

#TUPLE

warna = ("ungu", "kuning", "biru") #tuple tidak bisa diubah
print("isi tuple: ",warna)
print("elemen ke-1:", warna[0])
# Warna[1] = "kuning" #ini akan ERROR karna tuple tidak bisa diubah


#List
hewan = ["sapi", "ayam", "unta"] #bisa ubah
print("sebelum diubah:", hewan)

hewan[1] = "unta"  #mengubah isi
hewan.append("ayam") #menambah data
print("Setelah diubah:", hewan)
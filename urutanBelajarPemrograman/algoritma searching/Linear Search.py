def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


# Contoh penggunaan
data = [12, 34, 7, 23, 56, 9]
cari = 23

hasil = linear_search(data, cari)

if hasil != -1:
    print(f"Data {cari} ditemukan pada index {hasil}")
else:
    print("Data tidak ditemukan")


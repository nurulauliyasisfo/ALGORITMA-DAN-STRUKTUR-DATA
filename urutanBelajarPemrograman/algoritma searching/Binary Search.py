def binary_search(arr, key):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


# Contoh penggunaan
data = [5, 10, 15, 20, 25, 30]  # harus terurut
cari = 20

hasil = binary_search(data, cari)

if hasil != -1:
    print(f"Data {cari} ditemukan pada index {hasil}")
else:
    print("Data tidak ditemukan")


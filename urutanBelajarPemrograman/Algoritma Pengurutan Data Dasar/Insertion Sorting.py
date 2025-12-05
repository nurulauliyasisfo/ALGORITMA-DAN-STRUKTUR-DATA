# Insertion Sort

def insertion_sort(arr):
    # Loop dimulai dari indeks 1 karena elemen pertama dianggap sudah terurut
    for i in range(1, len(arr)):
        key = arr[i]     # Elemen yang akan dimasukkan ke posisi yang benar
        j = i - 1

        # Geser elemen arr[j] yang lebih besar dari key ke kanan
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Tempatkan key pada posisi yang sesuai
        arr[j + 1] = key

    return arr


# Contoh penggunaan
data = [9, 5, 1, 4, 3]
print("Data sebelum diurutkan:", data)

sorted_data = insertion_sort(data)
print("Data setelah diurutkan :", sorted_data)

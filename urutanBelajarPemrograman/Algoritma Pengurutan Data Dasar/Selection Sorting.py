def selection_sort(arr):
    n = len(arr)

    # iterasi untuk setiap posisi elemen
    for i in range(n):
        # asumsi index terkecil adalah i
        min_index = i

        # mencari index nilai terkecil
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # tukar elemen posisi i dengan elemen terkecil
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# Contoh penggunaan
data = [29, 10, 14, 37, 13]
print("Data sebelum diurutkan :", data)

hasil = selection_sort(data)
print("Data setelah diurutkan :", hasil)

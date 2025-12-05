def bubble_sort(arr):
    n = len(arr)

    # melakukan iterasi sebanyak jumlah elemen - 1
    for i in range(n - 1):
        # loop untuk membandingkan elemen
        for j in range(0, n - i - 1):
            # jika elemen sekarang lebih besar dari elemen setelahnya → tukar
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Contoh penggunaan
data = [34, 12, 5, 66, 1, 89, 23]
print("Data sebelum diurutkan :", data)

hasil = bubble_sort(data)
print("Data setelah diurutkan :", hasil)

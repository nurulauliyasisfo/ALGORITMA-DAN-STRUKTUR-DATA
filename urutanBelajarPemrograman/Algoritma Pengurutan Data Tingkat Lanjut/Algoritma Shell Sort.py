# Shell Sort

def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Jarak awal (gap) adalah setengah panjang array

    # Loop selama gap masih lebih besar dari 0
    while gap > 0:
        # Lakukan insertion sort dengan jarak (gap) tertentu
        for i in range(gap, n):
            temp = arr[i]
            j = i

            # Geser elemen yang lebih besar dari temp
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        # Kurangi gap menjadi setengahnya
        gap //= 2

    return arr


# Contoh penggunaan
data = [12, 34, 54, 2, 3]
print("Data sebelum diurutkan:", data)

sorted_data = shell_sort(data)
print("Data setelah diurutkan :", sorted_data)

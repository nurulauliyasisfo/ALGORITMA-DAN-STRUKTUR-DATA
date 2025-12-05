# Quick Sort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Sudah terurut jika panjang ≤ 1

    pivot = arr[len(arr) // 2]  # Ambil pivot dari elemen tengah
    left = [x for x in arr if x < pivot]      # Elemen lebih kecil dari pivot
    middle = [x for x in arr if x == pivot]   # Elemen sama dengan pivot
    right = [x for x in arr if x > pivot]     # Elemen lebih besar dari pivot

    # Rekursi: urutkan left dan right lalu gabungkan
    return quick_sort(left) + middle +_

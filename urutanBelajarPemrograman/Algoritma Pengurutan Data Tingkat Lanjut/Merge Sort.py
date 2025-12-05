# Merge Sort

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2       # Titik tengah array
        left_half = arr[:mid]     # Bagian kiri
        right_half = arr[mid:]    # Bagian kanan

        # Rekursi: urutkan bagian kiri dan kanan
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Penggabungan kedua bagian yang sudah terurut
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Jika masih ada sisa di left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Jika masih ada sisa di right_half
        while j < len(right_half):
            arr[k] = right_half[j]

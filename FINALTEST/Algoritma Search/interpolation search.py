def interpolation_search(arr, target):
    lo, hi = 0, len(arr)-1
    while lo <= hi and arr[lo] <= target <= arr[hi]:
        # jika semua elemen sama di rentang
        if arr[hi] == arr[lo]:
            if arr[lo] == target:
                return lo
            break
        # posisi estimasi
        pos = lo + int((target - arr[lo]) * (hi - lo) / (arr[hi] - arr[lo]))
        if pos < lo or pos > hi:
            break
        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            lo = pos + 1
        else:
            hi = pos - 1
    return -1

b = [10,20,30,40,50,60,70,80,90]
print(interpolation_search(b, 70))  
print(interpolation_search(b, 66))
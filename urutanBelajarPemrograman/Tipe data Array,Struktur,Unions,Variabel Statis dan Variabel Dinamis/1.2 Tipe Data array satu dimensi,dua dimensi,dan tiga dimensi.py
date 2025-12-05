# Tipe Data Array (List) 1 Dimensi, 2 Dimensi, dan 3 Dimensi

# 1. ARRAY 1 DIMENSI (list biasa)
array_1d = [10, 20, 30, 40, 50]
print("Array 1 Dimensi:", array_1d)

# Mengakses elemen
print("Elemen ke-2 (index 1):", array_1d[1])


# 2. ARRAY 2 DIMENSI (matriks)
array_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("\nArray 2 Dimensi (Matriks):")
for row in array_2d:
    print(row)

# Mengakses elemen baris ke-2 kolom ke-3
print("Elemen [1][2]:", array_2d[1][2])


# 3. ARRAY 3 DIMENSI
array_3d = [
    [   # Lapisan 1
        [1, 2],
        [3, 4]
    ],
    [   # Lapisan 2
        [5, 6],
        [7, 8]
    ]
]

print("\nArray 3 Dimensi:")
for layer in array_3d:
    print(layer)

# Mengakses elemen tertentu (lapisan 2, baris 1, kolom 2)
print("Elemen [1][0][1]:", array_3d[1][0][1])


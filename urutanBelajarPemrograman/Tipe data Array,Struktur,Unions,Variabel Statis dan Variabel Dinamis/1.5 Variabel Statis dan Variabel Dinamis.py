# Contoh Variabel Statis dalam fungsi

def counter():
    if not hasattr(counter, "value"):
        counter.value = 0  # static variable
    counter.value += 1
    return counter.value

print(counter())  # 1
print(counter())  # 2
print(counter())  # 3   -> nilainya tersimpan

# Contoh variabel dinamis
x = 10
print("Nilai awal:", x)

x = "Sekarang menjadi string"
print("Nilai berubah secara dinamis:", x)

x = [1, 2, 3]
print("Berubah lagi menjadi list:", x)

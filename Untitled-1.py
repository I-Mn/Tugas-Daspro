"""
Nama: Kautsar Muhammad Mizan
Kelas: 1C
NIM: 2404073
"""
buah = ["apel", "jeruk", "ceri", "durian", "apel"]
print ("Data awal:")
print (buah)

buah[2] = "cherry"
print ("1. Ganti nama:")
print (buah)

print ("2. Ditentukan User")
namabuah = input("Masukkan nama buah: ")
namabuah = namabuah.lower()
posisi = int(input("Posisi ke:"))
buah.insert(posisi-1,namabuah)
print (buah)

print ("3. Sesuai Abjad")
buah.sort()
print(buah)
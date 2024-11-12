'''
Kautsar Muhammad Mizan
RPL 1C
2404073
'''
hasil = 0
angka = 1
while True:
    angka = int(input("Masukkan angka: "))
    if angka >= 0:
        hasil += angka
    else:
        break
print ("Hasil dari penjumlahan angka tersebut adalah: ", hasil)
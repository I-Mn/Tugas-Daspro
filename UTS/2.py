'''Kautsar Muhammad Mizan
RPL 1C
2404073'''

angka = 0
Angka = 0
ganjil = 0
genap = 0


while angka >= 0:
    angka = int(input("Input bilangan : "))
    if angka % 2 == 0 and angka >= 0:
        genap += angka
    elif angka >= 0:
        ganjil += angka
print ()
print (f"Jumlah bilangan genap : {genap}")
print (f"Jumlah bilangan ganjil : {ganjil}")
'''Kautsar Muhammad Mizan
RPL 1C
2404073'''

angka = 0
angka1 = 0
Angka = 0
kurang = 3

angka = int(input("Input bilangan : "))
Angka += angka
while kurang > 0:
    angka1 = int(input("Input bilangan : "))
    if angka1 <= angka and kurang > 0:
        kurang -= 1
        """print ("A", kurang)"""
        angka = angka1
    if angka1 > angka:
        kurang = 3
        angka = angka1
        Angka += angka
    angka1 = angka
    '''print ("Angka",angka)'''
print (f"Hasil penjumlahan nilai yang membesar {Angka}")
'''Kautsar Muhammad Mizan
Rpl 1c
2404073'''
barang = int(input("Jumlah barang: "))
harga = 1
if (barang > 0): 
    if barang < 100:
        harga = 5000
    elif barang <= 150:
        harga = 4000
    else:
        harga = 2500
    total = harga*barang
    print ("Total harga: ", total)
else:
    print ("Tidak ada barang")
'''Kautsar Muhammad Mizan
RPL 1C
2404073'''
n = int(input("Masukan jumlah bebek : "))

while n > 1:
    print(f'''
          {n} bebek kecil berenang
          Menyusuri sungai yang deras
          Induknya mencari kwek kwek kwek
          Hanya {n-1} ekor yang pulang
          ''')
    n -= 1
if n == 1:
    print(f'''
          {n} bebek kecil berenang
          Menyusuri sungai yang deras
          Induknya mencari kwek kwek kwek
          Dan semua bebek kecil pulang, aha!
          ''')
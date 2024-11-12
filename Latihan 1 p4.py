"""
Kautsar Muhammad Mizan
RPL 1C
2404073
"""
Jumlah_entri = int(input("Masukkan jumlah data yang akan dimasukkan: "))
daftar_data = {i+1 : input(f"Masukkan nilai {i+1}: ") for i in range(Jumlah_entri)}
nilai_unik = list(dict.fromkeys(daftar_data.values()))
data_akhir = sorted(int(nilai) for nilai in nilai_unik)
print(data_akhir)

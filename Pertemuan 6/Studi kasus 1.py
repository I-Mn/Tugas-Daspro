''' Kautsar Muhammad Mizan
RPL 1C
2404073'''
nilai = int(input("Masukkan nilai siswa: "))
if nilai >= 0 and nilai <= 100:
    if nilai >= 90:
        nilai = "A"
    elif nilai >= 80:
        nilai = "B"
    elif nilai >= 70:
        nilai = "C"
    else:
        nilai = "D"
    print ("Nilai anda adalah: ", nilai)
else:
    print ("Nilai tidak valid")    
    
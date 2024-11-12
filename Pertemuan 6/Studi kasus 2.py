''' Kautsar Muhammad Mizan
RPL 1C
2404073'''
gender = str(input("Masukkan gender Anda: ")).upper()
umur = int(input("Masukkan umur Anda: "))
tinggi = int(input("Masukkan tinggi badan Anda: "))
iq = int(input("Masukkan IQ Anda: "))
maaf = "Maaf, anda tidak dapat menjadi model catwalk karena "
selamat = "Kamu bisa menjadi seorang model catwalk!"
alasan = 0
if umur >=18 and umur <= 25:
    if iq >= 130:
        if gender in ["PRIA", "LAKI LAKI", "LAKI-LAKI"]:
            if tinggi >= 175:
                print (selamat)
            else:
                alasan = "tinggi Anda tidak mencukupi"
                print (maaf, alasan)
        elif gender in ["WANITA", "PEREMPUAN"]:
            if tinggi >= 170:
                print (selamat)
            else:
                alasan = "tinggi Anda tidak mencukupi"
                print (maaf, alasan)
        else:
            print ('Mohon masukkan gender yang valid ("Pria/laki laki atau Wanita/perempuan (Tidak case sensitive))')
    else:
        alasan = "iq anda tidak mencukupi"
        print (maaf, alasan)
else:
    alasan = "umur anda lebih/tidak cukup."
    print (maaf, alasan)
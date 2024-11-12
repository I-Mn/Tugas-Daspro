'''
Kautsar Muhammad Mizan
RPL 1C
2404073
'''
def konversi(totalDetik):
    jam = totalDetik // 3600
    sisa = totalDetik % 3600
    menit = sisa // 60
    detik = sisa % 60
    return f"{jam} jam - {menit} menit - {detik} detik"
def hitung(a, b, c, d, e, f):
    a = a*3600
    d = d*3600
    b = b*60
    e = e*60
    
    selisih = d + e + f - a - b - c
    if selisih < 0:
        selisih += 24 *3600
    return (konversi(selisih))
jamMulai = int(input("Jam Mulai: "))
menitMulai = int(input("Menit Mulai: "))
detikMulai = int(input("Detik Mulai: "))
jamSelesai = int(input("Jam Selesai: "))
menitSelesai = int(input("Menit Selesai: "))
detikSelesai = int(input("Detik Selesai: "))
print (hitung(jamMulai, menitMulai, detikMulai, jamSelesai, menitSelesai, detikSelesai))
'''
Kautsar Muhammad Mizan
RPL 1C
2404073
'''

def cek(password):
    if password == "Latihan":
        return True
    else:
        return False
def login():
    coba = 0
    while coba < 3:
        user = input("Masukan username: ")
        password = input("Masukkan password: ")
        if cek(password):
            return True
        else:
            coba += 1
            if coba < 3:
                print(f"Password salah kesempatanmu {3 - coba} lagi")
    print ("Akses ditolak")
    return False
if login():
    print ("Login berhasil! Selamat datang!")
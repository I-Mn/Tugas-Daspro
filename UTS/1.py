'''Kautsar Muhammad Mizan
RPL 1C
2404073'''

user = "loginUTS"
pas = "rpl2024"
pengulangan = 1
sukses = "Selamat datang di aplikasi Prodi RPL"
gagal = "Anda tidak diperkenankan mengakses aplikasi ini"
p = 0

print ("Silahkan Login")
logus = input("Username : ")
logpas = input("Password : ")
if logus == user and logpas == pas :
    p = 1
    pass
else:
    while pengulangan <= 3 and p == 0 :
        print (f"Login Salah! Kesempatan anda {4 - pengulangan} lagi")
        pengulangan += 1
        logus = input("Username : ")
        logpas = input("Password : ")
        if logus == user and logpas == pas :
            p = 1      
    
if p == 1:
    print (sukses)
else:
    print(gagal)
'''Kautsar Muhammad Mizan
RPL 1C
2404073'''
def is_prima (x):
    for i in range (2,x):
        if x % i == 0:
            return False
            print ("t")
        return True
x = 0
Angka = 0
prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,49,53,59,61,67,71,73,79,83,89,91,97,101]
i = range(2,3,5,)
N = int(input("Masukkan nilai N = "))
for i in range(N):
    angka = int(input(f"Masukkan bilangan ke {i+1} = "))
    if angka in prime:
        Angka += angka
print (f"Jumlah bilangan prima adalah: {Angka}")

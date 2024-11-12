'''jumlah_perulangan = 3
for index in range(jumlah_perulangan):
    print (f"Print ke-{index}")
    
for i in "Python":
    print(f"Huruf: {i}")
for i in range(1, 6):
    print(i)
    
buah = ["Apel", "Belimbing", "Ceri", "Durian"]
for i in buah:
    print(f"Buah: {i}")
print (buah[1])

buah = ["Apel", "Belimbing", "Ceri", "Durian"]
for i in range(len(buah)):
    print(f"Buah :{buah[i]}")
    
    
angka = 0
while(angka < 8):
    print(f"Angka sekarang: {angka}")
    angka += 1
   ''' 
    
'''angka = [ 1, 2, 3, 4, 5]
for i in angka:
    print (i)
    if i == 3:
        break
    
angka = [1, 2, 3, 4, 5]
for i in angka:
    if i == 3:
        break
    print (i)
    
    
angka = [1, 2, 3, 4, 5]
for i in angka:
    if i == 3:
        continue
    print (i)

for i in range (6):
    print (i)'''
    
for i in range (10,0, -1):
    print (i)
    
buah = ['Apel', 'Belimbing', 'Ceri']
angka = [1, 2]

for i in buah:
    for j in angka:
        print (i)
        print (j)
        
list = ["A","B","C","D"]
listBaru = []
for item in range(len(list)):
    print(list[item])
for i in list:
    listBaru.append(i.upper())
print (listBaru)

kucing = {
    "Nama" : "A",
    "Umur" : 5,
}
#for i in kucing
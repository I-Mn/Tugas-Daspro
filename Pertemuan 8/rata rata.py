'''
Kautsar Muhammad Mizan
RPL 1C
2404073
'''
def rataRata (*angka):
    return sum(angka)/len(angka)

listAngka = []
angka = 0

while True:
    angka = int(input("Masukkan angka, akan berhenti jika diinputkan angka 0 "))
    if angka == 0:
        break
    listAngka.append(angka)
print (f"Rata ratanya adalah: {rataRata(*listAngka)}")
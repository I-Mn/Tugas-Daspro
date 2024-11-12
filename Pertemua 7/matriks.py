'''
Kautsar Muhammad Mizan
RPL 1C
2404073
'''
n = int(input("Masukan rasio matriks: "))
value = 1
'''for i in range(n):
    row = []
    for j in range(n):
        row.append(value)
        value += 1
    print(row)'''
for i in range(n):
    for j in range(n):
        print (value, end=" ")
        value+= 1
    print()
long_text = '''Ini adalah contoh teks yang sangat panjang.
Kamu bisa menulis beberapa baris teks di sini tanpa masalah.
Python akan menganggap ini sebagai satu string yang panjang.'''

print(long_text)

'''Kautsar Muhammad Mizan
RPL 1C
2404073'''

i = int(input("Input 3 digit terakhir : "))
if i >= 1 and i <= 50:
    if i % 2 == 0:
        k = 2
    else:
        k = 1
elif i >= 51 and i <= 100:
    if i % 2 == 0:
        k = 4
    else:
        k = 3
elif i >= 101 and i <= 150:
    if i % 2 == 0:
        k = 6
    else:
        k = 5
elif i > 150:
    if i > 150:
        if i % 2 == 0:
            k = 8
        else:
            k = 7
print(f"Silakan masuk ke kelas K{k}")
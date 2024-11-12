'''
Kautsar Muhammad Mizan
RPL 1C
2404073
'''
def deretFibon(N):
    deret = [0,1]
    if N < 1:
        deret = [0]
    elif N == 1:
        deret = [0,1]
    else:
        while len(deret) < N: 
            deret.append(deret[-1] + deret[-2])
    return deret
N = int(input("Masukkan jumlah N: "))
print(deretFibon(N))
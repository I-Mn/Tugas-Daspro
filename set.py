'''a = {"apel", "jeruk","ceri", "durian"}
print(a)
print(len(a))
'''
'''a = {"apel", 20, True, "durian", 8.7}
print(a)
'''
'''setA = {"apel", "jeruk", "ceri", "durian"}
for item in setA:
    print(item)
print("jeruk" in setA)
print("pisang" in setA)
'''

'''a = {"apel", "jeruk","ceri", "durian"}
a.add("semangka")
print(a)
b = {"strawberry", "blueberry"}
a.update(b)
print(a)'''

'''a = {"apel", "jeruk","ceri", "durian"}
b = {'stawberry', 'blueberry', 'apel'}
c = a.union(b)
print(c)'''

'''a = {"apel", "jeruk","ceri", "durian"}
b= {'strawberry', 'blueberry', 'apel', 'jeruk'}
c = a.intersection(b)
print(c)
a.symmetric_difference_update(b)
print(a)'''

'''a = {"apel", "jeruk","ceri", "durian"}
b= {'strawberry', 'blueberry', 'apel', 'jeruk'}
c = a.symmetric_difference(b)
print(c)'''

'''a = {"apel", "jeruk","ceri", "durian"}
b = ('strawberry', 'blueberry')
a.update(b)
print (a)

a = {"apel", "jeruk","ceri", "durian"}
b = ['strawberry', 'blueberry']
a.update(b)
print (a)'''

'''a = {"apel", "jeruk","ceri", "durian"}
a.pop()
print(a)

a.clear()
print(a)'''


kucing = {
    "nama": "Takuro",
    "umur": 2,
    "nama": "Kuro",
    "ras": "Persian",
    "jantan": True
}
'''print(len(kucing))
buah = dict(nama = "Apel", warna = "Merah", manis = True)
print(buah)
print(kucing['nama'])
print(kucing.get('ras'))
print(kucing.keys())
print(kucing.values())

kucing['umur'] = 1.5
kucing['lucu'] = True
print (kucing)
kucing.update({'warna':['putih','hitam']})
print(kucing)
'''
'''x = kucing.items()
print(x)
if'nama'in kucing :
    print("Ada key 'nama' pada dictionary")
'''

kucing.pop('jantan')
print(kucing)


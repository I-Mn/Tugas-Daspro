"""
Kautar Muhammad Mizan
RPL 1C
2404073
"""
students = {
    "Alice": "Computer Science",
    "Bob" : "Mathematics",
    "Charlie": "Physics",
    "David": "Computer Science",
    "Eva": "Mathematics"
}
jumlah = {}
for jurusan in students.values():
    if jurusan in jumlah:
        jumlah[jurusan] += 1
    else:
        jumlah[jurusan] = 1
print(f"Prodi Computer Science sebanyak {jumlah.get("Computer Science")}\n\
Prodi Mathematics sebanyak {jumlah.get("Mathematics")}\n\
Prodi Physics sebanyak {jumlah.get("Physics")}")

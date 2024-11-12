"""
Kautar Muhammad Mizan
RPL 1C
2404073
"""
student_info = {
    "Alice": {"age": 20, "major": "Computer Science"},
    "Bob": {"age": 21, "major": "Mathematics"},
    "Charlie": {"age": 19, "major": "Physics"}
}
inputan = input("Inputkan nama siswa: ")
if inputan in student_info:
    age = student_info[inputan]["age"]
    major = student_info[inputan]["major"]
    print (f"Umur {inputan} adalah {age} dan Prodinya adalah {major}")

else:
    print (f"Tidak ada nama {inputan} ditemukan")

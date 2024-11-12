'''
Kautsar Muhammad Mizan
Kelompok 6 Nexus
Kelas RPL 1C
NIM : 2404073
'''
# Daftar orang orang di sisi awal, di perahu, dan di sisi akhir
sisiAwal = {'suami': ['Suami 1', 'Suami 2', 'Suami 3'], 'istri': ['Istri 1', 'Istri 2', 'Istri 3']} # Orang orang di sisi awal, bisa ditambah jika diperlukan
sisiAkhir = {'suami': [], 'istri': []} # Daftar kosong untuk memasukan orang dari sisi awal ke sisi akhir
perahu = {'suami': [], 'istri': []} # Daftar kosong untuk dalam perahu

# Fungsi untuk memindahkan orang dari sisi awal ke perahu
def pindah(urutan, jenis):
    orang = sisiAwal[jenis][urutan] # Mendifinisikan orang dari sisi awal
    sisiAwal[jenis].remove(orang) # Menghapus orang dari daftar sisi awal
    perahu[jenis].append(orang) # Menambahkan orang ke perahu
    print(f"{orang} ke perahu") # Membuatkan status
    
# Fungsi untuk memindahkan orang dari perahu ke sisi akhir
def turun(urutan, jenis):
    orang = perahu[jenis][urutan] # Mendifinisikan orang dari perahu
    perahu[jenis].remove(orang) # Menghapus orang dari perahu
    sisiAkhir[jenis].append(orang) # Menambahkan orang ke sisi akhir
    print (f"{orang} turun dari perahu ke sisi akhir") # Membuat status

#Fungsi untuk menjelaskan orang yang telah menyebrang kembali dengan perahu menuju dekat sisi awal untuk menjemput orang berikutnya
def kembali(urutan, jenis):
    orang = perahu[jenis][urutan] # Mendefinisikan orang di perahu
    print(f"{orang} kembali") # Membuat status

#Fungsi untuk menjelaskan orang yang di perahu tengah menyebrang    
def nyebrang(urutan, jenis):
    orang = perahu[jenis][urutan] # Mendifinisikan orang di perahu
    print (f"{orang} menyebrang ke sisi akhir") # Membuat status

#Fungsi untuk menjelaskan siapa saja yang berada di sisi awal, di perahu, dan di sisi akhir    
def hasil():
    print(f"Sisi awal: {list(sisiAwal.values())}, Perahu: {list(perahu.values())}, Sebrang: {list(sisiAkhir.values())}") # Membuat status


# Loop untuk memindahkan orang, tidak akan berhenti selama masih ada orang di sisiAwal
while len(sisiAwal['suami']) + len(sisiAwal['istri']) > 0:
    
    #Untuk proses pertama saat tidak ada orang di perahu dan di sisi akhir
    if len(sisiAkhir['suami']) + len(sisiAkhir['istri']) == 0 and len(perahu['istri']) + len(perahu['suami']) == 0:
        pindah(0, 'suami') # Memindahkan suami 1 ke perahu
        pindah(0, 'istri') # Memindahkan istri 1 ke perahu
        nyebrang(0,'suami') # Menjelaskan suami 1 menyebrang
        nyebrang(0, 'istri') # Menjelaskan istri 1 menyebrang
        turun(0, 'suami') # Memindahkan suami 1 ke sisi akhir
        hasil() # Mencetak hasil saat ini
        
    # Untuk proses selanjutnya
    else:
        
        # Jika di sisi akhir jumlah suami dan istri sama, setiap orang berpasangan
        if len(sisiAkhir['suami']) == len(sisiAkhir['istri']):
            kembali(0, 'istri') # Membuat kembali istri yang suaminya tidak ada di sisi akhir kembali ke sisi awal
            pindah(0, 'suami')  # Memindahkan suami ke perahu
            nyebrang(0, 'istri') # Menjelaskan istri menyebrang
            nyebrang(0, 'suami') # Menjelaskan suami menyebrang
            turun(0,'suami') # Memindahkan suami dari perahu ke sisi akhir
            
            # Jika di sisi awal masih ada orang
            if len(sisiAwal['suami']) + len(sisiAwal['istri']) > 0 :
                hasil() # Mencetak hasil saat ini
                
        # Jika di sisi akhir jumlah suami dan istri tidak sama
        else:
            kembali(0, 'istri') # Membuat kembali istri yang baru saja menyebrang kembali ke sisi awal
            pindah(0, 'istri') # Memindahkan istri suami lain ke perahu
            nyebrang (0, 'istri') # Menjelaskan istri menyebrang
            nyebrang (1, 'istri') # Menjelaskan istri suami lain menyebrang
            turun (0,'istri') # Memindahkan istri yang sebelumnya (yang suaminya sudah ada di sisi akhir) ke sisi akhir
            hasil() # Mencetak hasil saat ini
turun(0, 'istri') # Memindahkan istri yang terakhir ke sisi akhir
hasil() # Mencetak hasil akhir dimana semua orang sudah berada di sisi akhir
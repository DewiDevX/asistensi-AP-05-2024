kalimat = "NegaraKesatuanRepublikIndonesia"
# Mendefinisikan variabel 'kalimat' yang berisi string

kata_kata = kalimat.split()
# Memisahkan kalimat menjadi daftar kata-kata menggunakan metode 'split()'
# Hasilnya adalah ['Negara', 'Kesatuan', 'Republik', 'Indonesia']

akronim = "".join([kata[0].upper() for kata in kata_kata])
# Mengubah huruf pertama tersebut menjadi huruf kapital (uppercase)
# Menggabungkan semua huruf pertama yang diambil menjadi string tunggal
# Hasilnya adalah "NKRI"

print(akronim)
# Mencetak hasil akronim
 
  

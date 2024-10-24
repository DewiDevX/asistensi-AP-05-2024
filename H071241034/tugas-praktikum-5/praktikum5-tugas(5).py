def caesar_cipher(text, shift):
    # Mendefinisikan fungsi caesar_cipher yang menerima dua argumen: 'text' (teks yang akan dienkripsi) dan 'shift' (jumlah pergeseran karakter)
    
    alfabet = 'abcdefghijklmnopqrstuvwxyz'
    hasil = ''
    
    for karakter in text:        
        if karakter.isalpha():
            # Jika karakter adalah huruf (baik besar maupun kecil)
            
            index = alfabet.index(karakter.lower())
            # Mencari indeks huruf pada alfabet dalam format lowercase
            
            if karakter.islower():
                # Jika karakter adalah huruf kecil
                hasil = hasil + alfabet[(index + shift) % 26].lower()
                # Menambahkan karakter hasil pergeseran ke 'hasil' dengan menjaga format huruf kecil
                
            else:
                # Jika karakter adalah huruf besar
                hasil = hasil + alfabet[(index + shift) % 26].upper()
                # Menambahkan karakter hasil pergeseran ke 'hasil' dengan menjaga format huruf besar
                
        elif karakter.isdigit() or karakter in '@#!$%&*()_+-={}|[]:;<>?,./':
            hasil = hasil + karakter
            # Langsung menambahkan karakter tersebut ke variabel 'hasil' tanpa perubahan
            
        else:
            hasil = hasil + karakter
            # Langsung menambahkan karakter tersebut ke variabel 'hasil'
    
    return hasil

# Input dari pengguna untuk teks yang akan dienkripsi
text = input("Masukkan string: ")

# Input dari pengguna untuk jumlah pergeseran
shift = int(input("Masukkan jumlah pergeseran: "))

# Menampilkan teks asli dan jumlah pergeseran
print('Text : ', text)
print('Shift : ', shift)

# Menampilkan hasil enkripsi dengan menggunakan fungsi caesar_cipher
print('Cipher : ', caesar_cipher(text, shift))

       



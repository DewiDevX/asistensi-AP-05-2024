def anagram(char):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'  # Definisikan string berisi huruf-huruf alfabet
    for i in range(26): 
        if char == alphabet[i]:  # Jika karakter 'char' sama dengan huruf pada posisi 'i' dalam alfabet
            return i  # Kembalikan indeks (posisi) dari huruf dalam alfabet

def min_deletions_to_anagram(s1, s2):  # Menghitung jumlah karakter yang perlu dihapus untuk membuat anagram
    freq_s1 = [0] * 26  # Inisialisasi daftar untuk frekuensi huruf di s1
    freq_s2 = [0] * 26  # Inisialisasi daftar untuk frekuensi huruf di s2
    
    # Menghitung frekuensi setiap huruf dalam s1
    for char in s1:
        index = anagram(char.lower())  # Dapatkan indeks dari karakter, konversi ke huruf kecil
        if index is not None:  # Pastikan karakter adalah huruf (index tidak None)
            freq_s1[index] += 1  # Tingkatkan frekuensi huruf di s1
    
    # Menghitung frekuensi setiap huruf dalam s2
    for char in s2:
        index = anagram(char.lower())  # Dapatkan indeks dari karakter, konversi ke huruf kecil
        if index is not None:  # Pastikan karakter adalah huruf (index tidak None)
            freq_s2[index] += 1  # Tingkatkan frekuensi huruf di s2

    deletions = 0  # Inisialisasi jumlah penghapusan
    for i in range(26):  # Iterasi untuk setiap huruf dalam alfabet
        # Menghitung jumlah karakter yang perlu dihapus dari s1 dan s2
        if freq_s1[i] > freq_s2[i]:  
            deletions += freq_s1[i] - freq_s2[i]  # Jika lebih banyak di s1, hitung selisih
        else:
            deletions += freq_s2[i] - freq_s1[i]  # Jika lebih banyak di s2, hitung selisih
    
    return deletions  # Kembalikan jumlah total penghapusan yang diperlukan

# Input dua string dari pengguna
s1 = input("Masukkan string pertama: ")
s2 = input("Masukkan string kedua: ")
# Hitung jumlah minimum penghapusan untuk membuat anagram
hasil = min_deletions_to_anagram(s1, s2)
print(f"Jumlah minimum penghapusan untuk membuat anagram: {hasil}")  # Tampilkan hasil

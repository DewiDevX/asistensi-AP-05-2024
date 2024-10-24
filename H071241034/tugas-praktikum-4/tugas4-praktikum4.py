def kalkulator():
    print("selamat datang dikakulator sederhana")
    try:
        # Meminta input angka pertama dari pengguna
        angka1 = float(input("Masukkan angka pertama: "))
        
        # Meminta input angka kedua dari pengguna
        angka2 = float(input("Masukkan angka kedua: "))
        
        # Meminta input operasi yang diinginkan dari pengguna
        operasi = input("Masukkan operasi (+, -, *, /): ")
        
        # Melakukan operasi berdasarkan input pengguna
        if operasi == '+':
            hasil = angka1 + angka2
        elif operasi == '-':
            hasil = angka1 - angka2
        elif operasi == '*':
            hasil = angka1 * angka2
        elif operasi == '/':
            # Menangani pembagian dengan nol
            if angka2 != 0:
                hasil = angka1 / angka2
            else:
                print("Error: Pembagian dengan nol tidak diperbolehkan.")
                return
        else:
            print("Operasi tidak valid. Silakan masukkan operasi yang benar (+, -, *, /).")
            return
        
        # Menampilkan hasil dari operasi
        print(f"Hasil: {hasil}")
    
    except ValueError:
        print("Input tidak valid. Pastikan Anda memasukkan angka.")
      

# Menjalankan program kalkulator
kalkulator()

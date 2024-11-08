def menu_awal():
    print("\n---Sistem Pemesanan Tiket Bioskop---")
    print("1. Admin")
    print("2. Pengunjung")
    print("3. Keluar")

def menu_admin():
    print("\n---Menu Admin---")
    print("1. Tambah Film")
    print("2. Hapus Film")
    print("3. Daftar Tiket")
    print("4. Hapus Tiket")
    print("5. Lihat Detail Tiket")
    print("6. Kembali")

daftar_film = []

def tambah_film():
    while True:
        print("\n---Tambah Film---")
        tambah = input("Masukkan nama film yang ingin ditambahkan (atau tekan Enter untuk kembali): ")
        if tambah != "":
            print(f"Film '{tambah}' berhasil ditambahkan.")
            daftar_film.append(f"{tambah}")
        else:
            print("\nKembali ke Menu Admin")
            return

def hapus_film():
    while True:
        print("\n---Hapus Film---")
        for i, film in enumerate(daftar_film, start=1):
            print(f"{i}. {film}")
        print("0. Kembali")
        try:
            hapus = int(input("Masukkan nomor film yang ingin dihapus (atau 0 untuk kembali): "))
            if hapus > 0 and hapus <= len(daftar_film):
                index = hapus - 1
                dihapus = daftar_film.pop(index)
                print(f"Film '{dihapus}' berhasil dihapus")    
            elif hapus == 0:
                print("\nKembali ke Menu Admin.")
                break
            else:
                print("Nomor film tidak valid.")
        except ValueError:
            print("Input tidak valid.")

def menu_pengunjung():
    print("\n---Menu Pengunjung---")
    print("1. Lihat daftar film")
    print("2. Beli tiket")
    print("3. Kembali")

def lihat_Daftarfilm():
    if not daftar_film:
        print("Daftar film kosong.")
    else:
        print("---Daftar Film---")
        for i, film in enumerate(daftar_film, start=1):
            print(f"{i}. {film}")

import random
import datetime
import os

id_tiket = []

def beli_tiket():
    if not daftar_film:
        print("Tidak ada film yang tersedia untuk dibeli.")
        return
    for i, film in enumerate(daftar_film, start=1):
        print(f"{i}. {film}")
    print("0. Kembali")
    beli = input("Pilih nomor film yang ingin ditonton (atau 0 untuk kembali): ")
    if beli == "0":
        return
    try:
        nomor_film = int(beli)
        if 1 <= nomor_film <= len(daftar_film):
            pilih_film = daftar_film[nomor_film - 1]
            ID = f"TICK{random.randint(1000000000,9999999999)}"
            id_tiket.append(f"{ID}")
            waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            lebar_tiket = 40
            os.makedirs('tickets', exist_ok=True)

            with open(f"tickets/{ID}.txt", "a") as file:
                file.write("+" + "-" * lebar_tiket + "+\n")                
                file.write("|" + " " + "TIKET BIOSKOP".center(lebar_tiket - 2) + " " + "|\n")
                file.write("+" + "-" * lebar_tiket + "+\n")
                file.write("|" + " ID Tiket: " + ID + " " * (lebar_tiket - len(ID) - 9) + "|\n")
                file.write("|" + " Film: " + pilih_film + " " * (lebar_tiket - len(pilih_film) - 5) + "|\n")
                file.write("|" + " Tanggal: " + waktu + " " * (lebar_tiket - len(waktu) - 10) + "|\n")
                file.write("+" + "-" * lebar_tiket + "+\n")                
                file.write("|" + " " + "Terima Kasih telah membeli tiket Anda!".center(lebar_tiket - 2) + "|\n")
                file.write("+" + "-" * lebar_tiket + "+\n")
            
            print(f"Tiket berhasil dibeli. ID Tiket Anda: {ID}")
            print(f"File tiket telah dibuat: tickets/{ID}.txt")
        else:
            print("Nomor film tidak valid.")
    except ValueError:
        print("Input tidak valid.")

def daftar_tiket():
    if not id_tiket:
        print("Daftar tiket kosong.")
    else:
        print("---Daftar Tiket---")
        for i, tiket in enumerate(id_tiket, start=1):
            print(f"{i}. {tiket}")

def hapus_tiket():
    if not id_tiket:
        print("Daftar tiket kosong.")
        return
    print("---Hapus Tiket---")
    for i, tiket in enumerate(id_tiket, start=1):
        print(f"{i}. {tiket}")
    try:
        pilihan = int(input("Masukkan nomor tiket yang ingin dihapus (atau 0 untuk kembali): "))
        if 1 <= pilihan <= len(id_tiket):
            tiket_dihapus = id_tiket.pop(pilihan - 1)
            os.remove(f"tickets/{tiket_dihapus}.txt")
            print(f"Tiket '{tiket_dihapus}' berhasil dihapus.")
        elif pilihan == 0:
            print("Kembali ke Menu Admin.")
        else:
            print("Nomor tiket tidak valid.")
    except (ValueError, FileNotFoundError):
        print("Tiket tidak ditemukan atau input tidak valid.")

def lihat_detail_tiket():
    if not id_tiket:
        print("Daftar tiket kosong.")
        return
    
    # Menampilkan daftar tiket yang tersedia
    print("---Daftar Tiket---")
    for i, tiket in enumerate(id_tiket, start=1):
        print(f"{i}. {tiket}")
    
    # Meminta ID tiket yang ingin dilihat detailnya
    tiket_id = input("Masukkan ID Tiket yang ingin dilihat: ")
    
    # Mencoba membuka file tiket yang sesuai dengan ID yang dimasukkan
    try:
        with open(f"tickets/{tiket_id}.txt", "r") as file:
            print("\n---Detail Tiket---")
            print(file.read())
    except FileNotFoundError:
        print("Tiket tidak ditemukan.")
 

def main():
    while True:
        menu_awal()
        peran = input("Pilih peran (1/2/3): ")
        if peran == "1":
            while True:
                menu_admin()
                opsi = input("Pilih Opsi (1/2/3/4/5/6): ")
                if opsi == "6":
                    print("\nKembali ke Menu Utama.")
                    break
                elif opsi == "1":
                    tambah_film()
                elif opsi == "2":
                    hapus_film()
                elif opsi == "3":
                    daftar_tiket()
                elif opsi == "4":
                    hapus_tiket()
                elif opsi == "5":
                    lihat_detail_tiket()
                else:
                    print("Mohon masukkan angka 1/2/3/4/5/6")
        elif peran == "2":
            while True:
                menu_pengunjung()
                opsi = input("Pilih opsi (1/2/3): ")
                if opsi == "1":
                    lihat_Daftarfilm()
                elif opsi == "2":
                    beli_tiket()
                elif opsi == "3":
                    print("\nKembali ke Menu Utama.")
                    break
        elif peran == "3":
            print("Terima Kasih telah menggunakan sistem ini.")
            break
        else:
            print("Mohon masukkan angka 1, 2, atau 3.")

main()

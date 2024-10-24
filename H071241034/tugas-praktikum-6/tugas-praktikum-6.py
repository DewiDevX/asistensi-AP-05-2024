inventory = {}

def tampilkan_menu():
    print("==== Menu Utama ====")
    print("1. Tambah Barang")
    print("2. Hapus Barang")
    print("3. Tampilkan Daftar Barang")
    print("4. Cari Barang")
    print("5. Update Data Barang")
    print("6. Keluar")
    
def input_angka( permintaan, tipe=float):
    while True:
        try:
            nilai = tipe(input(permintaan))
            if nilai < 0:
                print("Nilai tidak boleh negatif.")
            else:
                return nilai
        except ValueError:
            print("Input harus berupa angka.")
            
def tambah_barang():
    id_barang = input("Masukkan ID Barang: ")
    if id_barang in inventory:
        print("Barang dengan ID ini sudah ada.")
    else:
        nama_barang = input("Masukkan Nama Barang: ")
        jumlah_barang = input_angka(int("Masukkan Jumlah Barang: "))
        harga = input_angka("Masukkan harga per unit: ")
        inventory[id_barang] = {'nama': nama_barang, 'jumlah': jumlah_barang, 'harga': harga}
        print(f"Barang '{nama_barang}' berhasil ditambahkan.")

def hapus_barang(): 
    id_barang = input("Masukkan ID Barang yang akan dihapus: ")
    if id_barang in inventory:
        del inventory[id_barang]
        print(f"Barang dengan ID {id_barang} berhasil dihapus.")
    else:
        print("Barang tidak ditemukan.")

def tampilkan_daftar_barang():
    if not inventory:
        print("Inventory kosong.")
    else:
        print("=== Daftar Barang ===")
        for id_barang, data in inventory.items():
            print(f"ID: {id_barang}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga: {data['harga']}")
            
def cari_barang():
    id_barang = input("Masukkan ID Barang yang dicari: ")
    if id_barang in inventory:
        data = inventory[id_barang]
        print(f"ID: {id_barang}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga: {data['harga']}")
    else:
        print("Barang tidak ditemukan.")

def update_barang():
    id_barang = input("Masukkan ID Barang yang akan diupdate: ")
    if id_barang in inventory:
        nama_barang = input("Masukkan Nama Barang Baru: ")
        jumlah_barang = input_angka("Masukkan Jumlah Barang Baru: ", int)
        harga = input_angka("Masukkan harga: ")
        inventory[id_barang] = {'nama': nama_barang, 'jumlah': jumlah_barang, 'harga': harga}
        print(f"Barang dengan ID {id_barang} berhasil diperbarui.")
    else:
        print("Barang tidak ditemukan.")
        
def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-6): ")
        if pilihan == "1":
            tambah_barang()
        elif pilihan == "2":
            hapus_barang()
        elif pilihan == "3":
            tampilkan_daftar_barang()
        elif pilihan == "4":
            cari_barang()
        elif pilihan == "5":
            update_barang()
        elif pilihan == "6":
            print("Terima Kasih telah menggunakan program inventori.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

main()

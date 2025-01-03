def pemburu_harta_karun():
    total_distance = 0
    while True:
        try:
            langkah = int(input('Masukkan langkah (meter) atau 0 untuk selesai: '))
            if langkah < 0:
                print('Input tidak valid. Permainan berhenti.')
                break
            if langkah == 0:
                print(f'Total jarak: {total_distance} meter')

                # Cek kondisi bahaya berdasarkan total jarak
                if total_distance > 20:
                    print('Ada bahaya: Ya')
                    print('Keputusan: Tidak aman untuk menggali harta karun. Coba lagi!')
                elif total_distance < 50:
                    print('Ada bahaya: Tidak')
                    print('Keputusan: Tidak menemukan harta karun. Coba lagi!')
                else:
                    print('Ada bahaya: Tidak')
                    print('Keputusan: Aman! Kamu tepat menemukan harta karun dan menang!')
                break

            # Tambahkan langkah ke total jarak
            total_distance += langkah

        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat.")

pemburu_harta_karun()

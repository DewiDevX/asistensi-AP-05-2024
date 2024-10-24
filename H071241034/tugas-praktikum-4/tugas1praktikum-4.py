import random

def tarik_kartu():
    return random.randint(1, 11)

def blackjack():
    print("Welcome to Blackjack!")

    pemain = tarik_kartu()
    dealer = tarik_kartu()

    print(f"Kartu anda sekarang adalah: {pemain}")

    while pemain <= 21:
        ambil_kartu = input("Apakah masih akan mengambil kartu? (y/n): ")

        if ambil_kartu == "y":
            pemain = pemain + tarik_kartu()
            print(f"Kartu anda sekarang adalah: {pemain}")

            if pemain > 21:
                print(f"Anda kalah! ")
                return  # Keluarkan pemain dari permainan jika kalah

        if ambil_kartu == "n":
            break

    if pemain <= 21:
        print(f"Kartu dealer adalah: {dealer}")

        while dealer <= 17:
            dealer = dealer + tarik_kartu()
            print(f"Kartu dealer sekarang adalah: {dealer}")
            
            # Jika dealer lebih dari 21, maka dealer kalah
            if dealer > 21:
                print(f"Anda Menang! Kartu dealer adalah {dealer}")
                return  # Dealer kalah, akhiri permainan

    # Kondisi setelah dealer selesai mengambil kartu
    if pemain > dealer:
        print("Anda Menang!")
    elif pemain == dealer:
        print("Permainan Seri!")
    else:
        print("Dealer Menang!")

blackjack()



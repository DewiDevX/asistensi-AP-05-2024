import re

def is_valid_username(username):
    pattern = r"^[A-Za-z0-9_]{5,20}$"  # Validasi username 5-20 karakter, hanya huruf, angka, dan underscore
    return re.search(pattern, username) is not None

def is_valid_email(email):
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(com|co\.id)$"  # Validasi format email dengan domain .com atau .co.id
    return re.search(pattern, email) is not None

def is_valid_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"  # Validasi password sesuai ketentuan
    return re.search(pattern, password) is not None

# ------
username = input("Masukkan username: ")

if is_valid_username(username):
    email = input("Masukkan email: ")

    if is_valid_email(email):
        password = input("Masukkan password: ")

        if is_valid_password(password):
            print(f"\nRegistrasi berhasil! Halo {username}")  # Menampilkan sapaan dengan username
        else:
            print("\nPassword yang kamu input beresiko dihack. Registrasi gagal.")
    else:
        print("\nEmail yang kamu input tidak valid. Registrasi gagal!")
else:
    print("\nInputan username tidak valid dalam sistem. Registrasi gagal!")

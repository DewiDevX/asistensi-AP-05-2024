import re

def validasi_string(s):
    
    # Cek 40 karakter pertama
    if not re.match(r'^[A-Za-z0-9]{40}$', s[:40]):
        return False
    
    # Cek 5 karakter terakhir
    if not re.match(r'^[13579\s]{5}$', s[40:]):
      return False
    
    return True

#  penggunaan
input_string = input("Masukkan string: ")
result = validasi_string(input_string)
print(result)


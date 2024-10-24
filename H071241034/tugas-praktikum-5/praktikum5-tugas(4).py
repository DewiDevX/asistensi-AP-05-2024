def print_substrings(s):
    # Loop untuk panjang substring (1 hingga panjang maksimum string)
    for A in range(1, len(s) + 1):
        # Loop untuk memulai substring dari setiap posisi
        for i in range(len(s) - A + 1):
            print(s[i:i + A])

# Meminta input dari pengguna
s = input("input your string : ")

# Mencetak semua substring
print("===================")
print_substrings(s)



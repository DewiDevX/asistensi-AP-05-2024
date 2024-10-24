def palindrome():
    kata = input("Masukkan kata: ")
    palindrome = (''.join(reversed(kata))) #membalikkan urutan karakter kata dan menggabungkan 

    if kata == palindrome: #pengecekan palindrom
        print("Palindrome")
    else:
        print("Not Palindrome")  

palindrome()




total_belanja = int(input("Masukkan Total Belanja anda : "))
konfir_member = str(input("Apakah Kamu Termasuk Member? (y/n) : "))

if konfir_member == "y":
    if(total_belanja > 1000000):
        print("Selamat anda mendapatkan diskon sebesar 8%")
    elif (total_belanja >= 500000 and total_belanja <= 1000000):
        print("Selamat anda mendapatkan diskon sebesar 7%")
    else:
        print("Maaf, Kamu tidak mendapat discount :(")
elif konfir_member =="n":
    if(total_belanja > 1000000):
        print("Selamat anda mendapatkan diskon sebesar 3%")
    elif (total_belanja >= 500000 and total_belanja <= 1000000):
        print("Selamat anda mendapatkan diskon sebesar 2%")
    else:
        print("Maaf, Kamu tidak mendapat discount :(")
else:
    print("INPUT SALAH")
input_hari = str(input("Masukkan Hari : "))
hari = input_hari.lower()

if (hari == 'senin' ):
    print("Seragam anda hari ini merah")

elif (hari == 'selasa' or hari =='rabu'):
    print("Seragam anda hari ini putih")

elif (hari == 'kamis' or hari =='sabtu'):
    print("Seragam anda hari ini bebas")

elif (hari == 'jumat'):
    print("Seragam anda hari ini batik")

else:
    print('Anda menginputkan hari yang tidak terdaftar')

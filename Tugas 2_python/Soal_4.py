nilai = int(input('masukkan nilai n : '))

for baris in range(nilai):
    if baris==0:
        print("*"*nilai)
    elif baris == nilai-1:
        print("*"*nilai)
    else:
        print("*"+ "#"*(nilai-2) + "*")
#Program anak ayam

ayam = int(input("Masukkan jumlah anak ayam : "))
print()
print ("Anak ayam turun",ayam)
for i in range(ayam):
    a = ayam - i
    b = a - 1
    if b >= 1 :
        print ("Anak ayam turun",a,"mati satu tinggal",b)
    else:
        print ("Anak ayam turun",a,"mati satu tinggal induknya")
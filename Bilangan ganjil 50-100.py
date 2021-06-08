#Program bilangan ganjil 50-100

awal = int(input("Masukkan angka awal : "))
akhir = int(input("Masukkan angka akhir : "))

a = awal
b = akhir

print ("Bilangan ganjil mulai dari 50-100 :")
for bilangan_ganjil in range(a,b,1):
    if bilangan_ganjil % 2 == 1:
        print (bilangan_ganjil, end=",")
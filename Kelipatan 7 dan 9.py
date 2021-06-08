#Program kelipatan 7 dan 9 antara 100-200

#Kelipatan 7

awal = int(input("Masukkan angka awal : "))
akhir = int(input("Masukkan angka akhir : "))

a = awal
b = akhir
print ("Kelipatan angka 7 mulai dari 100-200 :")
for kelipatan7 in range(a,b,1):
    if kelipatan7 % 7 == 2:
        print (kelipatan7, end=",")

print()
#Kelipatan 9

print ("Kelipatan angka 9 mulai dari 100-200 :")
for kelipatan9 in range(a,b,1):
    if kelipatan9 % 9 == 1:
        print (kelipatan9, end=",")
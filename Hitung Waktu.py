print ("hitung dari detik berapa hari, jam, menit dan detik")
#input data
detik1 = int(input("Masukkan detik 1 :"))
#Rumus
hari = detik1//86400
jam = detik1%86400//3600
menit = detik1%86400%3600//60
detik2 = detik1%86400%3600%60
#Hasil
print ("Hasil dari hitung waktu hari =",hari)
print ("Hasil dari hitung waktu jam =",jam)
print ("Hasil dari hitung waktu menit =",menit)
print ("Hasil dari hitung waktu detik2 =",detik2)
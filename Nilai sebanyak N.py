#Program nilai sebanyak N kemudian tampilkan seluruh nilai beserta rata-rata, nilai min dan max

data = [27,5,20,19,30,7,45]

nilai_min = min(data)
nilai_max = max(data)
jumlah_nilai = sum(data)
jumlah_elemen = len(data)
rata_rata = jumlah_nilai / jumlah_elemen

print("List nilai :", data)
print("Nilai terbesarnya (Max) adalah : ",nilai_max)
print("Nilai terkecilnya (Min) adalah : ",nilai_min)
print("Rata-ratanya adalah : ",rata_rata)
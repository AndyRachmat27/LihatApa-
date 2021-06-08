print ("Program Perhitungan Pembayaran Donat")
#input data
jumlah_donat = 12
harga_donat = 10000
diskon = 0
hasil1 = 0
total_donat = jumlah_donat
#Rumus
for x in range(6):
        if jumlah_donat >= 6 :
            jumlah_donat = jumlah_donat - 6
            diskon = diskon + 10000
            print(diskon)

hasil = (total_donat * 10000) - diskon
print ("Donat yang dibeli : ",total_donat,"\nTotal : ",hasil)

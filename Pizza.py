print ("Program Pembelian Pizza")
#input data
jenis_pizza = int(input("Masukkan jenis pizza : no "))
if jenis_pizza < 2 :
    print ("Pizza Supreme Deluxe")
    pizza = 139300
elif jenis_pizza < 3 :
    print ("Pizza Meat Lovers")
    pizza = 145000
elif jenis_pizza < 4 :
    print ("Pizza Cheesy Mayo")
    pizza = 123799
jumlah_pizza = int(input("Masukkan jumlah pizza : "))
#Rumus
pesanan = pizza * jumlah_pizza
proses = pesanan / 100
ppn = pesanan * 0.1
hargatotal = ppn + pesanan
#Hasil
print ("PPN yang harus dibayar adalah",ppn)
print ("Total harga yang harus dibayar adalah Rp",+hargatotal)
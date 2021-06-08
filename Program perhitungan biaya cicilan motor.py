#Program perhitungan biaya cicilan motor

nama = input("Masukkan nama : ")
alamat = input("Masukkan alamat : ")
hp = input("No. HP : ")

print("1. Vixion = Rp 24.500.000")
print("2. Honda CBR = Rp 70.000.000")
jenis_motor = int(input("Pilih jenis motor (1/2) : "))
if jenis_motor == 1:
    harga = 24500000
elif jenis_motor == 2:
    harga = 70000000

metode = input("Pilih metode pembayaran (tunai/kredit) : ")
if metode == "tunai":
    print()
    print("Detail Pembayaran Berupa Tunai")
    print()
    print("Nama         : {}".format(nama))
    print("Alamat       : {}".format(alamat))
    print("No. HP       : {}".format(hp))
    print("Harga        : {}".format(harga))
    print("Total bayar  :",harga)
elif metode == "kredit":
    hargapokok = harga
    uangmuka = int(input("Masukkan jumlah uang muka : "))
    jangkacicil = int(input("Masukkan jangka cicilan (Bulan) : "))
    hutangpokok = harga - uangmuka
    angsuran = hutangpokok / jangkacicil
    bunga = 0.1 * hutangpokok
    total_angsuran = bunga + angsuran
    print()
    print("Detail Pembayaran Berupa Kredit")
    print()
    print("Nama                                     : {}".format(nama))
    print("Alamat                                   : {}".format(alamat))
    print("No. HP                                   : {}".format(hp))
    print("Harga pokok                              : {}".format(harga))
    print("Bunga per bulan (1% dari harga pokok)    : ",bunga)
    print("Angsuran per bulan                       : ",angsuran)
    print("Cicilan per bulan                        : ",total_angsuran)
    print("Total bayar                              : ",(harga + bunga))

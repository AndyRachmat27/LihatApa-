print ("Program Menghitung IP")
#input data
sks = 3
matkul = 5
#Rumus
def check(n) :
    if n == "A" :
        return 4
    elif n == "B" :
        return 3
    elif n == "C" :
        return 2
    elif n == "D" :
        return 1
    elif n == "E" :
        return 0
    else :
        return
#input nama mahasiswa
namamahasiswa = input("Nama Mahasiswa :")
#input nilai mata kuliah
matakuliah1 = check(input("Masukkan nilai matkul 1 (A/B/C/D/E) : "))
matakuliah2 = check(input("Masukkan nilai matkul 2 (A/B/C/D/E) : "))
matakuliah3 = check(input("Masukkan nilai matkul 3 (A/B/C/D/E) : "))
matakuliah4 = check(input("Masukkan nilai matkul 4 (A/B/C/D/E) : "))
matakuliah5 = check(input("Masukkan nilai matkul 5 (A/B/C/D/E) : "))
#proses
tn = ((sks*matakuliah1)+(sks*matakuliah2)+(sks*matakuliah3)+(sks*matakuliah4)+(sks*matakuliah5))
tk = sks * matkul
ip = tn / tk
#hasil
print ("Mahasiswa",namamahasiswa,"mendapatkan ip :",ip)
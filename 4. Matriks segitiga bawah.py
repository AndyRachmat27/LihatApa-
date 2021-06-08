#Program matriks segitiga bawah

cek = input("Mengecek matriks segitiga bawah/bukan segitiga bawah : ") #Ketik segitiga/bukan segitiga
if cek == "segitiga" :
    matriksA = [ [1,0,0,0,0], [6,5,0,0,0], [8,2,4,0,0], [7,6,5,4,0], [5,6,7,8,9]]
    matriksX = matriksA
    print("Matriks ini merupakan matriks segitiga bawah")

    for i in range (0,5) :
        for j in range (0,5) :
            print (matriksX[i][j], end = ' ')
        print()
else :
    matriksB = [ [1,6,8,7,5], [2,5,2,6,6], [3,1,4,5,7], [4,7,9,4,8], [5,3,3,3,9]]
    matriksY = matriksB
    print("Matriks ini adalah bukan matriks segitiga bawah")

    for k in range (0,5) :
        for l in range (0,5) :
            print (matriksY[k][l], end = ' ')
        print()
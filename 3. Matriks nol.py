#Program matriks nol

cek = input("Mengecek matriks nol/bukan nol : ") #Ketik matriks nol/bukan nol
if cek == "nol" :
    matriksA = [ [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
    matriksX = matriksA
    print("Matriks ini merupakan matriks nol")

    for i in range (0,5) :
        for j in range (0,5) :
            print (matriksX[i][j], end = ' ')
        print()
else :
    matriksB = [ [1,6,8,7,5], [2,5,2,6,6], [3,1,4,5,7], [4,7,9,4,8], [5,3,3,3,9]]
    matriksY = matriksB
    print("Matriks ini merupakan bukan matriks nol")

    for k in range (0,5) :
        for l in range (0,5) :
            print (matriksY[k][l], end = ' ')
        print()
#Program matriks simetri

cek = input("Mengecek sebuah matriks simetri/matriks bukan simetri  : ") #Ketik matriks simetri/bukan simetri
if cek == "matriks simetri" :
    matriksA = [ [1,2,3,4], [2,6,7,8], [3,7,5,9], [4,8,9,1]]
    matriksX = matriksA
    print("Matriks ini merupakan matriks simetri")

    for i in range (0,4) :
        for j in range (0,4) :
            print (matriksX[i][j], end = ' ')
        print()
else :
    matriksB = [ [1,2,9,4], [2,6,3,8], [3,7,5,8], [4,8,9,1]]
    matriksY = matriksB
    print("Matriks ini merupakan bukan matriks simetri")

    for k in range (0,4) :
        for l in range (0,4) :
            print (matriksY[k][l], end = ' ')
        print()
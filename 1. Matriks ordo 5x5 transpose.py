#Program matriks ordo 5x5 transpose

matriksA = [ [1,2,3,4,5], [6,5,1,7,3], [8,2,4,9,3], [7,6,5,4,3], [5,6,7,8,9]]
matX = matriksA

print("Matriks asal :")
print()
for i in range (0,5) :
    for j in range (0,5) :
        print (matX[i][j], end = '  ')
    print()

print()
matriksB = [ [1,6,8,7,5], [2,5,2,6,6], [3,1,4,5,7], [4,7,9,4,8], [5,3,3,3,9]]
matY = matriksB

print("Matriks transpose :")
print()
for k in range (0,5) :
    for l in range (0,5) :
        print (matY[k][l], end = '  ')
    print()
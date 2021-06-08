#Program perkalian matriks

from random import randint
matA = []
matB = []

b = int(input("Baris matriks = "))
k = int(input("Kolom matriks = "))

print("Matriks A")
for i in range (b) :
    matAelemen = []
    for j in range (k) :
        bil = randint(1,9)
        print (bil, end= ' ')
        matAelemen.append(bil)
    print()
    matA.append(matAelemen)

print()
print("Matriks B")
for i in range (b) :
    matBelemen = []
    for j in range (k) :
        bil = randint(1,9)
        print (bil, end= ' ')
        matBelemen.append(bil)
    print()
    matB.append(matBelemen)

print()
print("Hasil perkalian matriks A & B adalah")
for i in range (b) :
    for j in range (k) :
        matC = matA[i][j]*matB[i][j]
        print(matC, end= ' ')
    print()
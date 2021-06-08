#Program bilangan acak dan jumlahkan semuanya

from random import randint
from random import seed

seed(20)
for i in range(10):
    bil = randint(0, 50)
    print(bil, end = " ")
print()
data = [46,43,50,49,9,16,43,40,6,20]
sum = 0
for each in data :
    sum = sum + each
print("Jumlah angka tersebut adalah",sum)
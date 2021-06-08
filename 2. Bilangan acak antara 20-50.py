#Program bilangan acak antara 20-50 tampilkan bilangan ganjil

from random import randint
from random import seed

seed(5)
for i in range(10):
    bil = randint(20,50)
    print(bil, end = " ")
print()

seed(5)
for i in range(10):
    bil = randint(20,50)
    if bil % 2 == 1:
        print("Bilangan ganjil : ",bil)
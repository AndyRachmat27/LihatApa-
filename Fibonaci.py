#Program deret Fibonaci

bil1=1
bil2=1

print ("Deret Fibonaci :")
for i in range (15):
    print (bil1, end=",")
    fb = bil2 + bil1
    bil1 = bil2
    bil2 = fb
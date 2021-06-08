print ("Program Usia")
#input data
usia = int(input("Masukkan usia : "))
#Rumus
if usia < 5 :
    print ("Toddler")
elif 6 < usia < 12 :
    print ("Kids")
elif 13 < usia < 20 :
    print ("Teenager")
elif 21 < usia < 40 :
    print ("Young")
elif 41 < usia < 60 :
    print ("Adult")
if usia > 60 :
    print ("Old")
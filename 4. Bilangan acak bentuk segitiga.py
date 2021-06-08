#Program bilangan acak 0-9 tampilkan dalam bentuk segitiga

from random import randint

string = ""

i = 9
bar = i

while bar >= 0:
	kol = bar
	while kol > 0:
		string = string + "   "
		kol = kol - 1
	kiri = 1
	while kiri < (i - (bar-1)):
		string = string + " " + str(randint(1,9)) + " "
		kiri = kiri + 1		
	kanan = 1
	while kanan < kiri -1:
		string = string + " " + str(randint(1,9)) + " "
		kanan = kanan + 1	

	string = string + "\n\n"
	bar = bar - 1
print (string)
#Program perulangan bersarang b

string = ""

i = 9
bar = i
no = 0

while bar >= 0:
	kol = bar
	while kol > 0:
		string = string + "   "
		kol = kol - 1
	kiri = 1
	while kiri < (i - (bar-1)):
		string = string + " " + str(no) + " "
		kiri = kiri + 1		
	kanan = 1
	while kanan < kiri -1:
		string = string + " " + str(no) + " "
		kanan = kanan + 1	

	string = string + "\n\n"
	bar = bar - 1
	no = no + 1
print (string)
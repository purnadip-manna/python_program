import os, time
ip = input("Enter the name: ")
sign = ['/','-','\\','|']
load = list(map(str,ip.lower()))
a = ""
k = 0
l = len(load)
for i in range(50):
	for j in range(l):
		os.system("cls")
		load[j] = load[j].upper()
		a = "".join(map(str,load))
		print(a, end="")
		print(sign[k])
		k+=1
		if k==4:
			k=0
		load[j] = load[j].lower()
		time.sleep(0.2)

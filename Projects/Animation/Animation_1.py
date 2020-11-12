import os, time
ip = input("Enter your name: ")
load = list(map(str,ip.lower()))
a = ""
l = len(load)
for i in range(50):
	for j in range(l):
		os.system("cls")
		load[j] = load[j].upper()
		a = "".join(map(str,load))
		print(a)
		load[j] = load[j].lower()
		time.sleep(0.4)

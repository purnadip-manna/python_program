import os, time
ip = "--------purnadip-------"
load = list(map(str,ip.lower()))
a = ""
l = len(load)
for i in range(50):
	for j in range(l):
		os.system("cls")
		if load[j] == '-':
			load[j] = '*'
		else:
			load[j] = load[j].upper()
		a = "".join(map(str,load))
		print(a)
		if load[j] == '*':
			load[j] = '-'
		else:
			load[j] = load[j].lower()
		time.sleep(0.4)

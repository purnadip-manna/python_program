import os, time
ip = "||                     ||"
load = list(map(str,ip.lower()))
a = ""
l = len(load)
for i in range(1):
    start = 1
    sec = 0
    for j in range(l):
        end = start+3
        os.system("cls")
        k = 2
        while sec == 0 and k<6:
            load[k] = "* "
            a = "".join(map(str,load))
            print(a)
            time.sleep(0.4)
            os.system("cls")
            k+=1
            if k==6:
                sec = 1
        temp = start
        while start<=end and load[j]!='|' and sec == 1:
            load[j]="* "
            j+=1
            start+=1
        a = "".join(map(str,load))
        print(a)
        start = temp+1
        if sec == 1:
            ip = "||                     ||"
            load = list(map(str,ip.lower()))
        time.sleep(0.4)

import os, time

def ent(end, load):
    if end == 10:
        return load
    else:
        i = 1
        while(i<end):
            os.system("cls")
            load[i] = "o"
            a = "".join(map(str,load))
            print(a)
            temp = i
            i+=1
            if i==end:
                return ent((end-1), load)
            load[temp] = " "
            time.sleep(0.02)
    
ip = "[                     ]"
a = ""
load = list(ip.lower())
l = len(load)
for t in range(2):
    i = 1
    while(i<15):
        os.system("cls")
        load[i] = "o"
        a = "".join(map(str,load))
        print(a)
        temp = i
        i+=1
        if i==15:
            load = ent(14, load)
        load[temp] = " "
        time.sleep(0.03)
    end = 14
    while end>=10:
        i = end
        while i<l and load[i]!="]":
            os.system("cls")
            load[i] = "o"
            a = "".join(map(str,load))
            print(a)
            load[i] = " "
            i+=1
            time.sleep(0.03)
        os.system("cls")
        load[i-1] = " "
        a = "".join(map(str,load))
        print(a)
        end-=1
input()
        

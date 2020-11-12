def var(s, t, name):
    ck = input("Do you want assign value to "+name+"?(y/n)")
    if ck == 'y':
        value = input()
        edit = s+t+" "+name+" = "+value+";\n\t"
    else:
        edit = s+t+" "+name+";\n\t"
    return edit

def printf(s, content):
    ck = input("Do you want to print value of any variable?(y/n)")
    if ck == 'y':
        v = input("Name of variable: ")
        t = input("Datatype: ")
        if t == 'int':
            fs = "%d"
        elif t == 'float':
            fs = "%f"
        else:
            fs = "%c"
        edit = s+"printf(\""+content+fs+"\", "+v+");\n\t"
    else:
        edit = s+"printf(\""+content+"\");\n\t"
    return edit

def scanf(s, t, v):
    if t == 'int':
        fs = "%d"
    elif t == 'float':
        fs = "%f"
    else:
        fs = "%c"
    edit = s+"scanf(\""+fs+"\", &"+v+");\n\t"
    return edit

    
name = input("Enter the file name: ")
name = name+".c"
fl = open(name, "w")
s = "#include<stdio.h>\n\nint main(void)\n{\n\t"
print("Press 1 to add variables\nPress 2 to add printf()\nPress 3 to add scanf()\nPress 0 to exit:")
op = -1
while op:
    op = int(input("Enter choice: "))
    if op == 0:
        break
    elif op == 1:
        t = input("Datatype: ")
        name = input("Name of the variable: ")
        s = var(s, t, name)
    elif op == 2:
        con = input("Enter the content of printf(): ")
        s = printf(s, con)
    elif op == 3:
        t = input("Datatype of variable: ")
        v = input("Enter the name of variable: ")
        s = scanf(s, t, v)
    else:
        print("Wrong input")

s = s+"\n\treturn 0;\n}"
fl.write(s)
print("File created!")
print("File content:\n---------------------------\n"+s)
fl.close()
input("\n---------------------------\nPress enter to exit")

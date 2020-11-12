# Updating python code with html for WIX

fileLines = ""
fn = input("Enter python file name to read: ")
fd = input("Enter file to write: ")
space = ""

filename = r"C:\Users\Purnadip\Desktop\\" + fn
filedump = r"C:\Users\Purnadip\Desktop\\" + fd

pyfile = open(filename, 'r')
s = pyfile.read()
new = ""
for x in s:
    if x == " ":
        x = "&nbsp;"
    elif x == "\t":
        x = "&nbsp;&nbsp;&nbsp;&nbsp;"
    elif x == "\n":
        x = "<br>"
    new += x

pyfile.close()
wt = open(filedump, 'w')
wt.write(new)
wt.close()

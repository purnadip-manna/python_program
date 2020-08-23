fileLines = ""
fn = input("Enter python file name to read: ")
fd = input("Enter file to write: ")
space = ""

filename = r"file_location" + fn  # file_location -> of the main or source file
filedump = r"file_location" + fd  # file_location -> of the new or destination file

pyfile = open(filename, 'r')
s = pyfile.read()
new = "<code>"
for x in s:
    if x == " ":
        x = "&nbsp;"
    elif x == "\n":
        x = "</code><br><code>"
    new += x

pyfile.close()
new+="</code>"
wt = open(filedump, 'w')
wt.write(new)
wt.close()

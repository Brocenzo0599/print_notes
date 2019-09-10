import os, sys
import win32print, win32api
import datetime as dt
win32print.SetDefaultPrinter(win32print.GetDefaultPrinter())

#Gets list of already printed documents from printed.txt
printed_docs = []
f= open("printed.txt", "a")
f1 = open ("printed.txt", "r")
print ("already printed documents: ")
for line in f1.readlines():
    if line.startswith("C"):
        print (line)
        printed_docs.append(line.replace("\n", ""))
f1.close()


#Gets date and adds path according to semester and year (FORMAT :  "\SEMESTER YEAR")
def findpath():
    path = "C:\\Users\\vince\\Google Drive\\Mcgill"
    print(path.endswith("Mcgill"))
    date = dt.date.today()
    if date.month > 6 and path.endswith("Mcgill"):
        path += "\\Fall " + str(date.year)
    elif date.month <=6:
        path += "\\Winter " + str(date.year)
    return path


for dir in os.listdir(findpath()):
    path = findpath()
    print ("dir",dir)
    path += "\\%s" %dir + "\\notes"
    for file in os.listdir(path):
        file_path = path + "\\%s" %file
        if file.endswith(".pdf") and file_path not in printed_docs:
            print (file_path)
            printed_docs.append(file_path)
            f.write("\n"+ file_path)
            win32api.ShellExecute(0, "print",file_path, None, ".", 0)

f.close()
x = input()

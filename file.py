#Open a already made file
file=open('s.txt','r')
for i in file:
    print(i)
print("")

#Python code to create a file
f=input("Enter file name with extension: ")
print("1 for create")
print("2 for read")
c=input("File Operation")
if c=="1":
    fc=open(f,"w")
    content=input("write you text here: ")
    fc.write(content)
    fc.close()
    print("File created successfully...")
elif c=="2":
    fr=open(f,"r")
    for i in fr:
        print(i)
else:
    print("Not Done")
print("")

#Remove file
import os
os.remove("shivam.txt")
print("removed Successfully..")
print("")

#Rename a file
import os
os.rename("s.txt","shivam.txt")
print("File renamed..")


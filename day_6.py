# file i/o
# f = open("file6.txt", "r")
# print(f.read())
# f.close()
# #  or 
# with open("file6.txt", "r") as f:
#     print(f.read())

# writing

# with open("Filee6.txt","w") as c:
#     c.write("Hello this file is created using program")
#     c.close()
# with open("File6.txt",  "r") as b:
#     print(b.read())
    
# readline

# with open("Filee6.txt","r") as f:
#     # lines=f.readlines()
#     # print(lines,type(lines))
#     line1=f.readline()
#     print(line1)
#     line2=f.readline()
#     print(line2)
#     line3=f.readline()
#     print(line3)
    
# append to the txt file 

with open("Filee6.txt","a") as f:
    f.write("Hello")

    
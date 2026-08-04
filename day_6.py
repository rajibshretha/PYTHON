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

# with open("Filee6.txt","a") as f:
#     f.write("Hello")


# # p1
# with open("Filee6.txt","r") as f:
#     a=f.read();
#     print(a)
#     if ("this" in a):
#         print("yes it contain")
#     else:
#         print("no")
   
# # p2

import random
def game():
    print("youre playing the game...")
    score=random.randint(1,99)
    
    with open("file6.txt","r") as f:
        
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0
    if(score>hiscore):
        with open("file6.txt" , "w") as s:
            s.write(str(score))
            print("new highscore")
    return score
            
print(game())
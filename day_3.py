# Dictionary
 
# emptrydic={}
# print(type(emptrydic))

# marks={
#     "rajib":34,
#     "raj":32,
# }
# print(marks,type(marks))
# print(marks["rajib"]);
# print(marks.items())
# print(marks.keys())
# print(marks.values())

# marks.update({"raj":12,"raju":42})#if already exist then update else will create new
# print(marks)

# print(marks.get("raj"))

# print(marks["rajesh"])#gives error
# print(marks.get("rajesh"))#gives value none

# Set

# emptryset=set()
# print(type(emptryset))

# num={1,2,3,23,2,2,2,2,}
# print(num)

# s1={1,2,3}
# s2={4,5,6,3}
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1-s2)

# p1

# lang={
#     "bhai":"brother",
#     "behen":"sister"
# }
# word=input("enter the word you want meaning of : ")
# print(lang[word])

# # p2

# num=set()
# n=(input("Enter a number:"))
# num.add(int(n))
# n=(input("Enter a number:"))
# num.add(int(n))
# n=(input("Enter a number:"))
# num.add(int(n))
# print(num)

# # p3
# nw=set()
# nw.add(23)
# nw.add("23")
# print(nw)

# p4

fav={}
name=input("eneter friends name : ")
lang=input("enter lanugage name ")
fav.update({name: lang})
name=input("eneter friends name : ")
lang=input("enter lanugage name ")
fav.update({name: lang})
print(fav)
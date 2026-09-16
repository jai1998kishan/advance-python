myList = ["banana", "cherry", "apple"]
print(myList)
print(myList[-2])

myList2 = list()
print(myList2)

for item in myList:
    print(item)

if "banana" in myList:
    print("yes")
else:
    print("no")


print(len(myList))

myList.append("lemon")
print(myList)

myList.insert(1, "blueberry")  # 1 is index

items = myList.pop()
print(items)
print(myList)

myList.remove("cherry")
print(myList)

# item = myList.remove("cherry1") # this will show error because of typo error in cherry1
# print(item)

# myList.clear()
# print(myList)

# myList.reverse()
# print(myList)

myList3 = [1, -2, 3, 2, 9, 5, 0, -9]
# myList3.sort() # this change the orignal list
# print(myList3)

new_list = sorted(myList3)
print(myList3)
print(new_list)


myList4 = [0]*5
print(myList4)

myList5 = [1, 2, 3, 4, 5]
new_list1 = myList4 + myList5
print(new_list1)

myList6 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = myList6[1:5]
print(a)

a = myList6[2:]
print(a)

a = myList6[1::2]  # 1 is index and 2 is step
print(a)

a = myList6[::-1]
print(a)

list_org = ["banana", "cherry", "apply"]

list_cpy = list_org

print(list_org)
print(list_cpy)

list_cpy.append("lemon")
print(list_org)
print(list_cpy)
# both the geting change


list_copy = list_org.copy()
print(list_copy)
list_copy.append("mongo")
print(list_copy)

list_copy = list(list_org)
print(list_copy)

list_copy = list_org[:]
print(list_copy)


myList7 = [1, 2, 3, 4, 5, 6]
b = [i*i for i in myList7]
print(b)

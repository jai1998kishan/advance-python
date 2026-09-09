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

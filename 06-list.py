# list is a !primitive data type in python
# sometimes list is called array in other programming languages

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("mylist: ", myList)

# append new item to list
myList.append(11)
print("appended mylist: ", myList)

# inserting new item in beginning or middle of list
myList.insert(0, -1)
print("inserting into beginning of mylist: ", myList)
myList.insert(3, "ok")
print("inserting into middle of mylist: ", myList)

# removing item from list
myList.remove(2)
print("removing 2 int myList: ", myList)

# check how many item in list
print("member in myList: ", len(myList))

# print all of the items in myList 1 by 1 with loop
for i in range(1, len(myList)):
    print("item number-" + str(i), ":", myList[i])
# or like this
for item in myList:
    print(item)

# removing all item in list
myList.clear()
print("removing all item in myList: ", myList)

print("\n\n")

# range() function
# range(initiate, endNumber, [options:range_per_item])
x = range(0, 10, 2)
for i in x:
    print(i)
# or like this
print("\n")
for j in range(5):
    print(j)

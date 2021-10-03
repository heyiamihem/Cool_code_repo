# Lists: ordered,diff datatypes, mutable, allows duplicate elements

myList = ["banana", "cherry", "apple",]
print(myList)

# Creating an empty list with list function

mylist2 = list()
print(mylist2)

# List allows different data types
myList3 = [5, True, "Apple"]
print(myList3)

# List allos duplicate elements

myList4 = [5, True, "Apple", "Apple"]
print(myList4)


# Accessing List's Item or element
item = myList4[1:4]
print(item)

# Iterate over list
for elements in myList4: # here elements can be i or x or any variable
    print(elements) 

# Check if an item or element is in your list
if "Apple" in myList4:
    print("Yes Present")
else:
    print("Not Present")


# Number of elements in your list
lenght = len(myList4)
print(lenght)

# Append Item or Add Item in the end of the list
myList4.append("Orange")
print(myList4)


# Add or insert an item in specific location 
myList4.insert(2, "BlueBerry")
print(myList4)

# Remove Items from the list
myList4.pop(3) # 1- Here myList4.remove(3) could also be used
print(myList4) # 2- We can remove all the elements with .clear()

# Reverse the list
myList4.reverse()
print(myList4)

# Sort the List
numList = [4,3,6,2,4,5,1]
print(numList)
numList.sort()
print(numList)


# New Sorted List
numList1 = [3,5,7,2,7,9,2,10,-2,-10]
newSortedList = sorted(numList1)
print(numList1)
print(newSortedList)

# New List with an element as multiple time
multiList = [1] * 6
print(multiList)

# Concurrent or add two list
list1 = [2]*5
list2 = [4,5,6,7,8]
con_list  = list2 + list1
print(con_list)

# Slicing in List
list01 = [1,2,3,4,5,6,7,8,9]
a = list01[2:8:3] # list01[Start_index:End_index:Step_index]
print(a)

# Copying in List
list_org = ["banana", "cherry", "apple"]
list_cpy = list_org.copy()
print(list_cpy)

# Modify a list
original_list = [1,2,3,4,5]
modified_list = [ele * ele for ele in original_list]
print(original_list)
print(modified_list)
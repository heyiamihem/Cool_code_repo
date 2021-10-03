# Tuples: Ordered, Immutable[Cannot be Changed], Allows Duplicate Elements
mytuple1 = ("Max", 28, "Boston") # Parenthesis
print(mytuple1)
mytuple2 = "Max", 28, "Boston" # Without Parenthesis
print(mytuple2)

# Tuple from list
mytuple3 = tuple(["Apple", "Orange",9,True])
print(mytuple3)
print(type(mytuple3))

# Access elements of tuple
item = mytuple3[1]
print(item)

# WE CANNOT INSERT OR CHANGE ELEMENTS IN TUPLE SINCE IT IS IMMUTABLE
# mytuple3[0]= "Tim"
# print(mytuple3)
#Error:
# File "c:\Users\Mahi\Documents\Intermediate Python\02_tuples.py", line 17, in <module>
#     mytuple3[0]= "Tim"
# TypeError: 'tuple' object does not support item assignment

# Iterate tuple
for i in mytuple3:
    print(i)

# Check element in tuple
if "Orange" in  mytuple3:
    print("Yess!")
else: 
    print("No")


# Number, counts and index of elements in tuple
my_tuple = ("a", "p", "p", "l", "e")
print(len(my_tuple))
print(my_tuple.count('o'))
print(my_tuple.index("e"))

# From tuple to a list
my_list = list(my_tuple)
print(my_list)
print(type(my_list))


# Slicing in Tuple
a= (1,2,3,4,5,6,7,8,9,10)
b= a[3:8:2] # Here a[Start_index,End_index,Step_index]
print(b)


# Unpacking in tuple
my_tuple2 = ("Max", 28, True)
name, age, male = my_tuple2
print(name)
print(age)
print(male)

# Pick multiple elements in tuple
my_tuple = (1,2,3,4,5,6,7,8,9)
i1, *i2, i3, i4 = my_tuple
print(i1)
print(*i2)
print(i4)
print(i3)

# Working with tuple is more efficient as it takes less memory storage
import sys
my_list = [0,1,2,"hello",True,3,4,5,6,7,8,9] # 152 bytes
my_tuple = (0,1,2,"hello",True,3,4,5,6,7,8,9) # 136 bytes
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

# Time efficiency in making list and tuple
import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=10000000)) # List
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=10000000)) # Tuple
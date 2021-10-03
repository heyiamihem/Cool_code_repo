# Dictionary: It consisi of Key-Value pairs, Unordered, Mutable

# It is created with braces
mydict = {"NAME": "Max", "AGE": 28, "MALE": True, "CITY": "New York"}
print(mydict)

# Alternate way
mydict2 = dict(name= "Mary", age = 27, city= "Boston", female= True)
print(mydict2)

# Access values
value = mydict2["age"]
print(value)

# Insert Key-Value pair in dictionary mydict
mydict["EMAIL"] = "max21@gmail.com"
print(mydict)

# Delete item in dictionary mydict
del mydict["AGE"] # OR mydict.pop("AGE")
print(mydict)


# Check key in dictionary
if "NAME" in mydict:
    print(mydict["NAME"])
      # OR
try:
    print(mydict["AGE"])
except:
    print("Error")

# For key in loop in dictionary
for key in mydict.keys():
    print(key)

#For values of keys
for key, x in mydict.items():
    print(key, x)


# Copy dictionary
mydict_cpy = mydict.copy()
print(mydict_cpy)

# Merge dictionaries
mydict.update(mydict2)
print(mydict)


# Tuple in dictionaries
mytuple = (8,7)
mydict = {mytuple: 15}
print(mydict)
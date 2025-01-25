#Booleans

print(10 > 9)
print(10 == 9)
print(10 < 9)

#Operators

print((6 + 3) - (6 + 3))

#Lists

    #Lists
    
    thislist = ["apple", "banana", "cherry"]
    print(thislist)
    
    #Access List Items
    
    thislist = ["apple", "banana", "cherry"]
    print(thislist[1])

    #Change List Items

    thislist = ["apple", "banana", "cherry"]
    thislist[1] = "blackcurrant"
    print(thislist)

    #Add List Items

    thislist = ["apple", "banana", "cherry"]
    thislist.append("orange")
    print(thislist)

    #Remove List Items

    thislist = ["apple", "banana", "cherry"]
    thislist.remove("banana")
    print(thislist)

    #Loop Lists

    thislist = ["apple", "banana", "cherry"]
    for x in thislist:
        print(x)

    #List Comprehension

    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    newlist = []

    for x in fruits:
        if "a" in x:
            newlist.append(x)

    print(newlist)

    #Sort Lists

    thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
    thislist.sort()
    print(thislist)

    #Copy Lists

    thislist = ["apple", "banana", "cherry"]
    mylist = thislist.copy()
    print(mylist)

    #Join Lists

    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]

    list3 = list1 + list2
    print(list3)

#Tuples
    #Tuples

    thistuple = ("apple", "banana", "cherry")
    print(thistuple)

    #Access Tuple Items

    thistuple = ("apple", "banana", "cherry")
    print(thistuple[1])

    #Update Tuples

    x = ("apple", "banana", "cherry")
    y = list(x)
    y[1] = "kiwi"
    x = tuple(y)

    print(x)

    #Unpack Tuples

    fruits = ("apple", "banana", "cherry")

    (green, yellow, red) = fruits

    print(green)
    print(yellow)
    print(red)

    #Loop Tuples

    thistuple = ("apple", "banana", "cherry")
    for x in thistuple:
        print(x)

    #Join Tuples

    tuple1 = ("a", "b" , "c")
    tuple2 = (1, 2, 3)

    tuple3 = tuple1 + tuple2
    print(tuple3)

#Sets

    #Sets

    myset = {"apple", "banana", "cherry"}

    #Access Set Items

    thisset = {"apple", "banana", "cherry"}

    for x in thisset:
        print(x)

    #Add Set Items

    thisset = {"apple", "banana", "cherry"}

    thisset.add("orange")

    print(thisset)

    #Remove Set Items

    thisset = {"apple", "banana", "cherry"}

    thisset.remove("banana")

    print(thisset)

    #Loop Sets

    thisset = {"apple", "banana", "cherry"}

    for x in thisset:
    print(x)

    #Join Sets

    set1 = {"a", "b", "c"}
    set2 = {1, 2, 3}

    set3 = set1.union(set2)
    print(set3)

#Dictionaries

    #Dictionaries

    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    
    #Access Dictionary Items

    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    x = thisdict["model"]

    #Change Dictionary Items

    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    thisdict["year"] = 2018

    #Add Dictionary Items

    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    thisdict["color"] = "red"
    print(thisdict)

    #Remove Dictionary Items

    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    thisdict.pop("model")
    print(thisdict)

    #Loop Dictionaries

    for x in thisdict:
        print(x)

    #Copy Dictionaries

    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    mydict = thisdict.copy()
    print(mydict)

    #Nested Dictionaries

    myfamily = {
        "child1" : {
            "name" : "Emil",
            "year" : 2004
        },
        "child2" : {
            "name" : "Tobias",
            "year" : 2007
        },
        "child3" : {
            "name" : "Linus",
            "year" : 2011
        }
    }

#If ... Else

a = 33
b = 200
if b > a:
  print("b is greater than a")

#While Loops

i = 1
while i < 6:
  print(i)
  i += 1

#For Loops

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
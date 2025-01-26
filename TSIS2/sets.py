myset = {"apple", "banana", "cherry"}

#
thisset = {"apple", "banana", "cherry"}
print(thisset)

#access
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


#
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset) #true


#adding
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)


#
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#remove

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)


#
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

#
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)


#loop sets
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#join
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


#
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)


#
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)
#
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)

3
#with tuple
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

#
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

#
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)
#The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.

#
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

thislist = ["apple", "banana", "cherry"]
print(thislist)

#
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#access

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#change item value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#append items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#remove list items
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


# the first occurence of "banana"
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#
thislist = ["apple", "banana", "cherry"]
del thislist

#
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


#loop lists
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)



#
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


#list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


#
newlist = [x for x in fruits if x != "apple"]

#
newlist = [x for x in fruits]

#
newlist = [x for x in range(10) if x < 5]


#sort lists

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


#
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#reverse
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)




#copy lists
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)



#join lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

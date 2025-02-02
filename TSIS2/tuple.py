mytuple = ("apple", "banana", "cherry")

#
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#tuple allows to dublicate values

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))


#
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#access tuples
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])


#update tuples
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists



#unpack tuples
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Assign the rest of the values as a list called "red"
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


#loop tuples
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])


#
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1


#joining
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)



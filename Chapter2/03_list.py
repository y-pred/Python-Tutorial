fruits = ["Apple","Banana","Cherry",56, 43.22, True]

print(fruits) #prints the list
print(fruits[3]) #prints 2nd item in the list
print(fruits[-1]) #prints last item in the list

fruits.append("mango") #adds mango to the list

print(fruits)

l1=[3,2,5,7,1]

l1.sort()
print(l1)

l1.reverse()
print(l1)

l1.insert(2,4) #inserts 4 at index 2
print(l1)

l1.remove(4) #removes 4 from the list
print(l1)

value =l1.pop() #removes last item from the lsit and returns it
print(l1)
print(value)

print(type(l1))

print(len(l1))

fruits[4]="kiwi"
print(fruits)

print(sum(l1)) #prints sum of all items in the list
print(max(l1)) #prints max of all items in the list
colors = ("red","green","blue",1234,3345,True)
print(colors)
print(type(colors))

print(colors[0])
print(colors[0:3])

print(colors.count("blue")) #counts the number of times blue appears in the tuple
print(colors.index("red")) #prints the index of blue in the tuple

print(len(colors)) #prints the length of the tuple

print(colors.append("yelloew")) # it will show error because tuples are immutable

colors[2] = "yellow" # it will show error because tuples are immutable
print(colors)


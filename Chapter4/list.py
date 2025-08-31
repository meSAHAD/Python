array = ["sahad", 5, 10.56, "rahim", "kabir", 5+6j]

print(array)
print(type(array))
print(array[0])

array[0] = "changed"
print(array)
print(array[0])

print(array[1:4])
print(array[::2]) # it will take one element and skip one element
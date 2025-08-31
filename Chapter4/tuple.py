a=() #empty tuple
print(type(a))
b=(1,) #tuple with single element, we have to put comma after the element
print(type(b))
print(b)
c=(1,2,3,4,5) #tuple with multiple elements
print(type(c))
print(c)
print(c[0]) #accessing first element of tuple
print(c[1:4]) #slicing of tuple
print(c[::2]) # it will take one element and skip one element
#c[0]=100 # it will give error, because tuple is immutable, we can not change the value of tuple
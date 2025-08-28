# converting string to float
a="32.5"
b=float(a)
print(type(b))
print(b)
# converting float to integer
c=int(b)
print(type(c))
print(c)
# converting integer to string
d=str(b)
print(type(d))
print(d)
# converting integer to complex number
e=complex(c)
print(type(e))
print(e)
# Note: When converting from float to integer, the decimal part is truncated (not rounded).
# Also, converting a string to a number will raise an error if the string does not represent a valid number.    

# Python provides built-in functions to convert between different data types.
# These functions include int(), float(), str(), and complex().
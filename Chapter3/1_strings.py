a ='sahad'
b="sahad"
c='''sahad'''
d="""sahad"""

print(a)
print(d)

nameshort= b[0:3 ] # slicing from 0 to 3 but not including 3
print(nameshort)
print(b[0])  # indexing
print(b[-1]) # negative indexing
print(b[0:]) # slicing from 0 to end
print(b[:3]) # slicing from start to 3
print(b[::2]) # slicing with step size 2    

print(b[::-1]) # reversing a string using slicing

print(len(b)) # length of string
print(b.lower()) # convert string to lowercase
print(b.upper()) # convert string to uppercase
print(b.replace('h','H')) # replace a character in string
print(b.split('a')) # split a string into a list
print(b.find('h')) # find the index of a character in string
print(b.isalnum()) # check if string is alphanumeric
print(b.isalpha()) # check if string is alphabetic
print(b.count('a')) # count the number of occurrences of a character in string
print(b.startswith('s')) # check if string starts with a character
print(b.endswith('d')) # check if string ends with a character
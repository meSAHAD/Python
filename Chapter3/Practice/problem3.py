# 3. Write a program to detect double space in a string. 
string= input("Enter a string: ")
if "  " in string:
    print("double space is present")
else:
    print("double space is not present")  

 #alternate method
print (string.find("  ")) # it will give index of first double space, if not present it will give -1
word="abcdefghijklmnopqrstuvwxyz"

print(word[1:10:2]) # here 2 is skip value, it will skip one letter after taking one letter
print(word[::3]) # it will take one letter and skip two letters
print(word[::4]) # it will take one letter and skip three letters
print(word[::]) # it will take all letters
print(word[::1]) # it will take all letters, here 1 is skip value
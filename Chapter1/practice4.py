# Write a python program to print the contents of a directory using the os module. 
# Search online for the function which does that.

import os

if __name__ == "__main__":
    directory = "F:\Documents"
    for entry in os.listdir(directory):
            print(entry)

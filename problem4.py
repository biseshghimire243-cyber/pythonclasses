# write a pythin program to print the context of a directory using os moduel
import os

path = input("Enter directory path: ")

if os.path.exists(path):
    contents = os.listdir(path)

    print("Contents of the directory:")
    for item in contents:
        print(item)
else:
    print("Directory does not exist.") 
import os

path = "sample.txt"

if os.path.exists(path):
    if os.path.isfile(path):
        print(f"{path} is a file.")
    elif os.path.isdir(path):
        print(f"{path} is a directory.")
else:
    print(f"{path} does not exist.")

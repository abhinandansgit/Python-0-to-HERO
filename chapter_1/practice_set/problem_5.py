# Label the program written in problem 4 with comments. 

import os
#os module provides the system file access to the interpreter
def print_directory_contents(directory_path):

#   Prints the contents of a given directory.
#   Args:
#     directory_path: The path to the directory.
# use os module to view the directory contents

  for item in os.listdir(directory_path):
    item_path = os.path.join(directory_path, item)
    if os.path.isdir(item_path):
      print(f"{item_path}/")
      print_directory_contents(item_path)
    else:
      print(item_path)
#take input of path from user
directory_path = input("Enter the directory path: ")
print_directory_contents(directory_path)

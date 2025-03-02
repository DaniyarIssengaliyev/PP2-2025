import os
p=(r"C:\\Users\\Daniyar\\Desktop\\PP2 2025\\lab6\\dir-and-files\\delete.txt")
if os.path.exists(p):
    os.remove(p)
else:
    print("this file does not exist")
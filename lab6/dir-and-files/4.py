import os

f = open(r'C:\\Users\\Daniyar\\Desktop\\PP2 2025\\lab6\\dir-and-files\\4.txt')
cnt = 0
for lines in f:
    cnt += 1
print(f"file has {cnt} lines")
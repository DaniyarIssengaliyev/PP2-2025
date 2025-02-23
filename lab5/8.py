import re

str=input().strip()

words = re.split(r'(?=[A-Z])', str)
if words[0] == "":
    words.pop(0)
print(words)
import re

def find_seq(str):
    pattern = r"\b[a-z]+_[a-z]+\b"
    matches = re.findall(pattern,str)
    return matches 

str = str(input())
print(find_seq(str))
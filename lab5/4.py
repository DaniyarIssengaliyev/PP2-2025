import re

def find_seq(str):
    pattern = r"[A-Z][a-z]+"
    matches = re.findall(pattern, str)
    return matches

str = str(input())

print(find_seq(str))
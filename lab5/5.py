import re

def match_string(str):
    pattern = r"a.*b$"
    matches = re.findall(pattern,str)
    return matches 

str = str(input())

print(match_string(str))
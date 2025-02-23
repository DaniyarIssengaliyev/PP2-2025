import re
def convert(match):
    return match.group(1).upper()
def sn_to_ca(str):
    return re.sub(r'_([a-zA-Z])', convert, str)
str = str(input())

print(sn_to_ca(str))
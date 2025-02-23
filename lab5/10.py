import re

def sn_to_ca(str):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', str).lower()
str = str(input())

print(sn_to_ca(str))
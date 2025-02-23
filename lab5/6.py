import re
def repl(str):
    pattern = r'[ ,.]'
    text = re.sub(pattern,':', str)
    return text

str = str(input())

print(repl(str))
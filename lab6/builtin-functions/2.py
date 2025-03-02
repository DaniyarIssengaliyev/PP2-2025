text = str(input())

low = 0
up = 0
for char in text:
    if(char.islower()):
        low += 1
    elif(char.isupper()):
        up += 1

print(low,up)
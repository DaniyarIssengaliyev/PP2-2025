def temp():
    f = int(input("What is the temperature in fahrenheits: "))
    c = (5/9) * (f - 32) 
    return c

print(temp())
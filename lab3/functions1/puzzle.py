'''
35 heads and 94 legs 
x = chicken - 1 head, 2 legs
y = rabbit - 1 head, 4 legs
then,
{x + y = 35 ==> x = 35 - y
{2x + 4y = 94 /2 ==> 35 - y + 2y = 47 ==> 35 = 47 - y

y = 12 and x = 23

'''

heads = int(input("How many heads?: "))
legs = int(input("How many legs?: "))

def solve(numheads, numlegs):
    rabbits = (numlegs / 2) - numheads
    chicken = numheads - rabbits
    print("chickens: ", int(chicken))
    print("rabbits: ", int(rabbits))
solve(heads, legs)
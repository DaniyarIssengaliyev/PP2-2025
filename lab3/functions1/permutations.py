from itertools import permutations

def print_permutations(s):
    for perms in permutations(s):
        print("".join(perms))

user_input = input("Enter a string: ")
print_permutations(user_input)
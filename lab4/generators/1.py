num = int(input())
generated = (i**2 for i in range(num))
for i in range(num):
    print(next(generated))
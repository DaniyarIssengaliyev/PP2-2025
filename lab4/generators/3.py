def nums(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input())
num = [i for i in nums(n)]

print(num)
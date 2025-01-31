def histogram(nums):
    for i in nums:
        for j in range(1, i+1):
            print("*", end="")
        print()
nums = list(map(int,input("Enter numbers separated by spaces: ").split()))

histogram(nums)
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

input_numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
prime_numbers = filter_prime(input_numbers)
print("Prime numbers: ", prime_numbers)
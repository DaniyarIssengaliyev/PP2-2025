def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

class List:
    def __init__(self,a):
        self.a = a
    def filtering(self):
        return list(filter(lambda num : is_prime(num), self.a))
    
myList = List([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(myList.filtering())
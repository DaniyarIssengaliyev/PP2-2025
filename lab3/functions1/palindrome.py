def isPalindrome(word):
    reversed_word = word[::-1]
    if(reversed_word == word):
        print("is palindrom")
    else:
        print("not palindrom")
my_string = input("Enter a string: ")
isPalindrome(my_string)
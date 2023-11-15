def isPalindrome(str):
    return f"{str} is a palindrome." if str==str[::-1] else f"{str} is not a palindrome."

st = input("Enter to check the palindrome : ")
print(isPalindrome(st))
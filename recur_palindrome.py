n = int(input('Please give a number: '))

def reverse(num):
    if num<10:
      return num 
    else:
      return int(str(num % 10) + str(reverse(num // 10)))

def isPalindrome(num):
    if num == reverse(num):
        return 1
    return 0
if isPalindrome(n) == 1:
    print("Given number is a Palindrome")
else:
    print("Given number is a not Palindrome") 

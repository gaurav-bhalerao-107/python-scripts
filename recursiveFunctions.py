# Bunch of Mini Recursive functions done using Python


# Sum of a list recursively

numbers = [1,2,3,4,5,7,8,9,9,5]

def sumRecursive(numbers):
    if len(numbers) == 1:
        return numbers[0]
    if len(numbers) == 2:
        return numbers[0] + numbers[1]
    
    return sumRecursive([numbers[0] + numbers[1]] + numbers[2:])

sumRecursive(numbers)



#Palindrome string recursion function

pal_string = input("Enter a string to see if a palindrome")

def palindromeRecursive(s):

    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    
    return palindromeRecursive(s[1:-1])

if palindromeRecursive(pal_string):
    print("True")
else:
    print("False")

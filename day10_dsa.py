'''
#Sum of digits
def sum_of_digits(n):
    if n == 0:
        return 0
    
    return n % 10 + sum_of_digits(n//10)

print(sum_of_digits(1234))


#Power Function
def power(a,b):
    if b == 0:
        return 1
    
    return a * power(a, b-1)

print(power(2,4))


#Count digits
def count_digits(n):
    if n == 0:
        return 0
    
    return 1 + count_digits(n//10)

print(count_digits(12345))


#Reverse number recursively
def reverse_num(n, rev = 0):
    if n == 0:
        return rev
    
    digit = n % 10
    rev = rev * 10 + digit

    return reverse_num(n//10, rev)

print(reverse_num(1234))


#Product of digits
def product_digits(n):
    if n == 0:
        return 1
    
    return n % 10 * product_digits(n//10)
print(product_digits(1234))
'''

#Palindrome Number
def check_palindrome(n, rev = 0):
    if n == 0:
        return rev
    digit = n % 10
    rev = rev * 10 + digit

    return check_palindrome(n//10, rev)

def palindrome(n):
    reversed_num = check_palindrome(n)
    return n == reversed_num

print(palindrome(121))

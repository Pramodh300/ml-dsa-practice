#Factorial using recursion
def fact(n):
    if n == 1:
        return 1
    
    return n * fact(n-1)

print(fact(5))



#Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))




#Sum of first n numbers
def num(n):
    if n == 1:
        return 1
    return (n) + num(n-1)
print(num(5))




#Reverse string using recursion
def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]
print(reverse_string("hello"))




#Print numbers from n to 1
def num(n):
    if n == 0:
        return
       
    print(n)
    num(n-1)
num(5)


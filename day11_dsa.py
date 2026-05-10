#Sum of digits
def sum(num):
    if num == 0:
        return 0
    
    return num%10 + sum(num//10)

print(sum(12345))


#Count digits
def count_digits(num):
    if num == 0:
        return 0
    
    return 1 + count_digits(num//10)

print(count_digits(9876))


#Power function
def power(a,b):
    if b == 0:
        return 1
    
    return a * power(a, b-1)

print(power(2,5))


#Reverse Number
def reverse(num, rev = 0):
    if num == 0:
        return rev
    
    digit = num % 10
    rev = 10 * rev + digit
    return reverse(num//10, rev)

print(reverse(1234))


#Palindrome Number
def check_palindrome(num, rev=0):
    if num == 0:
        return rev
    
    digit = num % 10
    rev = 10 * rev + digit
    return check_palindrome(num//10, rev)

def palindrome(num):
    reverse_number = check_palindrome(num)
    return num == reverse_number

print(palindrome(121))


#Product of digits
def product(num):
    if num == 0:
        return 1
    
    return num%10 * product(num//10)

print(product(123))


#Tower of hanoi
def hanoi(n, source, helper, destination):
    if n == 1:
        print(f"Move disk from 1 to {source} to {destination}")
        return
    
    hanoi(n-1, source, destination, helper)
    print(f"Move disk {n} from {source} to {destination}")

    hanoi(n-1, helper, source, destination)
hanoi(2,"A","B","C")


#Count Hanoi moves
def hanoi_moves(n):
    if n == 1:
        return 1
    
    return 2 * hanoi_moves(n-1) + 1

print(hanoi_moves(3))


#Flood fill
image = [
    [1,1,1],
    [1,1,0],
    [1,1,1]
]
rows = len(image)
columns = len(image[0])

def flood_fill(r, c, old, new):
    if r < 0 or r >= rows or c < 0 or c >= columns:
         return
        
    if image[r][c] != old:
        return
    
    image[r][c] = new

    flood_fill(r+1, c, old, new)
    flood_fill(r-1, c, old, new)
    flood_fill(r, c+1, old, new)
    flood_fill(r, c-1, old, new)

flood_fill(1,1,1,2)
for row in image:
    print(row)
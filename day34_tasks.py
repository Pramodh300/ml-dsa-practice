import math
'''#Vector addition
a = [1,2]
b = [3,4]

result = []
for i in range(len(a)):
    result.append(a[i] + b[i])

print(result)


#Scalar Multiplication
v = [2,3]
k = 4

result = []
for i in range(len(v)):
    result.append(v[i] * k)

print(result)


#Vector magnitude
v = [3,4]
a = []
for i in range(len(v)):
    a.append(v[i] * v[i])
sum_of_list = sum(a)
result = math.sqrt(sum_of_list)
print(result)


#Dot Product
a = [1,2]
b = [3,4]
a1 = 0
b1 = 0
for i in range(len(a)):
    if i == 0:
        a1 = a[i] * b[i]
    break
for n in range(len(b)):
    if n == 0:
        continue
    b1 = a[n] * b[n]

result = a1 + b1
print(result)
'''

#Find largest vector element
v = [4,9,2,7]
max_element = v[0]
for i in range(len(v)):
    if v[i] > max_element:
        max_element = v[i]
print(max_element)
import math
#Basic mean and variance
nums = [2,4,6]

mean = sum(nums)/len(nums)
variance = sum((x - mean) ** 2 for x in nums)/len(nums)
print(f"Mean: {mean}")
print(f"Variance: {variance}")



#Standard deviation
nums = [1,3,5]
mean = sum(nums)/len(nums)
variance = sum((x - mean) ** 2 for x in nums)/len(nums)

standard_deviation = math.sqrt(variance)

print(f"Variance: {variance}")
print(f"Standard Deviation: {standard_deviation}")



#Zero Variance
nums = [7,7,7,7]
mean = sum(nums)/len(nums)
variance = sum((x - mean) ** 2 for x in nums)/len(nums)

standard_deviation = math.sqrt(variance)

print(f"Variance: {variance}")
print(f"Standard Deviation: {standard_deviation}")




#Compare Spread
A = [9,10,11]
B = [1,10,20]
#A set
mean = sum(A)/len(A)
varianceA = sum((x - mean) ** 2 for x in A)/len(A)
standard_deviationA = math.sqrt(varianceA)

#B set
mean = sum(B)/len(B)
varianceB = sum((x - mean) ** 2 for x in B)/len(B)
standard_deviationA = math.sqrt(varianceB)

if varianceA > varianceB:
    print("A spread out more.")
else:
    print("B spread out more.")




#Build function
def variance(nums):
    mean = sum(nums)/len(nums)
    variance = sum((x - mean) ** 2 for x in nums)/len(nums)
    return variance

def standard_deviation(nums):
    standard_deviation = math.sqrt(variance(nums))
    return standard_deviation

nums = list(map(int, input("Enter a list: ").split()))
print(variance(nums))
print(standard_deviation(nums))



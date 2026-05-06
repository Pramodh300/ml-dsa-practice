'''#Mean of list
nums = [10,20,30,40]

total_sum = sum(nums)
total_nums = len(nums)

print(total_sum/total_nums)



#Median (odd length)
nums = [1,3,5,6,8]
nums.sort()
length = len(nums)

median = nums[length//2]
print(median)




#Median (even length)
nums = [1,2,3,4]
nums.sort()

length = len(nums)

median = (nums[length//2-1] + nums[length//2])/2
print(median)




#Mode (Single)
nums = [1,2,2,3,4]
freq = {}

for num in nums:
    freq[num] = freq.get(num, 0)+1

mode = max(freq, key = freq.get)

print(mode)




#Mode (multiple)
nums = [1,1,2,2,3,4,4]

freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1

max_freq = max(freq.values())

mode = []
for num in freq:
    if freq[num] == max_freq:
        mode.append(num)

print(mode)




#All three(mean, median, mode)
nums = [4,1,2,2,3]
nums.sort()
t = sum(nums)
n = len(nums)
#mean
mean = t/n
print(mean)
#median
median = n//2
print(median)
#mode
freq = {}
for num in nums:
    freq[num] = freq.get(num, 0)+1

max_freq = max(freq.values())
mode = []
for num in freq:
    if freq[num] == max_freq:
        mode.append(num)
print(mode)




#Median without sorting
import heapq
nums = [1,1,2,2,3]
max_heap = []
min_heap = []
for num in nums:
    heapq.heappush(max_heap, -num)

    heapq.heappush(min_heap, -heapq.heappop(max_heap))

    if len(min_heap) > len(max_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))

if len(max_heap) > len(min_heap):
    median = -max_heap[0]

else:
    median = (-max_heap[0] + min_heap[0]) / 2

print(median)




#Running mean
nums = [10,20,30,40]

running_sum = 0
result = []
for i, num in enumerate(nums, 1):
    running_sum += num
    result.append(running_sum//i)
print(result)




#Remove outliers then find mean
nums = [10,12,14,1000]
nums.sort()

filtered = nums[1:-1]
t = sum(filtered)
n = len(filtered)

print(t//n)




#Median of two sorted arrays
a = [1,3]
b = [2]

c = a+b
c.sort()

n = len(c)
if n % 2 == 1:
    median = c[n //2]

else:
    median = (c[n//2-1] + c[n//2])/2

print(median)
'''



#Frequency-based mode
nums = [4,1,2,2,3]

freq = {}
for num in nums:
    freq[num] = freq.get(num, 0)+1

max_freq = 0
mode = None

for key in freq:
    if freq[key] > max_freq:
        max_freq = freq[key]
        mode = key
print(mode, max_freq)

#Balanced Parentheses
def is_balanced(s):
    stack = []
    pairs = {")":"(","}":"{","]":"["}

    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return len(stack) == 0

print(is_balanced("({[}])"))
print(is_balanced("(({{[[]]}}))"))
print(is_balanced("[{}]"))


#Min stack
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))

        else:
            self.min_stack.append(val)

    def pop(self):
        self.min_stack.pop()

    def peek(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]

ms = MinStack()
ms.push(2)
ms.push(1)
ms.push(10)
print(ms.get_min())
print(ms.peek())


#Reverse word
def reverse_word(word):
    stack = []
    for ch in word:
        stack.append(ch)

    result = ""
    while stack:
        result += stack.pop()
    
    return result

print(reverse_word("hello"))


#Next Greater Element
arr = [4,5,2,10,8]

stack = []
result = []

for num in reversed(arr):
    while stack and stack[-1] < num:
        stack.pop()

    if not stack:
        result.append(-1)

    else:
        result.append(stack[-1])

    stack.append(num)

result.reverse()

print(result)
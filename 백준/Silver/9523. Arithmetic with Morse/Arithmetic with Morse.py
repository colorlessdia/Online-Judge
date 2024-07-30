from collections import deque

N = int(input())
lines = input().split()

matched_morse = {
  '.': 1,
  '-': 5,
  ':': 2,
  '=': 10
}

stack = deque()

for line in lines:
    
    if line[0] in '+*':
        stack.append(line[0])
        continue
    
    temp = 0

    for char in line:
        temp += matched_morse[char]
    
    stack.append(str(temp))

print(eval(''.join(stack)))
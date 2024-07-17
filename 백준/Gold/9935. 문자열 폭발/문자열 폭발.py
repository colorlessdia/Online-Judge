from collections import deque

string = input()
target_string = input()
target_length = len(target_string)

string_stack = deque()

for c in string:
    string_stack.append(c)

    if len(string_stack) < len(target_string):
        continue
    
    if c != target_string[-1]:
        continue
    
    temp = ''

    for i in range(1, target_length + 1):
        temp += string_stack[-i]
    
    if temp[::-1] == target_string:
        for _ in range(target_length):
            string_stack.pop()

if len(string_stack) == 0:
    print('FRULA')
else:
    print(''.join(string_stack))
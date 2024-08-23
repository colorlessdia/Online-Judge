from collections import deque

S = input()

string = ''

stack = deque()

tag_state = False

for char in S:
    
    if char == '<':
        tag_state = True
    
    if tag_state:
        stack.append(char)

        if char == '>':
            string += ''.join(stack)
            stack.clear()
            tag_state = False

        continue
    
    if char == ' ':
        string += ''.join(stack) + ' '
        stack.clear()
        continue

    stack.appendleft(char)

if len(stack) != 0:
    string += ''.join(stack)
    stack.clear()

print(string)
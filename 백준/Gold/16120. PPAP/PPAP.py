from collections import deque

string = input()
string_stack = deque()

for char in string:
    string_stack.append(char)

    if len(string_stack) < 4:
        continue
    
    if char == 'A':
        continue

    temp = ''.join([string_stack[-i] for i in range(1, 4 + 1)][::-1])
    
    if temp == 'PPAP':
        for _ in range(4):
            string_stack.pop()
        
        string_stack.append('P')

if ''.join(string_stack) == 'P':
    print('PPAP')
else:
    print('NP')
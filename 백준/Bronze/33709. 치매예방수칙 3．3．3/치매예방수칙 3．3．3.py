N = int(input())
S = input()

temp = []
count = 0

for char in S:
    
    if char.isdigit():
        temp.append(char)
        continue
    
    count += int(''.join(temp))
    temp = []

count += int(''.join(temp))

print(count)
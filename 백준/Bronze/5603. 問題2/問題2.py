def formatted_string(string):
    temp = []
    count = 1

    for i in range(len(string) - 1):
        current = string[i]
        after = string[i + 1]

        if current == after:
            count += 1
            continue

        temp.append(str(count) + current)
        count = 1
    
    temp.append(str(count) + string[-1])

    return ''.join(temp)

N = int(input())
L = input()
S = L

for _ in range(N):
    S = formatted_string(S)

print(S)
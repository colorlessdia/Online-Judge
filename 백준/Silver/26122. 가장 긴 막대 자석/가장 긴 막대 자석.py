K = int(input())
S = input()

before_length_list = []
before = S[0]
accumulation = 1

for i in range(1, K):
    char = S[i]
    
    if char == before:
        accumulation += 1
    else:
        before_length_list.append(accumulation)
        before = char
        accumulation = 1

    if i == K - 1:
        before_length_list.append(accumulation)

if len(before_length_list) == 1:
    print(0)
else:
    maximum_length = 0
    
    for j in range(len(before_length_list) - 1):
        A = before_length_list[j]
        B = before_length_list[j + 1]
        L = min(A, B) * 2
        
        if maximum_length < L:
            maximum_length = L
    
    print(maximum_length)
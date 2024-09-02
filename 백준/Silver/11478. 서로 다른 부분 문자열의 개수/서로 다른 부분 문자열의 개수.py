S = input()

substring_dict = dict()

count = 0

for i in range(1, len(S) + 1):
    
    for j in range(len(S) + 1 - i):
        
        if S[j:j + i] not in substring_dict:
            substring_dict[S[j:j + i]] = 1
            count += 1

print(count)
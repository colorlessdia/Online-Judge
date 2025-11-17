S = input()

total_score = 1
cumulative_score = 1

for i in range(1, len(S)):
    before = S[i - 1]
    current = S[i]

    if before < current:
        cumulative_score += 1
    else:
        cumulative_score = 1
    
    total_score += cumulative_score

print(total_score)
import sys

input = sys.stdin.readline

N = int(input())

painting_list = [''] * (N + 1)
painting_pair = []
maximum_similarity = -1

for i in range(1, N + 1):
    painting_list[i] = ''.join([input().rstrip() for _ in range(5)])

for j in range(1, N + 1):
    A = painting_list[j]

    for k in range(j + 1, N + 1):
        B = painting_list[k]

        similarity = 0

        for l in range(35):
            
            if A[l] == B[l]:
                similarity += 1
        
        if maximum_similarity < similarity:
            maximum_similarity = similarity
            painting_pair = [j, k]

print(*painting_pair)
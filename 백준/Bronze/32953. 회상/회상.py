import sys

input = sys.stdin.readline

N, M = map(int, input().split())

id_count = dict()

for _ in range(N):
    K = int(input())
    id_sequence = map(int, input().split())

    for id in id_sequence:

        if id not in id_count:
            id_count[id] = 0
        
        id_count[id] += 1

student_count = 0

for count in id_count.values():

    if M <= count:
        student_count += 1

print(student_count)
import sys

input = sys.stdin.readline

L, X = map(int, input().split())

count = 0
rejected_group = 0

for _ in range(X):
    event, people = input().rstrip().split()
    people = int(people)

    if event == 'leave':
        count -= people
        continue

    if L < count + people:
        rejected_group += 1
        continue

    count += people

print(rejected_group)
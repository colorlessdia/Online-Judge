import sys

input = sys.stdin.readline

N = int(input())

contact_dict = {input().rstrip(): 1 for _ in range(N)}

M = int(input())

count = 0

for _ in range(M):
    address = input().rstrip()

    if address not in contact_dict:
        continue
    
    count += 1

print(count)
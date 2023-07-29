import sys

cnt_dict = {sys.stdin.readline().rstrip(): 1 for _ in range(int(input()))}
cnt = 0

for _ in range(int(input())):
    s = sys.stdin.readline().rstrip()

    if s in cnt_dict:
        cnt += 1 

print(cnt)
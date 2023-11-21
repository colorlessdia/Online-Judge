import sys

cnt_dict = dict()

for _ in range(int(input())):
    s = sys.stdin.readline().rstrip()
    
    if s in cnt_dict:
        cnt_dict[s] += 1
    else:
        cnt_dict[s] = 1

cnt = 0

for v in cnt_dict.values():
    if 1 < v:
        cnt += 1
        
print(cnt)
import sys

trophy = [int(sys.stdin.readline()) for _ in range(int(input()))]

l_vis, l_cnt = 0, 0
r_vis, r_cnt = 0, 0

for l in trophy:
    if l_vis < l:
        l_vis = l
        l_cnt += 1

for r in reversed(trophy):
    if r_vis < r:
        r_vis = r
        r_cnt += 1

print(l_cnt)
print(r_cnt)
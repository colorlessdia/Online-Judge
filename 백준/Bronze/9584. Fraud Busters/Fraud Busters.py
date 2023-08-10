import sys

std = input()
star = 9 - std.count('*')
cnt = 0
eq_list = []

for _ in range(int(input())):
    target = sys.stdin.readline().rstrip()
    eq = 0

    for s, t in zip(std, target):
        if s != '*' and s == t:
            eq += 1

    if star == eq:
        cnt += 1
        eq_list.append(target)
        
print(cnt)

for i in eq_list:
    print(i)
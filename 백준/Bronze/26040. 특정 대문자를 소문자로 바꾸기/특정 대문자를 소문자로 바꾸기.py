a = input()
b = input().split()

s = a

for bb in b:
    s = s.replace(bb, bb.lower())

print(s)
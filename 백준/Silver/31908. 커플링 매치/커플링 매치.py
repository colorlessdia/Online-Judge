import sys

N = int(sys.stdin.readline())

ring_count = dict()

for _ in range(N):
    p, s = sys.stdin.readline().rstrip().split()

    if s == '-':
        continue
    
    if s not in ring_count:
        ring_count[s] = [p]
    else:
        ring_count[s] += [p]

couple_count = 0
couple_list = []

for ring, master_list in ring_count.items():
    
    if len(master_list) == 2:
        couple_count += 1
        couple_list.append(master_list)

print(couple_count)

for couple in couple_list:
    print(' '.join(couple))
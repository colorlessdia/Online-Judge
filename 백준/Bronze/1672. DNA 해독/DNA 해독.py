from collections import deque

N = int(input())
DNA = deque(input())

base = ['A', 'G', 'C', 'T']
base_list = [
    ['A', 'C', 'A', 'G'],
    ['C', 'G', 'T', 'A'],
    ['A', 'T', 'C', 'G'],
    ['G', 'A', 'G', 'T'],
]

matched_base = dict()

for i in range(4):
    
    for j in range(4):
        k = (base[i], base[j])
        v = base_list[i][j]

        matched_base[k] = v

while 1 < len(DNA):
    col = DNA.pop()
    row = DNA.pop()

    DNA.append(matched_base[(row, col)])

print(''.join(DNA))
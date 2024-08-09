import sys

n = int(sys.stdin.readline())

tree_count = dict()

for _ in range(n):
    g, r = map(int, sys.stdin.readline().split())

    if r not in tree_count:
        tree_count[r] = g
        continue
    
    if tree_count[r] < g:
        tree_count[r] = g

print(len(tree_count.keys()))
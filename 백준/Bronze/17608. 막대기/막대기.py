import sys
from collections import deque

N = int(input())

bar_list = reversed([int(sys.stdin.readline()) for _ in range(N)])
bar_stack = deque()

height = 0

for bar in bar_list:
    if height < bar:
        bar_stack.append(bar)
        height = bar

visible_bar = len(bar_stack)

print(visible_bar)
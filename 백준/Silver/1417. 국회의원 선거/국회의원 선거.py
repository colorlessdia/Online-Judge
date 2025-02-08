import sys
from heapq import heappush, heappop

input = sys.stdin.readline

vote_count = 0
max_vote = []

N = int(input())

for candidate in range(1, N + 1):
    vote = int(input())

    if candidate == 1:
        vote_count = vote
        continue

    heappush(max_vote, -vote)

buy_count = 0

while 0 < len(max_vote):
    vote = -heappop(max_vote)
    
    if vote < vote_count:
        break
    
    heappush(max_vote, -(vote - 1))

    buy_count += 1
    vote_count += 1

print(buy_count)
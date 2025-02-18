from heapq import heappush, heappop

N, M, K = map(int, input().split())
P_list = list(map(int, input().split()))

plan_list = []

for i in range(N):
    P = P_list[i]

    if 0 <= M - P:
        heappush(plan_list, -P)

        M -= P
        continue

    if K == 0:
        break

    heappush(plan_list, -P)
    heappush(plan_list, 0)

    plan = -heappop(plan_list)

    M += plan - P
    K -= 1

diet_day = len(plan_list)

print(diet_day)
N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)

day = 0
complete_list = []

for a in A:
    complete_list.append(a + day)

    day += 1

print(max(complete_list))
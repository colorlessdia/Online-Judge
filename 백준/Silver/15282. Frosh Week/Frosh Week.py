N, M = map(int, input().split())
T_list = sorted(map(int, input().split()), key=lambda x: -x)
E_list = sorted(map(int, input().split()), key=lambda x: -x)

index = 0
count = 0

for T in T_list:

    for i in range(index, M):
        E = E_list[i]

        if E < T:
            break
        
        index = i + 1
        count += 1
        break

print(count)
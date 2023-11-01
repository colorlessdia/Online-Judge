n = int(input())
car_num = map(int, input().split())

cnt = 0

for num in car_num:
    if num == n:
        cnt += 1

print(cnt)
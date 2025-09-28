N = int(input())
number_list = list(map(int, input().split()))

height_list = []
temp = []

for i in range(N):
    number = number_list[i]
    
    if (not temp) or (temp[-1] < number):
        temp.append(number)
        continue

    if temp:
        height_list.append(temp[-1] - temp[0])

    temp.clear()
    temp.append(number)

if 2 <= len(temp):
    height_list.append(temp[-1] - temp[0])
    temp.clear()

print(max(height_list))
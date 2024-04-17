from collections import deque

N, K = map(int, input().split())

prime_list = []
number_list = deque(range(2, N + 1))

is_find = False

count = 0

while 0 < len(number_list):
    P = number_list[0]

    for i in range(P, N + 1, P):
        if i == P and i in number_list:
            prime_list.append(i)
            number_list.remove(i)
            count += 1
        elif i in number_list:
            number_list.remove(i)
            count += 1
        
        if count == K:
            is_find = True
            print(i)
            break
        
    if is_find:
        break
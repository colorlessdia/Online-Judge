T = int(input())

t = T
r_list = []

while 0 < t:
    r = t % 9
    r_list.append(str(r))
    t //= 9

print(''.join(reversed(r_list)))
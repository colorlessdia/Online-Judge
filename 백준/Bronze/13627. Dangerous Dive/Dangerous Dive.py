n, r = map(int, input().split())
nums = map(int, input().split())

chk_list = [0] * (n + 1)

for n in nums:
    chk_list[n] += 1

return_list = [i for i, c in enumerate(chk_list[1:], 1) if c == 0]

if len(return_list) == 0:
    print('*')
else:
    print(*return_list)
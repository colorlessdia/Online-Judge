ch, cm, cs = map(int, input().split(':'))
sh, sm, ss = map(int, input().split(':'))

cur_time = (ch * 3600) + (cm * 60) + cs
start_time = (sh * 3600) + (sm * 60) + ss

h, m, s = 0, 0, 0

if cur_time < start_time:
    calc_time = start_time - cur_time
else:
    calc_time = 86400 - cur_time + start_time

h = str(calc_time // 3600).zfill(2)
calc_time %= 3600
m = str(calc_time // 60).zfill(2)
calc_time %= 60
s = str(calc_time).zfill(2)

print(f'{h}:{m}:{s}')
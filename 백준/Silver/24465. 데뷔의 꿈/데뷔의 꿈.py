import sys

def calc_constellation(month, day):
    
    if (month == 1 and 20 <= day) or (month == 2 and day <= 18):
        return 'Aquarius'
    
    if (month == 2 and 19 <= day) or (month == 3 and day <= 20):
        return 'Pisces'
    
    if (month == 3 and 21 <= day) or (month == 4 and day <= 19):
        return 'Aries'
    
    if (month == 4 and 20 <= day) or (month == 5 and day <= 20):
        return 'Taurus'
    
    if (month == 5 and 21 <= day) or (month == 6 and day <= 21):
        return 'Gemini'
    
    if (month == 6 and 22 <= day) or (month == 7 and day <= 22):
        return 'Cancer'
    
    if (month == 7 and 23 <= day) or (month == 8 and day <= 22):
        return 'Leo'
    
    if (month == 8 and 23 <= day) or (month == 9 and day <= 22):
        return 'Virgo'
    
    if (month == 9 and 23 <= day) or (month == 10 and day <= 22):
        return 'Libra'
    
    if (month == 10 and 23 <= day) or (month == 11 and day <= 22):
        return 'Scorpio'
    
    if (month == 11 and 23 <= day) or (month == 12 and day <= 21):
        return 'Sagittarius'
    
    if (month == 12 and 22 <= day) or (month == 1 and day <= 19):
        return 'Capricorn'

member_constellation = dict()

for _ in range(7):
    mm, dd = map(int, sys.stdin.readline().split())

    constellation = calc_constellation(mm, dd)

    if constellation not in member_constellation:
        member_constellation[constellation] = 1

N = int(sys.stdin.readline())

passed_list = []

for _ in range(N):
    mm, dd = map(int, sys.stdin.readline().split())

    constellation = calc_constellation(mm, dd)

    if constellation not in member_constellation:
        passed_list.append((mm, dd))

sorted_passed_list = sorted(passed_list, key=lambda x: (x[0], x[1]))

if len(sorted_passed_list) == 0:
    print('ALL FAILED')
else:
    for mm, dd in sorted_passed_list:
        print(mm, dd)
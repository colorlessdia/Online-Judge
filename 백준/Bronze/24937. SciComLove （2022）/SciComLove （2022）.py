s = 'SciComLove'

n = int(input())

if 10 <= n:
    n %= 10

print(s[n:] + s[:n])
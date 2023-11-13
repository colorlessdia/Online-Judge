n = int(input())

r = list('abcdefgh')
c = list('12345678')

chess = [rr + cc for cc in c for rr in r]

print(chess[n - 1])
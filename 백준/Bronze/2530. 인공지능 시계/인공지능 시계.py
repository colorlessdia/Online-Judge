sh, sm, ss = map(int, input().split())
sec = int(input())

sec %= (60 * 60 * 24)

for _ in range(sec):
    ss += 1

    if 60 <= ss:
        sm += 1
        ss = 0
    if 60 <= sm:
        sh += 1
        sm = 0
    if 24 <= sh:
        sh = 0

print(sh, sm, ss)
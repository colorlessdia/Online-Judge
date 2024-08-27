import sys

string = sys.stdin.readline().rstrip()

N = int(sys.stdin.readline())

count = 0

for _ in range(N):
    engraving = sys.stdin.readline().rstrip()
    engraving += engraving[:len(string) - 1]

    for i in range(len(engraving) - len(string) + 1):
        part = engraving[i:i + len(string)]

        if part == string:
            count += 1
            break

print(count)
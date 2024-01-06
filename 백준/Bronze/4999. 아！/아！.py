import sys

say = sys.stdin.readline().strip()
want = sys.stdin.readline().strip()

print('go') if len(want) <= len(say) else print('no')
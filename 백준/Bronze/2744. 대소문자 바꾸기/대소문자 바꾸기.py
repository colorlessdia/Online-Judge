import sys

s = sys.stdin.readline().strip()
new_s = ''
for c in s:
    if c.islower():
        new_s += c.upper()
    elif c.isupper():
        new_s += c.lower()

print(new_s)
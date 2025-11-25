S = input()

if len(S) == len(set([s for s in S])):
    print(1)
else:
    print(0)
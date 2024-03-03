dice = [input() for _ in range(3)]

if dice == [':::', ':o:', ':::']:
    print(1)
elif dice == ['o::', ':::', '::o'] or dice == ['::o', ':::', 'o::']:
    print(2)
elif dice == ['::o', ':o:', 'o::'] or dice == ['o::', ':o:', '::o']:
    print(3)
elif dice == ['o:o', ':::', 'o:o']:
    print(4)
elif dice == ['o:o', ':o:', 'o:o']:
    print(5)
elif dice == ['o:o', 'o:o', 'o:o'] or dice == ['ooo', ':::', 'ooo']:
    print(6)
else:
    print('unknown')
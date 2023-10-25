n = input()

u = n.index('U')
f = n[::-1].index('F')

print(('-' * u) + 'U' + ('C' * (len(n) - (u + f + 2))) +  'F' + ('-' * f))
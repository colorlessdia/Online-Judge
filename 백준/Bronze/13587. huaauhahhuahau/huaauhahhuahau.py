S = input()

vowels = [s for s in S if s in ['a', 'e', 'i', 'o', 'u']]

if ''.join(vowels) == ''.join(vowels[::-1]):
    print('S')
else:
    print('N')
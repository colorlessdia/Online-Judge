A = ''.join(sorted(input().replace(' ', '')))
B = ''.join(sorted(input().replace(' ', '')))

print('Is an anagram.') if A == B else print('Is not an anagram.')
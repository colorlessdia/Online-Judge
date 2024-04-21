N = int(input())
erased_string = input()

palindrome = ''

for char1, char2 in zip(erased_string, erased_string[::-1]):
    if char1 == '?' and char2 == '?':
        palindrome += 'a'
    elif char1 == '?':
        palindrome += char2
    elif char2 == '?':
        palindrome += char1
    else:
        palindrome += char1

print(palindrome)
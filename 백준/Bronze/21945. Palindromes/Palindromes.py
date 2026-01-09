def is_palindrome(s):

    for i in range(len(s) // 2):
        f, b = s[i], s[-(i + 1)]

        if f != b:
            return False

    return True

N = int(input())
string_sequence = input().rstrip().split()

count = 0

for string in string_sequence:
    
    if is_palindrome(string):
        count += int(string)

print(count)
def is_palindrome(word):
    half = int(len(word) / 2)

    if half == 0:
        return True

    prefix = word[:half]
    suffix = word[-half:]

    if prefix == suffix[::-1]:
        return is_palindrome(prefix)
    else:
        return False

S = input()

if is_palindrome(S):
    print('AKARAKA')
else:
    print('IPSELENTI')
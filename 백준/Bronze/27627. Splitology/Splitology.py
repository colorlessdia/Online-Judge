def check_palindrome(s):
    length = len(s)

    if 1 < length:
        
        for i in range(length // 2):
            a, b = s[i], s[-(i + 1)]

            if a != b:
                return False

    return True

S = input()
L = len(S)

is_palindrome = False
string_pair = []

if L == 1:
    is_palindrome = True
    string_pair.append(S)
else:

    for i in range(1, len(S)):
        A, B = S[:i], S[i:]

        check_A = check_palindrome(A)
        check_B = check_palindrome(B)

        if check_A and check_B:
            is_palindrome = True
            string_pair.append((A, B))
            break

if is_palindrome:
    print(*string_pair[0])
else:
    print('NO')
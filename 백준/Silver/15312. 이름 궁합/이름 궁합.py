from string import ascii_uppercase as uppercase

stroke_count = list(map(int, '32123323322122122212111221'))
matched_count = dict(zip(uppercase, stroke_count))

A = input()
B = input()

length = len(A)
dp = [[0 for _ in range(length * 2)] for _ in range(2, (length * 2) + 1)]
index = 0

for i in range(length):
    A_count = matched_count[A[i]]
    B_count = matched_count[B[i]]

    dp[0][index] = A_count
    index += 1
    dp[0][index] = B_count
    index += 1

before_length = len(dp[0])

for i in range(len(dp) - 1):
    j = i + 1

    for k in range(before_length - 1):
        score = (dp[i][k] + dp[i][k + 1]) % 10
        dp[j][k] = score
    
    before_length -= 1
    
formatted_score = ''.join(map(str, dp[-1][:2]))

print(formatted_score)
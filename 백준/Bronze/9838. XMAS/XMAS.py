import sys

n = int(input())

matched_customer = [0] * n

for i in range(n):
    k = int(sys.stdin.readline())

    matched_customer[k - 1] = i + 1

for customer in matched_customer:
    print(customer)
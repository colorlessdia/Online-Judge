n, a = map(int, input().split())
receipt_list = list(map(int, input().split()))

ticket = 0

for receipt in receipt_list:
    if a <= receipt:
        ticket += (receipt // a)

print(ticket)
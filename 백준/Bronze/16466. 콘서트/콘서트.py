N = int(input())
ticket_list = sorted(map(int, input().split()))

if ticket_list[0] != 1:
    print(1)
elif ticket_list[-1] != N:
    
    for i, ticket in enumerate(ticket_list, 1):
        
        if i != ticket:
            print(i)
            break
else:
    print(ticket_list[-1] + 1)
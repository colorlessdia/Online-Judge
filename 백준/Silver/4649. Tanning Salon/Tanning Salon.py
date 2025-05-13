import sys

input = sys.stdin.readline

while 1:
    line = input().rstrip().split()
    bed = int(line[0])

    if not bed:
        break
    
    salon = dict()
    return_customer = set()
    customer_sequence = line[1]

    for customer in customer_sequence:
        
        if customer not in salon:
            
            if len(salon) < bed:
                salon[customer] = 1
            else:
                return_customer.add(customer)
        else:
            del salon[customer]
    
    if len(return_customer) == 0:
        print('All customers tanned successfully.')
    else:
        print(f'{len(return_customer)} customer(s) walked away.')
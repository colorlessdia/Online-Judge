from math import sqrt

def is_prime(number):
    if number < 2:
        return False
    
    for i in range(2, int(sqrt(number)) + 1):        
        if number % i == 0:
            return False

    return True

prev_phone_number, prefix = input().split()
current_phone_number = int(prefix + prev_phone_number)

if is_prime(int(prev_phone_number)) and is_prime(current_phone_number):
    print('Yes')
else:
    print('No')
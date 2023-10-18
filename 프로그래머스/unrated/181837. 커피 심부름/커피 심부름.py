def solution(order):
    total = 0
    
    for o in order:
        if 'americano' in o or 'anything' == o:
            total += 4500
        elif 'latte' in o:
            total += 5000
    
    return total
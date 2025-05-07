def matched_string(hole):
    
    if hole < 2:
        return int(not hole)
    
    return int(('4' * (hole % 2)) + ('8' * (hole // 2)))

h = int(input())

print(matched_string(h))
def calculator(number_1, operator, number_2):

    if operator != '/':
        return str(eval(number_1 + operator + number_2))
    
    if int(number_1) < 0 and 0 <= int(number_2):
        return str(((int(number_1) * -1) // int(number_2)) * -1)
    
    if int(number_2) < 0 and 0 <= int(number_1):
        return str((int(number_1) // (int(number_2) * -1)) * -1)
    
    return str(int(number_1) // int(number_2))

K1, O1, K2, O2, K3 = input().split()

result_1 = int(calculator(calculator(K1, O1, K2), O2, K3))
result_2 = int(calculator(K1, O1, calculator(K2, O2, K3)))

min_result = min(result_1, result_2)
max_result = max(result_1, result_2)

print(min_result)
print(max_result)
import sys

def filter_product(product_count, product_list, count):
    temp = dict()
    
    for k, v in product_list:
        
        if k not in temp:
            temp[k] = 0
        
        temp[k] += int(v)
    
    for k, v in temp.items():
        v = int(v)

        if v < count:
            continue
        
        if k not in product_count:
            product_count[k] = 0

        product_count[k] += 1

input = sys.stdin.readline

n1, n2, n3 = map(int, input().split())
product_list = []

while 1:
    line = input().rstrip().split()

    if line == []:
        break
    
    for id, count in zip(line[::2], line[1::2]):
        product_list.append([id, count])

product_count = dict()

filter_product(product_count, product_list[:n1], 20)
filter_product(product_count, product_list[n1:n1 + n2], 20)
filter_product(product_count, product_list[-n3:], 20)

filtered_product = []

for k, v in product_count.items():
    
    if v == 3:
        filtered_product.append(k)

print(f'{len(filtered_product)} {' '.join(filtered_product)}')
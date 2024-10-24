import sys

item_history = dict()

while True:
    line = sys.stdin.readline().rstrip()

    if line == '':
        break
    
    item, stock, profit = line.split()

    stock = int(stock)
    profit = float(profit)

    total_profit = f'{(stock * profit):.2f}'

    item_history[item] = {
        'stock': stock,
        'total_profit': total_profit
    }

sorted_item = sorted(
                      item_history.items(), 
                      key=lambda x: (
                          -float(x[1]['total_profit']),
                          -int(x[1]['stock']),
                          x[0]
                      )
                    )

for item, detail in sorted_item:
    stock = detail['stock']
    total_profit = detail['total_profit']
    
    print(f'${total_profit} - {item}/{stock}')
N, K = map(int, input().split())

temperature_list = list(map(int, input().split()))

before_temperature = sum(temperature_list[:K])
max_temperature = before_temperature

for i in range(K, N):
    prefix_sum = before_temperature + temperature_list[i] - temperature_list[i - K]

    if max_temperature < prefix_sum:
        max_temperature = prefix_sum
        
    before_temperature = prefix_sum

print(max_temperature)
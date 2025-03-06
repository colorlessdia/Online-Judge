def matched_fizzbuzz(number):
    
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    
    if number % 3 == 0:
        return 'Fizz'
    
    if number % 5 == 0:
        return 'Buzz'
    
    return number

next_number = -1

for i in range(3, 0, -1):
    line = input()

    if line.isnumeric():
        next_number = int(line) + i

print(matched_fizzbuzz(next_number))
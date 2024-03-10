def camel_to_pascal(camel):
    return camel[0].upper() + camel[1:]

def camel_to_snake(camel):
    snake = ''

    for char in camel:
        if char.isupper():
            snake += '_' + char.lower()
            continue
        
        snake += char

    return snake

def snake_to_camel(snake):
    camel = ''

    is_upper = False

    for char in snake:
        if is_upper:
            camel += char.upper()
            is_upper = False
            continue

        if char == '_':
            is_upper = True
            continue
        
        camel += char
    
    return camel

def pascal_to_camel(pascal):
    return pascal[0].lower() + pascal[1:]

number, variable = input().split()

camel_case = ''
snake_case = ''
pascal_case = ''

if number == '1':
    camel_case = variable
    snake_case = camel_to_snake(camel_case)
    pascal_case = camel_to_pascal(camel_case)

elif number == '2':
    snake_case = variable
    camel_case = snake_to_camel(snake_case)
    pascal_case = camel_to_pascal(camel_case)

elif number == '3':
    pascal_case = variable
    camel_case = pascal_to_camel(pascal_case)
    snake_case = camel_to_snake(camel_case)

print(camel_case)
print(snake_case)
print(pascal_case)
N = int(input())

required_ingredients = {ingredient: 1 for ingredient in input().split()}
used_ingredients = input().split()

for ingredient in used_ingredients:
    del required_ingredients[ingredient]

print(list(required_ingredients.keys())[0])
def make_breakfast(meal, ingredients):
    print("Get ingredients")
    print("Mix")
    print("")
    print("Flip the other side")
    breakfast = []
    breakfast.append("Yummy " + meal)
    breakfast.append(ingredients)
    return breakfast

print(make_breakfast("Egg", ['ingredient1','ingredient2']))
print(make_breakfast("Pancake", ['ingredient3', 'ingredient4']))
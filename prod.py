# напишите здесь функцию print_shopping_list(),
# подобрав уникальные названия продуктов и сложив значения
def print_shopping_list(dish1, dish2):
    shopping_list = set(dish1).union(set(dish2))
    for product in shopping_list:
        if shopping_list[product] in dish1 or dish2:
            print(shopping_list.add(dish1, dish2))



pizza = {'мука, кг': 1,
         'помидоры, кг': 1.5,
         'шампиньоны, кг': 1.5,
         'сыр, кг': 0.8,
         'оливковое масло, л': 0.1,
         'дрожжи, г': 50}
salad = {'огурцы, кг': 1,
         'перцы, кг': 1,
         'помидоры, кг': 1.5,
         'оливковое масло, л': 0.1,
         'листья салата, кг': 0.4}

print_shopping_list(pizza, salad)

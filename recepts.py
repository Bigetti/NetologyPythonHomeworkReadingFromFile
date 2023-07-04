
cook_book = {}


with open('recept.txt', encoding='utf-8') as f:
    while True:
        dish_name = f.readline().strip()
        if not dish_name:
            break

        ingredients_counter = int(f.readline().strip())
        ingredients =[]

        for _ in range(ingredients_counter):
            ingredient_info = f.readline().strip().split(" | ")
            ingredient_name, quantity, measure = ingredient_info
            ingredient = {
                'ingridient_name': ingredient_name,
                'quantity': int(quantity),
                'measure': measure
            }

            ingredients.append(ingredient)


        cook_book[dish_name] = ingredients

        # Пропускаем пустую строку между блюдами
        f.readline()

# print (cook_book)
    
person_count = 4

dishes = list(cook_book.values())

def get_shop_list_by_dishes(dishes_for, person_count):
    dict1 = {}
    for dish in dishes_for:
        if dish in dishes:
        
            dict1 += {'ingredient_name': {'measure': measure, quantity: quantity}
                       }
    print (dict1)
    return dict1

        
get_shop_list_by_dishes(['Омлет'], 3)
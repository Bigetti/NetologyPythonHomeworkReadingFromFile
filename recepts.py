
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
                'ingredient_name': ingredient_name,
                'quantity': int(quantity),
                'measure': measure
            }

            ingredients.append(ingredient)


        cook_book[dish_name] = ingredients

        # Пропускаем пустую строку между блюдами
        f.readline()

    print (cook_book)
    print()
    print()
    




def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            ingredients = cook_book[dish]
            for ingredient in ingredients:
                ingredient_name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity']*person_count
                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] = {'quantity': quantity, 'measure': measure}
                else:
                    shop_list[ingredient_name][quantity]+=quantity

        else:
            print(f' блюдо {dish} отсутсвует в cook_book')
    
    return shop_list

dishes = ['Омлет', 'Запеченный картофель', 'пирог']        
result = get_shop_list_by_dishes(dishes, 5)

for ingredient_name, ingredient_info in result.items():
    quantity = ingredient_info['quantity']
    measure = ingredient_info['measure']
    print(f"{ingredient_name}: {quantity} {measure}")
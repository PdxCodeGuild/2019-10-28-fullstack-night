import json

def get_meals(meals_json):
    with open(meals_json) as f:
        return json.loads(f.read())

def save_meals(meals_json, meals):
    with open(meals_json, 'w') as f:
        return f.write(json.dumps(meals))

meals_json = 'tracker/management/commands/default_meals.json'

meals = get_meals(meals_json)

actions = ['create', 'retrieve', 'update', 'delete', 'quit']
headers = ['name', 'kcal', 'fat', 'carb', 'protein']

while True:

    print('Actions:')
    for i in range(len(actions)):
        print(i, actions[i])
    action = actions[int(input("Choose an action by integer: "))]

    if action not in actions:
        print("Choose a valid action.")
        continue

    if action == 'quit':
        save_meals(meals_json, meals)
        break

    if action == 'create':
        new_meal = {}
        for header in headers:
            new_meal[header] = input(f"{header}: ")
        meals.append(new_meal)
    
    elif action == 'retrieve':
        search = input('Retrieve which meal: ').casefold()
        for meal in meals:
            if meal['name'] == search:
                break
        for header in headers:
            meal[header] = print(f"{header}: {meal[header]}")

    elif action == 'update':
        search = input("Update which meal: ").casefold()
        for i, meal in enumerate(meals):
            if meal['name'] == search:
                break
        for header in headers:
            value = input(f"{header} ({meal[header]})")
            if value:
                meal[header] = value
        meals[i] = meal
    
    elif action == 'delete':
        search = input("Delete which meal: ").casefold()
        for i, meal in enumerate(meals):
            if meal['name'] == search:
                break
        meals.pop(i)
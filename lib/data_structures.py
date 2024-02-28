spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    #To return a list of names of spicy foods
    return [food["name"] for food in spicy_foods]
print(get_names(spicy_foods))
pass

def get_spiciest_foods(spicy_foods):
    # Returns a list of spicy foods with a heat level greater than 5
    return [food for food in spicy_foods if food["heat_level"] > 5]
print(get_spiciest_foods(spicy_foods))
pass

def print_spicy_foods(spicy_foods):
       # To print the names, cuisines, and heat levels of all spicy foods
      for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")
print(print_spicy_foods(spicy_foods))
pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
   # To return the first spicy food with the specified cuisine
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
print(get_spicy_food_by_cuisine(spicy_foods, 'cuisine'))
pass

def print_spiciest_foods(spicy_foods):
   # To print the names, cuisines, and heat levels of spicy foods with a heat level greater than 5
    for food in spicy_foods:
        if food["heat_level"] > 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")
print(print_spiciest_foods(spicy_foods))
pass
    
def get_average_heat_level(spicy_foods):
    # To calculate and return the average heat level of all spicy foods
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    return total_heat_level // len(spicy_foods)
print(get_average_heat_level(spicy_foods))
pass

def create_spicy_food(spicy_foods, new_spicy_food):
    # To add a new spicy food to the list of spicy foods
    spicy_foods.append(new_spicy_food)
    return spicy_foods

new_spicy_food = {
    "name": "Griot",
    "cuisine": "Haitian",
    "heat_level": 13,
}

updated_spicy_foods = create_spicy_food(spicy_foods, new_spicy_food)
print(updated_spicy_foods)
pass

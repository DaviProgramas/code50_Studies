fruits = {
    "apple": 130,
    "banana": 110,
    "avocado": 50,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "melon": 50,
    "lime": 20,
    "nectarine": 60,
    "kiwifruit": 90,
    "lemon": 15,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "Strawberries": 50,
    "sweetcherries": 100,
    "tangerine": 50,
    "watermelon": 80
}

fruit = input("Fruit: ").strip().lower()
if fruit in fruits:
    print("Calories:", fruits[fruit])
    
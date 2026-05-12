menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

valor = 0.0

while(True):
    try:
        item = input("Item: ").title()
        if item in menu:
            valor += menu[item]
            print(F"total: ${valor:.2f}")
        else: continue
    except (EOFError, KeyboardInterrupt):
        exit(0)

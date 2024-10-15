foods = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}

sum = 0

try:
    while True:
        text = input("Item: ").title()

        if text in foods:
            sum += foods[text]

        print(f"Total cost: ${sum:.2f}")

except EOFError:
    print()

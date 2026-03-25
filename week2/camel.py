var = input("camelCase: ")
for capital in var:
    if capital.isupper():
        var = var.replace(capital, "_" + capital.lower())

print("snake_case: " + var)
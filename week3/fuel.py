while(True):
    try:
        x, y = input("Fraction: ").split("/")
        x = int (x)
        y = int (y)

        if x < 0 or x > y or y == 0:
            continue

        break
    except (ValueError, ZeroDivisionError):
        pass

result = (x/y)*100

if result <= 1:
    result = "E"
elif result >= 99:
    result = "F"
else:
    result = f"{round(result)}%"

print(result)

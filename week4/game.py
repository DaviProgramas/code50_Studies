import random

level = int(input("level: "))

randnumber = random.randint(1,level)

n = 0

while(n != randnumber):
    n = int(input("guess: "))

    if n < 1:
        continue

    if n < randnumber:
        print("too small")
        continue
    elif n == randnumber:
        print("just right")
        exit(0)
    elif n > randnumber:
        print("too large")
        continue

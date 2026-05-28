from random import randint 

def get_level():
    Level = 0 
    while(True):
        try:
            while(1 > Level or Level > 3):
                Level = int(input("Level: "))

            if 0 < Level < 4:
                break

        except ValueError:
            pass

    return Level

def genarate_integer(level):
    if level == 1:
        number = randint(0,9)
    if level == 2:
        number = randint(10,99)
    if level == 3:
        number = randint(100, 999)

    return number

def main():
    level = get_level()
    counter = 0
    i = 0
    while i<10:
        x = genarate_integer(level)
        y = genarate_integer(level)
        answer = x + y
        j = 0
        while j<3:
            try: guess = int(input(f"{x} + {y} = "))
            except ValueError:
                continue

            if guess == answer: 
                counter += 1
                break
            if guess != answer: 
                if j == 2:
                    print("EEE")
                    print(f"{x} + {y} = {answer}")
                    j += 1
                    continue
                print("EEE")
                j += 1
                continue
        i += 1  

    print("score: ", counter) 


if __name__ == "__main__":
    main()
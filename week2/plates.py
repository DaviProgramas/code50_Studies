def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    for i in plate[0:2]:
        if i.isdigit(): return False
    
    if len(plate) < 2 or len(plate) > 6:
        return False
    
    numbers_started = False

    for i in plate:
        if i.isdigit() and i == '0' and numbers_started == False:
            return False
        elif i.isdigit():
            numbers_started = True
        elif numbers_started:
            return False
        
    for i in plate:
        if i in " ,.´~^`}":
            return False

    if plate: return True

main()
list = {}
while(True):
    try:
        item = input("Item: ").upper()

        if item.isdigit():
            continue
        if item in list:
            list[item] += 1
        else:
            list[item] = 1
        
    except ValueError:
        pass
    except KeyboardInterrupt:
        for item in sorted(list):
            print(list[item], item)
        exit(0)




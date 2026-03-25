coke = 50
coin = 0
paied = 0
while paied < 50:
    while coin != 25 and coin != 10 and coin != 5:
        print ("amount due:", coke)
        coin = int(input("insert coin: "))

    coke -= coin
    paied += coin
    if paied >= 50:
        print("change owned:", paied - 50)
        break
    coin = 0
 
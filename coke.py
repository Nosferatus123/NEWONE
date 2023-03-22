value = 50

while value > 0:
    print("amount due", value )
    coin = int(input("Insert Coin "))
    if coin == 5:
        value -= coin
    elif coin == 10:
        value -= coin
    elif coin == 25:
        value -= coin
    else:
        continue

change = abs(value)
print("changed owed", change)
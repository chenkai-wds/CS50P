amount_due = 50
while amount_due > 0:
    print("Amount Due: ", amount_due)
    coin = input("Insert Coin: ")
    if coin == "5" or coin == "10" or coin == "25":
        amount_due -= int(coin)

print("Change Owed:", -1 * amount_due)

"""
# better
due, inserted = 50, 0
while inserted < due:
    print("Amount Due:", due - inserted)
    coin = int(input("Insert Coin: "))
    if coin in [5, 10, 25]:
        inserted += coin
print("Change Owed:", inserted - due)

"""
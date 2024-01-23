coin_denominations = {25: "quarters", 10: "dimes", 5: "nickels", 1: "pennies"}

amount_to_change = int(input("Enter the amount to be converted into change: "))
remaining_amount = amount_to_change

change_result = []

for denomination_value in coin_denominations.keys():
    change_result.append(remaining_amount // denomination_value)
    remaining_amount = remaining_amount - (remaining_amount // denomination_value) * denomination_value

print("To provide change of ${}, you need to give:".format(amount_to_change))

counter = 0

for denomination_name in coin_denominations.values():
    if change_result[counter] == 0:
        counter += 1
        continue
    else:
        print("{} {}".format(str(change_result[counter]), denomination_name))
        counter += 1

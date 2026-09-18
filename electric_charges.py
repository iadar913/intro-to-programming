# Electric Charges

kw_hours = int(input("Enter the KW hours used: "))

if kw_hours <= 1000:
    amount_owed = kw_hours * 7.633 / 100
else:
    amount_owed = (1000 * 7.633 + (kw_hours - 1000) * 9.259) / 100

print("Amount owed is ${}".format(amount_owed))
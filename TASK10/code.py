price = float(input("Enter product price: "))
stock = int(input("Enter available stock: "))
qty = int(input("Enter order quantity: "))

if qty <= stock and qty > 0:
    bill = price * qty
    stock = stock - qty
    print("Total Bill:", bill)
    print("Remaining Stock:", stock)
else:
    print("Item Not Available")


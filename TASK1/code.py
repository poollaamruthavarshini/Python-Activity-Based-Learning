n = int(input("Enter number of products: "))

subtotal = 0
tax = 0

for i in range(n):
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    qty = int(input("Enter quantity: "))
    category = input("Enter category A, B or C: ")

    amount = price * qty
    subtotal += amount

    if category == "A":
        tax += amount * 0.05
    elif category == "B":
        tax += amount * 0.12
    elif category == "C":
        tax += amount * 0.18
    else:
        print("Invalid category")

discount = 0

if subtotal >= 1000:
    discount = subtotal * 0.10

    if discount > 200:
        discount = 200

total = subtotal - discount + tax

print("Subtotal:", subtotal)
print("Discount:", discount)
print("Tax:", tax)
print("Final Bill:", total)




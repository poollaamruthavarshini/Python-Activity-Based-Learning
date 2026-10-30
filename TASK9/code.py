opening = int(input("Enter opening stock: "))
received = int(input("Enter received quantity: "))
issued = int(input("Enter issued quantity: "))
actual = int(input("Enter actual closing stock: "))

expected = opening + received - issued

print("Expected Stock:", expected)

if expected == actual:
    print("Stock Matched")
else:
    print("Difference:", expected - actual)


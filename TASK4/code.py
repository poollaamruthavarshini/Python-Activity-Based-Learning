balance = float(input("Enter initial balance: "))

n = int(input("Enter number of transactions: "))

for i in range(n):
    choice = input("Enter deposit or withdraw: ")
    amount = float(input("Enter amount: "))

    if choice == "deposit":
        balance += amount
    elif choice == "withdraw":
        if amount <= balance:
            balance -= amount
        else:
            print("Insufficient balance")
    else:
        print("Invalid transaction")

print("Final Balance:", balance)

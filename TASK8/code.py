products = (
    (101, "Pen", 10),
    (102, "Book", 50),
    (103, "Bag", 500)
)

for p in products:
    print(p)

prices = [p[2] for p in products]

print("Highest Price:", max(prices))
print("Lowest Price:", min(prices))


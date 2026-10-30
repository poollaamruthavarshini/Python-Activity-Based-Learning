## Case Study No. 57 – Smart Canteen Order and Stock Management

 Case Study No. 57

### 1. Problem Statement

Process customer orders, calculate bills, update available stock, reject unavailable quantities and display remaining stock.

### 2. Algorithm

1. Start.
2. Enter product name, price and available stock.
3. Enter ordered quantity.
4. Check stock availability.
5. If available, calculate bill and update stock.
6. Otherwise, display unavailable quantity.
7. Display final bill and remaining stock.
8. Stop.

### 3. Flowchart 
```Mermaid

flowchart TD
    A([Start]) --> B[/Enter price and stock/]
    B --> C[/Enter order quantity/]
    C --> D{Quantity <= Stock?}
    D -- Yes --> E[Calculate bill]
    E --> F[Update stock]
    D -- No --> G[/Display Not Available/]
    F --> H[/Display bill and stock/]
    G --> H
    H --> I([Stop])
```

### 5. Sample Input

```
Enter product price: 20
Enter available stock: 50
Enter order quantity: 5
```

### 6. Sample Output

```
Total Bill: 100.0
Remaining Stock: 45
```

Source: Your uploaded Python Activity-Based Learning PDF.

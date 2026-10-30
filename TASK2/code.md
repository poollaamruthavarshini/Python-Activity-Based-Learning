## Case Study 1: Progressive Electricity Billing

### 1. Problem Statement

Calculate the electricity bill based on the number of units consumed using different tariff rates.

### 2. Algorithm

1. Start.
2. Enter electricity units.
3. If units are negative, display invalid input.
4. If units are up to 100, multiply by ₹2.
5. If units are up to 200, calculate the bill using ₹3 for extra units.
6. Otherwise, calculate the bill using ₹5 for units above 200.
7. Display the bill.
8. Stop.

### 3. Flowchart 
```Mermaid

flowchart TD
    A([Start]) --> B[/Enter units/]
    B --> C{Units < 0?}
    C -- Yes --> D[/Invalid Input/]
    C -- No --> E{Units <= 100?}
    E -- Yes --> F[Bill = Units * 2]
    E -- No --> G{Units <= 200?}
    G -- Yes --> H[Bill = 200 + extra units * 3]
    G -- No --> I[Bill = 500 + extra units * 5]
    F --> J[/Display Bill/]
    H --> J
    I --> J
    D --> K([Stop])
    J --> K
```


### 5. Sample Input

```
Enter units: 250
```

### 6. Sample Output

```
Electricity Bill: 750
```


## Case Study No. 14– Warehouse Inventory Reconciliation

### 1. Problem Statement

Calculate the expected closing stock of products and compare it with the actual closing stock.

### 2. Algorithm

1. Start.
2. Enter opening stock.
3. Enter received quantity and issued quantity.
4. Calculate expected closing stock.
5. Enter actual closing stock.
6. Compare both quantities.
7. Display the difference.
8. Stop.

### 3. Flowchart 
```Mermaid

flowchart TD
    A([Start]) --> B[/Enter opening stock/]
    B --> C[/Enter received and issued quantity/]
    C --> D[Calculate expected stock]
    D --> E[/Enter actual stock/]
    E --> F{Expected = Actual?}
    F -- Yes --> G[/Stock Matched/]
    F -- No --> H[Calculate difference]
    H --> I[/Display difference/]
    G --> J([Stop])
    I --> J
```
### 4. Sample Input

```
Enter opening stock: 100
Enter received quantity: 50
Enter issued quantity: 30
Enter actual closing stock: 110
```

### 5. Sample Output

```
Expected Stock: 120
Difference: 10
```

## Case Study No. 13 – ATM Transaction Sequence Simulation

### 1. Problem Statement

Simulate ATM transactions such as deposits and withdrawals while maintaining the account balance.

### 2. Algorithm

1. Start.
2. Enter the initial balance.
3. Enter the transaction type.
4. If deposit, add the amount to the balance.
5. If withdrawal, subtract the amount if sufficient balance is available.
6. Display the updated balance.
7. Stop.

### 3. Flowchart 
```Mermaid

flowchart TD
    A([Start]) --> B[/Enter balance/]
    B --> C[/Enter transaction type and amount/]
    C --> D{Deposit?}
    D -- Yes --> E[Add amount to balance]
    D -- No --> F{Sufficient balance?}
    F -- Yes --> G[Subtract amount]
    F -- No --> H[/Insufficient balance/]
    E --> I[/Display balance/]
    G --> I
    H --> I
    I --> J([Stop])
```

### 5. Sample Input

```
Enter initial balance: 5000
Enter number of transactions: 2
Enter deposit or withdraw: deposit
Enter amount: 1000
Enter deposit or withdraw: withdraw
Enter amount: 2000
```

### 6. Sample Output

```
Final Balance: 4000.0
```

## Case Study 3: Attendance Recovery Computation

### 1. Problem Statement

Calculate a student's attendance percentage and find how many consecutive classes are needed to reach the required attendance.

### 2. Algorithm

1. Start.
2. Enter total classes and attended classes.
3. Calculate attendance percentage.
4. Check whether attendance is at least 75%.
5. If not, calculate the required additional classes.
6. Display the attendance percentage and required classes.
7. Stop.

### 3. Flowchart 
```Mermaid

flowchart TD
    A([Start]) --> B[/Enter total and attended classes/]
    B --> C[Calculate attendance percentage]
    C --> D{Attendance >= 75?}
    D -- Yes --> E[/Eligible/]
    D -- No --> F[Calculate required classes]
    F --> G[/Display required classes/]
    E --> H([Stop])
    G --> H
```

### 4. Sample Input

```
Enter total classes: 40
Enter attended classes: 25
```

### 5. Sample Output

```
Attendance: 62.5 %
Required classes: 20
```

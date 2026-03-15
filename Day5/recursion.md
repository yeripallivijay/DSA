
---

# 📘 Recursion – FAANG Interview Revision Notes

Recursion is one of the most important concepts in **Data Structures and Algorithms (DSA)** and is heavily used in **FAANG interviews**. Many complex problems like **tree traversal, backtracking, divide and conquer, and dynamic programming** rely on recursion.

---

# 1️⃣ What is a Function?

A **function** is a reusable block of code that performs a specific task.

### Key Points

* Functions improve **modularity and readability**.
* They can accept **parameters (input)**.
* They may **return a value**.

Example in Python:

```python
def add(a, b):
    return a + b

print(add(2, 3))
```

---

# 2️⃣ What is Recursion?

**Recursion** is a technique where a function **calls itself** to solve smaller instances of the same problem.

### Key Idea

Break a large problem into **smaller identical subproblems** until it reaches a **base case**.

### Structure of a Recursive Function

A recursive function always has:

1. **Base Case** → Stops recursion
2. **Recursive Case** → Calls itself with smaller input

Example:

```python
def print_numbers(n):
    if n == 0:      # Base case
        return
    print(n)
    print_numbers(n-1)  # Recursive call

print_numbers(5)
```

Output:

```
5 4 3 2 1
```

---

# 3️⃣ Infinite Recursion

**Infinite recursion** occurs when a function keeps calling itself **without a base condition**.

This causes a **stack overflow**.

Example:

```python
def infinite_recursion():
    print("Calling function")
    infinite_recursion()
```

Running this will crash the program because the recursion **never stops**.

---

# 4️⃣ Base Case

The **base case** is the stopping condition of recursion.

Without it, recursion will run forever.

Example:

```python
def factorial(n):
    if n == 0:        # Base case
        return 1
    return n * factorial(n-1)
```

---

# 5️⃣ Recursive Stack Space

Every recursive call is stored in a **Call Stack**.

Each function call creates a **stack frame** that stores:

* function parameters
* local variables
* return address

Example:

```python
factorial(4)
```

Call stack:

```
factorial(4)
factorial(3)
factorial(2)
factorial(1)
factorial(0)  ← base case
```

Then the stack **unwinds**.

```
1 → 1*1 → 2*1 → 3*2 → 4*6
```

Result = **24**

---

# 6️⃣ Program Flow in Recursion

Steps:

1. Function is called.
2. It calls itself with a smaller input.
3. Calls keep stacking.
4. Base case is reached.
5. Stack starts **unwinding**.

---

# 7️⃣ Types of Recursion

## 1. Head Recursion

The **recursive call happens first**, then processing occurs.

Example:

```python
def head_recursion(n):
    if n > 0:
        head_recursion(n - 1)
        print(n, end=" ")

head_recursion(5)
```

Output:

```
1 2 3 4 5
```

### Flow

```
Call Stack Builds First
Processing Happens Later
```

---

## 2. Tail Recursion

The **recursive call is the last operation**.

Example:

```python
def tail_recursion(n):
    if n == 0:
        return
    print(n, end=" ")
    tail_recursion(n - 1)

tail_recursion(5)
```

Output:

```
5 4 3 2 1
```

### Advantage

Some compilers perform **Tail Call Optimization (TCO)** to reduce stack usage.

---

# 8️⃣ Stack Overflow

A **stack overflow** occurs when:

* recursion depth is too large
* base case is missing
* too many stack frames are created

Example:

```
Recursion Depth > Stack Limit
```

Result:

```
Program Crash
```

---

# 9️⃣ Recursion Tree

A **recursion tree** visualizes how recursive calls expand.

Example:

```
func(3)
 ├── func(2)
 │    ├── func(1)
 │    │    └── func(0)
 │    └── func(1)
 └── func(2)
```

Recursion trees help analyze **time complexity**.

---

# 🔟 Time Complexity

Time complexity depends on **number of recursive calls**.

Example:

```
T(n) = T(n-1) + O(1)
```

Time Complexity:

```
O(n)
```

For branching recursion:

```
T(n) = 2T(n-1)
```

Time Complexity:

```
O(2^n)
```

Example: Fibonacci recursion.

---

# 1️⃣1️⃣ Space Complexity

Space complexity depends on **maximum recursion depth**.

If recursion depth = **n**

```
Space Complexity = O(n)
```

Because **n stack frames** exist simultaneously.

---

---

# 📘 Parameterized Recursion – FAANG Interview Revision Notes

Parameterized recursion is an important recursion pattern used in **Data Structures and Algorithms (DSA)**.
Instead of relying on **global variables or implicit state**, all required information is passed as **function parameters**.

This approach results in:

* ✔ Better control over recursion flow
* ✔ Cleaner and more readable code
* ✔ No dependency on global variables
* ✔ Easier debugging and testing

---

# 1️⃣ What is Parameterized Recursion?

In **parameterized recursion**, the recursive function receives all necessary information as parameters.

### General Pattern

```python
def recursive_function(parameters):
    if base_condition:
        return

    # perform operation
    recursive_function(updated_parameters)
```

The recursion continues until the **base condition** is satisfied.

---

# 2️⃣ Example 1: Print Value X, N Times

### Problem

Given two numbers **X** and **N**, print **X exactly N times**.

### Python Implementation

```python
def print_x_n_times(x, n):
    if n == 0:
        return   # Base case

    print(x, end=" ")
    print_x_n_times(x, n - 1)

x = 4
n = 5
print_x_n_times(x, n)
```

### Output

```
4 4 4 4 4
```

### Explanation

Each recursive call:

1. Prints `x`
2. Decreases `n` by `1`
3. Stops when `n == 0`

---

# 3️⃣ Example 2: Print Numbers from 1 to N

This can be implemented using **Head Recursion** or **Tail Recursion**.

---

# Head Recursion (Work After Recursive Call)

In head recursion, the **recursive call happens first** and work happens later.

### Python Implementation

```python
def print1ToN(n):
    if n == 0:
        return

    print1ToN(n - 1)
    print(n, end=" ")

print1ToN(5)
```

### Output

```
1 2 3 4 5
```

### Explanation

The function keeps calling itself until `n = 0`.
During **stack unwinding**, numbers are printed.

---

# Tail Recursion (Work Before Recursive Call)

In tail recursion, the **work happens before the recursive call**.

To print **1 to N**, we introduce a parameter `i`.

### Python Implementation

```python
def print_1_to_n(i, n):
    if i > n:
        return

    print(i, end=" ")
    print_1_to_n(i + 1, n)

n = 5
print_1_to_n(1, n)
```

### Output

```
1 2 3 4 5
```

---

# 4️⃣ Example 3: Print Numbers from N to 1

---

# Using Tail Recursion

Work happens **before recursion**, producing decreasing order.

### Python Implementation

```python
def printNto1(n):
    if n == 0:
        return

    print(n, end=" ")
    printNto1(n - 1)

printNto1(5)
```

### Output

```
5 4 3 2 1
```

### Explanation

Each call:

1. Prints current `n`
2. Decreases `n`
3. Recursively calls until `n = 0`

---

# Using Head Recursion

To print **N to 1**, we introduce an index `i`.

### Python Implementation

```python
def printNto1(i, n):
    if i > n:
        return

    printNto1(i + 1, n)
    print(i, end=" ")

printNto1(1, 5)
```

### Output

```
5 4 3 2 1
```

### Explanation

1. Function recursively increases `i`
2. When recursion returns, values are printed
3. Output appears in **reverse order**

---

# 5️⃣ Head Recursion vs Tail Recursion

| Aspect          | Head Recursion                | Tail Recursion              |
| --------------- | ----------------------------- | --------------------------- |
| Execution Order | Recursive call happens first  | Work happens first          |
| Stack Behavior  | Work done during stack unwind | Work done during call       |
| Loop Conversion | Harder to convert to loops    | Easy to convert to loops    |
| Optimization    | Difficult for compiler        | Can be optimized            |
| Common Uses     | Tree traversal, backtracking  | Iterative-like computations |

---



# 1️⃣2️⃣ When to Use Recursion (Important for Interviews)

Recursion is commonly used in:

### Tree Problems

* Tree Traversals
* DFS

### Backtracking

* N Queens
* Sudoku Solver
* Subsets
* Permutations

### Divide and Conquer

* Merge Sort
* Quick Sort
* Binary Search

### Dynamic Programming

* Fibonacci
* Knapsack

---

# 🔑 FAANG Interview Tips

### Always Check

1️⃣ **Base Case**
2️⃣ **Recursive Relation**
3️⃣ **Stack Depth**
4️⃣ **Time Complexity**

---

### Common Recursion Interview Problems

* Factorial
* Fibonacci
* Reverse a string
* Generate subsets
* Generate permutations
* Binary tree traversal
* N Queens
* Tower of Hanoi

---

# 🚀 Key Takeaways

✔ Recursion solves problems by **breaking them into smaller subproblems**
✔ Every recursive function must have a **base case**
✔ Recursive calls use the **call stack**
✔ Time complexity depends on **number of recursive calls**
✔ Space complexity depends on **recursion depth**

---

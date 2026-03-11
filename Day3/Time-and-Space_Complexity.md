# Understanding Time and Space Complexity

Time and Space Complexity are fundamental concepts in **Data Structures and Algorithms (DSA)**. They help measure the **efficiency of an algorithm** and are heavily tested in **technical interviews at top tech companies**.

---

# 1. What is Time Complexity?

**Time Complexity** measures how the **execution time of an algorithm grows with input size (N)**.

Instead of measuring actual time (seconds), we measure **growth rate**.

Why?

Because execution time depends on:

* Hardware
* Programming language
* System environment

So we use **asymptotic analysis**.

---

# 2. Big-O Notation

**Big-O Notation** represents the **upper bound (worst-case scenario)** of an algorithm.

It shows how the runtime increases as input size increases.

Common complexities:

| Complexity | Name         | Example                    |
| ---------- | ------------ | -------------------------- |
| O(1)       | Constant     | Accessing an array element |
| O(log N)   | Logarithmic  | Binary Search              |
| O(N)       | Linear       | Traversing an array        |
| O(N log N) | Linearithmic | Merge Sort                 |
| O(N²)      | Quadratic    | Nested loops               |

---

# 3. Rules for Calculating Time Complexity

### 1️⃣ Ignore Constants

```
O(5) → O(1)
O(2N) → O(N)
```

Constants do not affect scalability.

---

### 2️⃣ Focus on Growth Rate

We only care about how the algorithm behaves when **N becomes very large**.

Example:

```
O(N + 100) → O(N)
```

---

### 3️⃣ Always Consider Worst Case

Worst case gives the **maximum running time**.

Example:

Searching in an array

```
for (int i = 0; i < N; i++) {
    if (arr[i] == target)
        break;
}
```

Best Case → **O(1)**
Worst Case → **O(N)**

In interviews, we usually discuss the **worst case**.

---

# 4. Common Time Complexity Examples

### O(1) – Constant Time

```
int sum = a + b;
```

Execution time does not depend on input size.

---

### O(N) – Linear Time

```
for (int i = 0; i < N; i++) {
    // operation
}
```

Loop runs **N times**.

---

### O(N²) – Quadratic Time

```
for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
        // operation
    }
}
```

Total operations = **N × N = N²**

---

### O(log N) – Logarithmic Time

```
for (int i = 1; i < N; i = i * 2) {
    // operation
}
```

Input size **reduces exponentially**.

Example:
Binary Search.

---

# 5. Other Complexity Notations

Apart from Big-O:

| Notation  | Meaning      |
| --------- | ------------ |
| Big-O (O) | Worst Case   |
| Theta (Θ) | Average Case |
| Omega (Ω) | Best Case    |

In interviews, **Big-O is most commonly used**.

---

# 6. What is Space Complexity?

**Space Complexity** measures how much **memory an algorithm uses**.

It depends on:

* Variables
* Data structures
* Function calls
* Recursion stack

---

# 7. Types of Space Complexity

### 1️⃣ Input Space

Memory used by input data.

Example:

```
int arr[N];
```

Space = **O(N)**

---

### 2️⃣ Auxiliary Space

Extra memory used by the algorithm.

Example:

```
int temp;
```

Space = **O(1)**

---

# 8. Space Complexity Examples

### Array

```
int arr[N];
```

Space Complexity = **O(N)**

---

### Recursive Function

If recursion depth = **N**

Space Complexity = **O(N)** due to **call stack**.

---

# 9. Key Interview Takeaways

✔ Focus on **growth rate, not actual time**
✔ Ignore **constants and smaller terms**
✔ Analyze **worst-case complexity**
✔ Understand common complexities:

* O(1)
* O(log N)
* O(N)
* O(N log N)
* O(N²)

✔ Optimize both **time and space**

---

# Conclusion

Understanding **Time and Space Complexity** helps in:

* Writing efficient algorithms
* Comparing different approaches
* Solving problems in technical interviews
* Building scalable software systems

Mastering these concepts is essential for **FAANG-level coding interviews**.


---

# 📚 Arrays – Quick Revision Notes

## 1️⃣ What is an Array

* An **Array** is a **linear data structure** used to store multiple elements.
* All elements in an array must be of the **same data type** (int, float, double, etc.).
* Elements are stored in a **continuous (contiguous) memory location**.
* Each element is accessed using an **index**.

---

## 2️⃣ Indexing in Arrays

* Array indexing **starts from 0**.
* First element → `arr[0]`
* Last element → `arr[n-1]` (where `n` = size of array)

Example:

```python
arr = [4, 2, 3]

print(arr[0])  # 4
print(arr[1])  # 2
print(arr[2])  # 3
```

---

## 3️⃣ Array Traversal

Traversal means **visiting each element of the array one by one**.

Usually done using **loops**.

Example:

```python
arr = [4, 2, 3]

for i in arr:
    print(i)
```

Output

```
4
2
3
```

⚠️ Always ensure traversal **does not exceed array bounds**.

---

## 4️⃣ Memory Structure of Arrays

* Arrays are stored in **contiguous memory locations**.
* This allows **fast access using index**.
* Memory is **allocated during array creation**.

Important Point:

```
Arrays have FIXED size
```

Size **cannot change during runtime**.

---

## 5️⃣ Two-Dimensional Arrays (2D Arrays)

A **2D array** is an **array of arrays**.

Used to represent:

* **Matrices**
* **Tables**
* **Grids**

Example:

```python
arr = [
    [1, 2, 3],
    [4, 5, 6]
]
```

---

## 6️⃣ Traversing a 2D Array

```python
for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()
```

Output

```
1 2 3
4 5 6
```

---

## 7️⃣ Common Array Problems

Practice these basic array operations:

* Sum of array elements
* Count odd numbers in array
* Reverse an array
* Check if the array is sorted

---

## 8️⃣ Key Advantages of Arrays

✔ Fast element access using index
✔ Simple and easy to use
✔ Efficient memory usage
✔ Useful for implementing other data structures

---

## 🔑 Final Summary

* Arrays store **same type elements**
* **Index-based access**
* **Contiguous memory allocation**
* **Fixed size**
* Supports **1D and 2D structures**

---


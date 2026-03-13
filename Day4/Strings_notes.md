
## 1. What is a String

* A **string** is a **sequence of characters** used to represent text.
* Strings are a **fundamental data type** in almost every programming language.
* They allow programs to **store and manipulate textual data efficiently**.

---

# 2. String Implementation in Different Languages

### Java

```java
String str = "Hello";
```

### C++

```cpp
std::string str = "Hello";
```

### Python

```python
str = "Hello"
```

### JavaScript

```javascript
let str = "Hello";
```

Most languages provide **built-in libraries or classes** to work with strings.

---

# 3. Mutability of Strings

## C++ Strings (Mutable)

* Strings can be **modified after creation**.

Example:

```cpp
std::string s = "taj";
s = s + 'j';   // "tajj"
```

Meaning:

* The original string **can change**.

---

## Java Strings (Immutable)

* Strings **cannot be changed after creation**.
* Any modification creates a **new string object**.

Example:

```java
String s = "raj";
s = s + 'j';   // "rajj"
```

Meaning:

* `"raj"` remains unchanged.
* `"rajj"` is a **new string object**.

---

# 4. Accessing Characters in a String

### Java

Use `charAt()` method.

```java
String s = "raj";
char c = s.charAt(1);   // 'a'
```

### C++

Use **index operator []**

```cpp
std::string s = "raj";
char c = s[1];   // 'a'
```

Key point:

* **Strings use 0-based indexing**.

Example:

| Index | Character |
| ----- | --------- |
| 0     | r         |
| 1     | a         |
| 2     | j         |

---

# 5. Character Arrays

A **character array** stores characters in **contiguous memory locations**.

Example in C:

```c
char str[] = "Hello";
```

Important points:

* Stored as a sequence of characters
* Ends with **null character `'\0'`**
* Used in **low-level programming**

Example memory:

```text
H e l l o \0
```

---

# 6. String vs Character

| Type      | Representation |
| --------- | -------------- |
| String    | "Hello"        |
| Character | 'H'            |

Examples:

```java
String s = "Hello";
char c = 'H';
```

Key Difference:

* **String → multiple characters**
* **Character → single character**

---

# 7. Traversing a String

Traversing means **iterating through each character**.

Example:

```java
for(int i = 0; i < s.length(); i++){
    char c = s.charAt(i);
}
```

Purpose:

* Process each character
* Perform operations like:

  * counting
  * searching
  * modifying

---

# 8. Character Data Type

Characters correspond to **ASCII values**.

Important ASCII ranges:

| Character | ASCII Value |
| --------- | ----------- |
| A-Z       | 65 – 90     |
| a-z       | 97 – 122    |

Example:

```cpp
int freq[256] = {0};
freq['c']++;    // ASCII value 99
```

Used for:

* **Character frequency counting**
* **Hashing techniques**

---

# 9. Substrings

A **substring** is a **part of a string**.

Example:

```
string = "string"
```

Possible substrings:

```
str
ring
tri
rin
```

---

# 10. Substring in C++

Use `substr(start_index, length)`.

Example:

```cpp
std::string s = "string";
std::string sub = s.substr(2,3);
```

Output:

```
"rin"
```

Explanation:

* Start index = **2**
* Length = **3**

---

# 11. Substring in Java

Use `substring(start, end)`.

Example:

```java
String s = "string";
String sub = s.substring(2,4);
```

Output:

```
"ri"
```

Explanation:

* Start index = **2**
* End index = **4 (exclusive)**

---

# 12. Difference Between C++ and Java Substring

| Language | Syntax               | Ending Index        |
| -------- | -------------------- | ------------------- |
| C++      | substr(start,length) | length based        |
| Java     | substring(start,end) | end index exclusive |

Example:

```
C++  → substr(2,3) → "rin"
Java → substring(2,4) → "ri"
```

---

# 13. Key Interview Points

* Strings are **sequences of characters**.
* **C++ strings are mutable**, **Java strings are immutable**.
* Characters are accessed using **indexing**.
* Character arrays store **characters in contiguous memory**.
* ASCII values help in **character operations and hashing**.
* Substrings extract **portions of strings**.
* Different languages use **different substring methods**.

---


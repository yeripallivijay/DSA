
---

# 🐍 Python Basics for DSA & Coding Interviews

> Python is one of the most popular languages for **Data Structures, Algorithms, AI, and Backend Development**.

Used by companies like **Google, Netflix, Instagram, and OpenAI.

---

# 🚀 Why Python?

Python is known for:

✅ Simple syntax
✅ Fast development
✅ Huge ecosystem
✅ Powerful libraries

Example:

```python
print("Hello World")
```

Compared to other languages, Python is **very readable and beginner-friendly**.

---

# 🖥️ Python Interpreter

Python is an **interpreted language**.

Execution flow:

```
Python Code
     ↓
Python Interpreter
     ↓
Bytecode
     ↓
Python Virtual Machine
     ↓
Output
```

---

# ⚙️ Running Python Code

### Interactive Mode (Python Shell)

Run small commands instantly.

```python
print(2 + 3)
```

Output

```
5
```

---

### Script Mode

Create a file:

```
hello.py
```

Run it:

```
python hello.py
```

---

# 🧾 Variables

Variables store data.

```python
name = "Raj"
age = 25
city = "Mumbai"
```

Example

```python
print(name, age)
```

Rules:

* Must start with **letter or underscore**
* No spaces
* Case sensitive

---

# 🔤 Strings (Text Data)

Strings are characters inside quotes.

```python
name = "Raj"
```

### Operations

```python
print("Hello " + name)
print("Hello " * 3)
print(len(name))
```

---

# 🔑 Escape Characters

| Escape | Meaning      |
| ------ | ------------ |
| `\n`   | New line     |
| `\t`   | Tab          |
| `\"`   | Double quote |
| `\\`   | Backslash    |

Example

```python
print("Line1\nLine2")
```

---

# ⭐ f-Strings (Recommended)

Best way to insert variables in strings.

```python
name = "Raj"
age = 25

print(f"My name is {name} and I am {age}")
```

---

# 🔧 String Methods

```python
text = "  Hello World  "

text.upper()
text.lower()
text.strip()
text.replace("World","Python")
text.find("World")
```

---

# 🔢 Numbers & Operators

| Operator | Meaning        |
| -------- | -------------- |
| `+`      | Addition       |
| `-`      | Subtraction    |
| `*`      | Multiplication |
| `/`      | Division       |
| `//`     | Floor Division |
| `%`      | Modulus        |
| `**`     | Power          |

Example

```python
print(2 ** 3)
```

Output

```
8
```

---

# 🔄 Type Conversion

Convert between types.

```python
age = "25"

age_num = int(age)

price = 99.9
price_str = str(price)
```

---

# ⚖️ Comparison Operators

Return **True or False**.

| Operator | Meaning          |
| -------- | ---------------- |
| `==`     | Equal            |
| `!=`     | Not equal        |
| `>`      | Greater          |
| `<`      | Less             |
| `>=`     | Greater or equal |
| `<=`     | Less or equal    |

Example

```python
print(5 > 3)
```

---

# 🧠 Conditional Statements

Used for **decision making**.

```python
marks = 85

if marks >= 90:
    print("Grade A")

elif marks >= 80:
    print("Grade B")

else:
    print("Grade C")
```

---

# ⚡ Ternary Operator

Short version of if-else.

```python
age = 20
status = "Adult" if age >= 18 else "Minor"
```

---

# 🔗 Logical Operators

| Operator | Meaning              |
| -------- | -------------------- |
| `and`    | Both conditions true |
| `or`     | At least one true    |
| `not`    | Reverse condition    |

Example

```python
if age >= 18 and has_id:
    print("Allowed")
```

---

# 🔁 For Loop

Used to repeat actions.

```python
for i in range(5):
    print(i)
```

Loop through list:

```python
for fruit in ["apple","banana"]:
    print(fruit)
```

---

# 🔁 While Loop

Runs while condition is True.

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

---

# ⚠️ Infinite Loop

```python
while True:
    print("Running forever")
```

Stop using:

```
Ctrl + C
```

---

# ⚙️ Functions

Functions allow **code reuse**.

```python
def greet(name):
    print(f"Hello {name}")

greet("Raj")
```

---

# 🔹 Default Arguments

```python
def country(name="India"):
    print(name)

country()
```

Output

```
India
```

---

# 🔹 Keyword Arguments

```python
def my_func(c1,c2,c3):
    print(c3)

my_func(c1="A",c2="B",c3="C")
```

---

# 🔹 *args (Variable Arguments)

```python
def my_func(*kids):
    print(kids[0])

my_func("A","B","C")
```

---

# 🧪 Practice Exercises

1️⃣ Print your name and age
2️⃣ Build a simple calculator
3️⃣ Check if number is even or odd
4️⃣ Print numbers 1-10
5️⃣ Write a greeting function

---

# ⚠️ Common Beginner Mistakes

❌ Forgetting `:` in `if` or loops
❌ Wrong indentation
❌ Misspelled variable names
❌ Using `=` instead of `==`

---

# 🎯 Key Takeaways

✔ Python syntax is simple
✔ Variables store data
✔ Strings handle text
✔ Loops automate repetition
✔ Functions reuse code

---

# 📌 Final Advice

Programming skill grows with **consistent practice**.

> “The journey of a thousand miles begins with a single step.”

Keep coding 🚀

---
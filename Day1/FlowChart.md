# Lecture 2: Flowcharts and Logical Thinking – Important Points

## Why Flowcharts Before Code

* **Golden Rule:** Think Before We Code.
* **Problem (in English) → Flowchart (Visual Plan) → Code (Instructions)**
* Makes us **think clearly**
* Shows **mistakes BEFORE writing code**
* Easy to **explain to others**
* **Language doesn't matter** (same flowchart works for Python, Java, C++)
* **Visual = Easier to understand**

---

# What Is a Flowchart

**Definition:**
A flowchart is a **diagram that shows the steps to solve a problem**.

It uses:

* **Boxes (to show actions)**
* **Diamonds (to show decisions/questions)**
* **Arrows (to show direction/flow)**

It is **a map for our program**.

---

# Flowchart Symbols

## 1. START / END (Oval)

Meaning:

* **Beginning or end of the process**

Used for:

* **Start**
* **Stop / End**

Every flowchart **starts with START and ends with END**.

---

## 2. PROCESS (Rectangle)

Meaning:

* **Doing something / Performing an action**

Used for:

* Calculations
* Assigning values
* Any action step

Examples:

* Calculate total
* Add numbers
* Print message

---

## 3. DECISION (Diamond)

Meaning:

* **Asking a question / Making a decision**

Used for:

* Yes / No questions
* Checking conditions
* If-else decisions

Important:

* **Diamond always has two exits**

  * YES / TRUE
  * NO / FALSE

---

## 4. INPUT / OUTPUT (Parallelogram)

Meaning:

* **Getting data or displaying data**

Used for:

* Input from user
* Output to user

Examples:

* Read input
* Print result
* Show message

---

## 5. ARROWS (Flow Lines)

Meaning:

* **Direction of flow**
* **Shows the order of steps**

Flow usually goes:

* **Top to bottom**
* **Left to right**

---

# Example Flowchart Logic

## Simple Addition Program

START → Read a → Read b → sum = a + b → Print sum → END

Type:

* **Sequential flowchart**

---

## Check Even or Odd

START → Read n → remainder = n % 2 → Is remainder == 0?

YES → Print "Even"
NO → Print "Odd"

→ END

Type:

* **Decision flowchart**

---

## Maximum of Two Numbers

START → Read a → Read b → Is a > b?

YES → Print a
NO → Print b

→ END

---

# Common Flowchart Patterns

## 1. Sequential

Steps happen **one after another**.

Example:
START → Read length → Read breadth → area = length * breadth → Print area → END

---

## 2. Conditional

Contains **decision (diamond)**.

Example:
START → Read age → Is age ≥ 18?

YES → Print "Eligible"
NO → Print "Not eligible"

→ END

---

## 3. Loop

Steps **repeat multiple times**.

Example:
START → i = 1 → Is i ≤ 10?

YES → Print i → i = i + 1 → go back
NO → END

---

# Problem-Solving Approach (5 Steps)

1. **Understand the Problem**

   * What is the input?
   * What is the output?
   * What needs to be done?

2. **Break into Smaller Steps**

3. **Draw the Flowchart**

4. **Verify with Examples**

5. **Then Write Code**

Important rule:
**Flowchart first, code second.**

---

# Tools for Drawing Flowcharts

## Pen and Paper

* Fast
* No software needed
* Easy to erase and redraw
* Good for practice

---

## Draw.io / diagrams.net

* Free online tool
* Drag and drop symbols
* Clean and professional

---

# Flowcharts vs Pseudocode

| Aspect        | Flowchart       | Pseudocode    |
| ------------- | --------------- | ------------- |
| Format        | Visual          | Text          |
| Best for      | Visual learners | Text thinkers |
| Showing flow  | Excellent       | Good          |
| Showing logic | Good            | Excellent     |

Use cases:

* **Complex decisions → Flowchart**
* **Complex calculations → Pseudocode**

---

# Common Mistakes in Flowcharts

### Missing START or END

Every flowchart **must have START and END**.

### Unlabeled Arrows

Decision arrows must be labeled **YES / NO**.

### Dead End

Every path must **reach END**.

### No Flow Direction

Use **arrows showing clear flow**.

---

# Why Companies Value Flowcharts

* Shows **clear thinking**
* Helps in **team communication**
* **Reduces errors before coding**
* **Saves time and money**

---

# Most Important Points

* **Think before coding**
* **Draw flowchart first**
* **Use correct symbols**
* **Decision = diamond**
* **Process = rectangle**
* **Input/Output = parallelogram**
* **Every flowchart must have START and END**
* **Label decision paths YES / NO**
* **Test with examples before writing code**

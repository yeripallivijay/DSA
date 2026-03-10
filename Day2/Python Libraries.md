
# 🐍 Python Libraries for DSA & Coding Interviews

> Essential Python toolkit for solving **Data Structures & Algorithms problems** efficiently.
> Similar to **C++ STL** and **Java Collections**.

## 🚀 Why These Libraries Matter

* ⏱️ Save time with optimized built-in code
* 💻 Expected knowledge in coding interviews
* 📈 Simplifies complex DSA problems
* 🧠 Used in real industry codebases

---

# 1️⃣ Built-in Functions (Must Know)

## Sorting

```python
arr = [3,1,4,1,5]

sorted(arr)                 # [1,1,3,4,5]
sorted(arr, reverse=True)   # [5,4,3,1,1]

sorted(arr, key=abs)

arr.sort()                  # In-place sorting
```

### Custom Sorting

```python
words = ["apple","pie","banana"]

sorted(words, key=len)
```

---

## Min / Max

```python
min([3,1,4,1,5])
max([3,1,4,1,5])
```

Custom key:

```python
min(words, key=len)
```

---

## Sum / Product

```python
sum([1,2,3,4])

import math
math.prod([2,3,4])
```

---

## Any / All

```python
any([False, True, False])   # True
all([True, True, True])     # True
```

---

## Enumerate

Used to access **index + value together**

```python
for i,val in enumerate([10,20,30]):
    print(i,val)
```

Output

```
0 10
1 20
2 30
```

---

## Zip

Combine multiple lists.

```python
list(zip([1,2],[3,4]))
```

Output

```
[(1,3),(2,4)]
```

---

## Range

```python
range(5)
range(1,5)
range(0,10,2)
```

---

# 2️⃣ Collections Module (Most Important for Interviews)

```python
from collections import deque, Counter, defaultdict, OrderedDict
```

---

# 🔹 deque (Double Ended Queue)

Fast **O(1)** insertion/removal from both ends.

```python
from collections import deque

dq = deque([1,2,3])

dq.append(4)
dq.appendleft(0)

dq.pop()
dq.popleft()
```

### Used In

* BFS
* Sliding window
* Queue/Stack

---

# 🔹 Counter (Frequency Counter)

```python
from collections import Counter

c = Counter([1,2,2,3,3,3])

c[2]
c.most_common(2)
```

Example Output

```
[(3,3),(2,2)]
```

### Used In

* Frequency problems
* Top K elements
* Anagrams

---

# 🔹 defaultdict

Avoids **KeyError**

```python
from collections import defaultdict

d = defaultdict(int)

d['a'] += 1
```

For grouping

```python
groups = defaultdict(list)

groups["fruit"].append("apple")
```

### Used In

* Graphs
* Grouping
* Counting

---

# 🔹 OrderedDict

Maintains insertion order.

```python
from collections import OrderedDict

od = OrderedDict()

od['a']=1
od['b']=2

od.move_to_end('a')
od.popitem(last=False)
```

### Used In

* LRU Cache

---

# 3️⃣ Heapq (Priority Queue)

```python
import heapq
```

Python uses **Min Heap**

```python
heap = []

heapq.heappush(heap,3)
heapq.heappush(heap,1)

heapq.heappop(heap)
```

### Convert List to Heap

```python
heapq.heapify(arr)
```

### K Largest Elements

```python
heapq.nlargest(3,arr)
```

---

### Max Heap Trick

```python
heapq.heappush(heap,-10)

max_val = -heapq.heappop(heap)
```

---

# 4️⃣ Bisect (Binary Search)

```python
import bisect
```

Array must be **sorted**

```python
arr = [1,3,3,5]

bisect.bisect_left(arr,3)
bisect.bisect_right(arr,3)
```

Insert while maintaining sorted order

```python
bisect.insort(arr,4)
```

---

# 5️⃣ Itertools (Advanced Iteration)

```python
import itertools
```

### Combinations

```python
itertools.combinations([1,2,3],2)
```

Output

```
(1,2),(1,3),(2,3)
```

### Permutations

```python
itertools.permutations([1,2],2)
```

### Cartesian Product

```python
itertools.product([1,2],[3,4])
```

---

# 6️⃣ Functools

```python
import functools
```

## LRU Cache (Important for DP)

```python
@functools.lru_cache(None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1)+fib(n-2)
```

---

## Reduce

```python
from functools import reduce

reduce(lambda x,y:x+y,[1,2,3])
```

---

# 7️⃣ Math Module

```python
import math
```

Common interview functions

```python
math.gcd(48,18)
math.lcm(12,8)

math.sqrt(16)

math.factorial(5)

math.ceil(4.3)
math.floor(4.7)
```

---

# 8️⃣ Common DSA Patterns in Python

---

# 🔹 Two Sum

```python
seen = {}

for i,num in enumerate(nums):
    if target-num in seen:
        return [seen[target-num],i]

    seen[num]=i
```

---

# 🔹 Group Anagrams

```python
from collections import defaultdict

groups = defaultdict(list)

for s in strs:
    groups[''.join(sorted(s))].append(s)

return list(groups.values())
```

---

# 🔹 Top K Frequent Elements

```python
from collections import Counter

counter = Counter(nums)

counter.most_common(k)
```

---

# 🔹 Sliding Window

```python
from collections import deque

dq = deque()

dq.append(i)
dq.pop()
dq.popleft()
```

---

# 📊 Which Library to Use?

| Problem Type         | Library     |
| -------------------- | ----------- |
| Frequency counting   | Counter     |
| BFS / Sliding window | deque       |
| Graph building       | defaultdict |
| Priority queue       | heapq       |
| Binary search        | bisect      |
| Combinations         | itertools   |
| Memoization          | functools   |

---

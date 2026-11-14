# 🐍 Python Basics Master Study Guide
*Inspired by W3Schools & Modern Python Documentation standards.*
*Compiled as a comprehensive, student-friendly reference handbook.*

---

## 📌 Section 1: Python Variables
Variables are simply **containers for storing data values**. Python has no command for declaring a variable; a variable is created the moment you first assign a value to it.

* **সহজ ভাষায় (Simple Explanation):** Variable হচ্ছে একটা **মেমোরি বক্স বা পাত্রের মতো**, যার ভেতরে আমরা কোনো ডাটা (যেমন: নাম, নাম্বার) রেখে দিই। পরবর্তীতে যখনই ওই ডাটা দরকার হয়, আমরা বক্সের নাম (Variable Name) ধরে ডাক দিলেই ডাটা চলে আসে।
* **Code Example:**
  ```python
  x = 5          # x একটি পাত্র যেখানে 5 জমা আছে
  name = "John"  # name একটি পাত্র যেখানে text জমা আছে
  print(x)
  print(name)
  ```
* **⚠️ Rules for Students (মনে রাখার নিয়ম):**
  * Variable name অবশ্যই letter অথবা underscore (`_`) দিয়ে শুরু হতে হবে।
  * কখনো **নাম্বার দিয়ে শুরু করা যাবে না** (e.g., `1myvar` ভুল)।
  * এটি **Case-sensitive** (অর্থাৎ `a` এবং `A` দুটি আলাদা variable)।

---

## 📌 Section 2: Python Lists
A **Python List** is a versatile, built-in data type used to store multiple items sequentially in a single variable. Lists are defined by placing comma-separated values inside **square brackets `[]`**.

* **সহজ ভাষায় (Simple Explanation):** মনে করো তোমার কাছে একটা বাজারের থলে (Bag) আছে। সেই থলেতে তুমি একসাথে আলু, পেঁয়াজ, ডিম অনেক কিছু রাখতে পারো। Python-এ List হলো সেই থলের মতো, যেখানে একটা মাত্র Variable-এর ভেতর আমরা **একসাথে অনেকগুলো ডাটা** সাজিয়ে রাখতে পারি।

### 🧱 3 Core Characteristics of List Items
1. **Ordered (ক্রমাবদ্ধ):** Lists maintain a defined order. When you add a new item using `.append()`, it is **always placed at the absolute end**.
2. **Changeable / Mutable (পরিবর্তনযোগ্য):** You can freely modify, add, or remove items in a list after it has been created using its index.
3. **Allow Duplicates (একই ডাটা বারবার নেওয়া যায়):** Since lists are indexed, they can contain multiple items with the exact same value.

### 🗺️ Index Mapping Visual
```text
 Positive Index ➡️     0          1          2          3          4
                 ["apple",  "banana",  "cherry",  "orange",    "kiwi"]
Negative Index ⬅️    -5         -4         -3         -2         -1
```

### ✂️ Range of Indexes (Slicing)
Slicing allows you to extract a specific chunk (sub-list) from a larger list.
* **Syntax:** `list[start : end]`
* **The Golden Rule:** The `start` index is **included**, but the `end` index is **excluded** (up to, but not including).

### 🛠️ Modifying & Dynamic Resizing
* **List Grows (📈):** `thislist[1:2] = ["blackcurrant", "watermelon"]` (1 item replaced by 2).
* **List Shrinks (📉):** `thislist[1:3] = ["watermelon"]` (2 items replaced by 1).

### 📊 Master Table: 7 Essential Built-in List Methods
| Method Name | Operation Target | Execution Purpose | Return Value / Side Effect |
| :--- | :--- | :--- | :--- |
| **`append(x)`** | Value | Appends an item to the **very end** of the list. | Modifies list in place, returns `None`. |
| **`insert(i, x)`** | Index + Value | Injects an item at a **specific index position**. | Shifts right-side items, returns `None`. |
| **`extend(iterable)`** | Collection / Iterable | Appends **all elements** from another iterable. | Unpacks elements to the end, returns `None`. |
| **`remove(x)`** | Value | Removes the **first instance** matching the value. | Raises `ValueError` if the item is missing. |
| **`pop(i)`** | Index | Removes and **returns** item at specified index. | If index is omitted, pops the **last item**. |
| **`clear()`** | Structural Interior | **Wipes out all items**, leaving an empty container. | Leaves an empty structure `[]`. |
| **`len(list)`** | Global Container | Measures and returns the **total item count**. | Returns an **Integer**. |

---

## 📌 Section 3: List Comprehension
List comprehension provides a shorter and elegant way to create a new list from an existing iterable.

* **Formula:** `newlist = [expression for item in iterable if condition]`
* **Conditional Expression Inside (if-else):** When using an `else`, the conditional block moves to the front:
  `newlist = [x if x != "banana" else "orange" for x in fruits]`

---

## 📌 Section 4: Python Tuples
A **Python Tuple** is an immutable collection type wrapped in **round brackets `()`**.

* **সহজ ভাষায় (Simple Explanation):** Tuple হলো পাইথনের এমন একটা ডাটা ঝুড়ি, যা তৈরি করার পর আর কখনো তার ভেতরের জিনিসপত্র **বদলানো, যোগ করা বা মুছে ফেলা যায় না**।
* **⚠️ The Single-Item Tuple Trap:** Creating a tuple with a solitary item requires a **trailing comma `,`** (e.g., `thistuple = ("apple",)`). Without it, Python treats it as a standard raw string.

### 🛠️ The "List Bypass" Workaround
To alter a tuple, convert it into a list, change the list, and convert it back into a tuple:
```python
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
```

### 📦 Unpacking Tuples & The Asterisk (`*`)
Extracting stored elements back into variables is called unpacking. If the number of variables is less than the items, add an `*` to capture the rest as a list:
```python
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits  # red becomes a list of the remaining items
```

### 📊 Built-In Tuple Methods
* **`.count(x)`:** Returns the number of times a specified value occurs.
* **`.index(x)`:** Searches for a specified value and returns its first position.

---

## 📊 Summary Comparison: Python Collections
| Collection Type | Ordered? | Changeable? | Allows Duplicates? | Syntax |
| :--- | :--- | :--- | :--- | :--- |
| **List** | ✅ Yes | ✅ Yes | ✅ Yes | `[]` |
| **Tuple** | ✅ Yes | ❌ No | ✅ Yes | `()` |
| **Set** | ❌ No | ❌ *Items unchangeable | ❌ No | `{}` |
| **Dictionary** | ✅ Yes (3.7+) | ✅ Yes | ❌ Keys Only | `{:}` |

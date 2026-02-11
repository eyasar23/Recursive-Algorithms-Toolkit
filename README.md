# 🌀 Recursive Algorithms Toolkit

**A collection of pure recursive algorithms for mathematical analysis and hierarchical data parsing.**

> *"Solving complex parsing and evaluation problems without a single loop."*

## 📖 Project Overview
This repository contains a set of advanced algorithms implemented using **Pure Recursion**. The project adheres to strict constraints: **No Iteration** (`for`/`while` loops are forbidden) and **No Global Variables**. It solves two distinct classes of problems:

1.  **Symbolic Math Analysis:** Evaluating and differentiating composite trigonometric functions.
2.  **Hierarchical Parsing:** Traversing nested directory structures encoded in string formats.

## 📂 File Structure & Functionality

### 📐 Part 1: Trigonometric Engine (`q1` Series)
Handles parsing and calculus of nested trigonometric strings (e.g., `'sin(cos(x))*sin(x)'`).

| File | Function | Logic & Description |
| :--- | :--- | :--- |
| **`q1a.py`** | `calculate(f, x)` | **Evaluator:** Recursively parses the string, handles operator precedence, and computes the value of complex composite functions like $f(g(x))$. |
| **`q1b.py`** | `derivative(f, x)` | **Differentiator:** Calculates the numerical derivative recursively, implementing the **Chain Rule** ($f(g(x))'$) and **Product Rule** automatically. |

### 📂 Part 2: Directory Parser (`q2` Series)
Parses hierarchical file system strings (e.g., `'root[file1(10),subdir[file2(20)]]'`) to extract metadata.

| File | Function | Logic & Description |
| :--- | :--- | :--- |
| **`q2a.py`** | `count_files(dir)` | **Counter:** Traverses the nested string structure to count the total number of files, ignoring directory depth. |
| **`q2b.py`** | `sum_file_sizes(dir)` | **Aggregator:** Recursively extracts file sizes (integers inside `()`) and computes the total storage usage. |
| **`q2c.py`** | `largest_file(dir)` | **Searcher:** Navigates the entire hierarchy to identify and return the name of the file with the largest size. |

## 🛠️ Technical Constraints
This project demonstrates mastery of algorithmic thinking under strict limitations:
* **Pure Recursion:** All logic (traversal, parsing, searching) is built without iteration.
* **Immutable Parsing:** String parsing is handled via slicing and recursive calls, not regex or external libraries.
* **State Management:** All data is passed through function arguments, ensuring thread-safe logic without global state.

## 🚀 Usage Example

```python
# Example for Trigonometry (q1)
from q1a import calculate
print(calculate('sin(cos(x))', 0.7)) 

# Example for Directory Parsing (q2)
from q2a import count_files
fs_string = "root[doc(10),photos[img(20)]]"
print(count_files(fs_string)) # Output: 2

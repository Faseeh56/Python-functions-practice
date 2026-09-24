# 🐍 Python Functions Practice

> Practical Python exercises focused on **functions, reusable logic, and basic data processing** as part of my AI Engineering learning journey.

This repository contains my completed practice work from the **Python Functions** phase of the AI Engineering From Scratch series.

The purpose of these exercises was not to learn Python as a profession, but to develop the programming foundation needed to work confidently with **data, Machine Learning, and AI systems**.

---

## 🎯 What This Repository Represents

The central idea of this week's practice was:

```text
Write logic once
      ↓
Give it a name
      ↓
Reuse it
      ↓
Combine it with data + conditions + loops
      ↓
Build more organized programs
```

The exercises move from simple reusable functions to programs that combine functions with **lists, dictionaries, loops, conditions, and returned values**.

---

## 🧠 Concepts Practiced

This repository covers:

- Defining functions with `def`
- Calling functions
- Parameters
- Arguments
- `return`
- `print()` vs `return`
- Reusable logic
- Functions with lists
- Functions with dictionaries
- Loops inside functions
- Conditions inside functions
- Combining multiple functions in one program
- Basic data processing with reusable logic

---

# 🧩 Practice Programs

## 01 — Movie Night Picker 🎬

**File:** `01_Movie_Night_Picker.py`

A small movie-search utility that receives a list of movies and a requested movie name through a function.

The function:

```python
find_movie(movies, wanted)
```

loops through the movie list, performs a case-insensitive and whitespace-tolerant comparison, and returns either a matching movie message or a “not found” message.

### Concepts

- Function definition
- Parameters and arguments
- `for` loop
- String methods
- Conditional comparison
- `return`

---

## 02 — Student Score Coach 📚

**File:** `02_Student_Score_Coach.py`

A student-performance program built around a list of dictionaries.

The program uses separate functions to:

- check whether a score is considered a high score
- determine a grade
- display student information

Example data:

```python
students = [
    {"name": "Ali", "score": 82},
    {"name": "Sara", "score": 91},
    {"name": "Hamza", "score": 67},
    {"name": "Ayesha", "score": 88}
]
```

The program then loops through the student records and uses the functions to decide which students to display.

### Concepts

- Functions
- Parameters
- `return`
- Lists
- Dictionaries
- Loops
- Conditions
- Reusable decision logic

---

## 03 — AI Result Reporter 🤖

**File:** `03_AI_Result_Reporter.py`

A small AI-inspired program that treats a model result as structured data:

```python
result = {
    "label": "cat",
    "confidence": 0.94,
    "class_id": 3
}
```

The function:

```python
show_result(result)
```

reads the dictionary and produces a readable report.

It also uses the confidence score to decide whether the prediction should be considered confident or low-confidence.

### Concepts

- Functions
- Dictionaries
- Key-based access
- Conditions
- Function parameters
- AI-style structured output

### Why this example matters

AI applications often need to turn structured model output into useful information for another part of a system. This exercise is a small introduction to that pattern.

---

## 04 — Mini Expense Analyzer 💰

**File:** `04_Mini_Expense_Analyzer.py`

A simple expense-analysis program that works with a list of numeric values.

It separates two tasks into reusable functions:

```python
get_total(expenses)
```

and

```python
show_large_expenses(expenses, limit)
```

The first function calculates the total using a loop, while the second filters expenses based on a user-provided limit.

### Concepts

- Functions
- Parameters
- `return`
- Lists
- Loops
- Running totals
- Conditions
- Data filtering
- User input

---

## 05 — Smart Study Dashboard 📊

**File:** `05_Smart_Study_Dashboard.py`

The final program combines multiple concepts into a small study-analysis system.

The data is stored as a list of dictionaries:

```python
courses = [
    {"name": "Python", "score": 88},
    {"name": "Git", "score": 92},
    {"name": "Math", "score": 74},
    {"name": "SQL", "score": 81}
]
```

The program uses functions to:

- identify strong scores
- display course information
- calculate the average score

The main flow combines those functions with iteration through the course records.

### Concepts Combined

```text
List
  ↓
Dictionary
  ↓
Loop
  ↓
Condition
  ↓
Function
  ↓
Return
  ↓
Result
```

This serves as the practical capstone of the week's functions work.

---

# 📂 Repository Structure

```text
Python-functions-practice/
│
├── Output_screenshots/
├── problems/
│
├── 01_Movie_Night_Picker.py
├── 02_Student_Score_Coach.py
├── 03_AI_Result_Reporter.py
├── 04_Mini_Expense_Analyzer.py
└── 05_Smart_Study_Dashboard.py
```

The repository contains separate folders for the **problem material** and **output screenshots**, alongside the five completed Python programs.

---

# 🚀 How to Run

Make sure Python 3 is installed.

Clone the repository:

```bash
git clone https://github.com/Faseeh56/Python-functions-practice.git
```

Move into the repository:

```bash
cd Python-functions-practice
```

Run any program, for example:

```bash
python 01_Movie_Night_Picker.py
```

or:

```bash
python 05_Smart_Study_Dashboard.py
```

---

# 🔍 What I Practiced This Week

The major shift in this week's learning was from writing individual pieces of code to **organizing logic into reusable units**.

```text
Before
------
Write the same logic again
        ↓
Repeated code


After
-----
Create a function
        ↓
Call it whenever needed
```

This makes programs easier to understand, reuse, modify, and combine.

---

# 🤖 Why Functions Matter for AI Engineering

Functions are not an AI technology by themselves, but they are a fundamental engineering tool.

As AI applications become larger, logic is naturally divided into smaller tasks such as:

```text
load_data()
clean_data()
prepare_features()
train_model()
predict()
evaluate()
save_results()
```

The exact functions will change from project to project, but the engineering idea stays the same:

> **Break a larger problem into smaller, reusable pieces of logic.**

This is why functions are an important part of the Python foundation before moving into more serious data and AI work.

---

# 📈 Learning Progress

### Completed

- [x] Basic Python foundations
- [x] Conditions
- [x] Loops
- [x] Lists
- [x] Dictionaries
- [x] Tuples
- [x] Functions
- [x] Parameters & arguments
- [x] Return values
- [x] Functions + data structures
- [x] Basic reusable data-processing logic

### Next Direction

```text
Functions
    ↓
Files / JSON / APIs
    ↓
NumPy
    ↓
Pandas
    ↓
Data Analysis
    ↓
Machine Learning
    ↓
Deep Learning
    ↓
Generative AI
    ↓
AI Systems
```

---

# 💡 Learning Philosophy

> **Learn → Practice → Build → Explain → Document → Showcase**

These programs are intentionally small.

The objective is to become comfortable with the building blocks that will later support much larger systems.

> **We are not learning Python just to learn Python. We are learning the Python that helps us build.**

---

## 👨‍💻 Author

**Faseeh Qamar**

Computer Science Student | AI Engineering Journey

GitHub: [@Faseeh56](https://github.com/Faseeh56)

---

## 🔗 Repository

[Python Functions Practice](https://github.com/Faseeh56/Python-functions-practice)

> **The future is not given. It is engineered.**

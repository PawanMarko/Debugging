# 🐛 Day 13 — Python Debugging

A beginner-level Python practice project focused on **debugging common programming errors** and understanding how to identify and fix bugs in Python code.

## 📌 About

This project was created as part of **Day 13 of my Python learning journey**.

The main goal was to practice debugging by reproducing errors, identifying the cause, and applying fixes to make the programs work correctly.

## 🧠 What I Practiced

### 1. 🔄 Understanding `range()`

Debugged a loop using Python's `range()` function and learned how the start and stop values work.

```python
for i in range(1, 21):
    if i == 20:
        print("you got it")
```

### 2. 🎲 Debugging a Dice Program

Fixed an indexing problem when selecting a random value from a list.

```python
from random import randint

dice_image = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(0, 5)

print(dice_image[dice_num])
```

This helped reinforce the concept that **Python list indexes start from `0`**.

### 3. 💻 Generational Classification

Debugged a program that determines whether a person is a **Millennial, Gen Z, or older** based on their year of birth.

The exercise focused on:

* `if` / `elif` / `else`
* Comparison operators
* Logical operators
* Boundary conditions

### 4. 🚗 Input Validation

Practiced handling invalid numerical input using `try` and `except`.

```python
try:
    age = int(input("How old are you??"))

except ValueError:
    print("Please enter a valid number.")
```

This introduced basic **exception handling** and the `ValueError` exception.

## 🛠️ Concepts Covered

* Python debugging
* `range()`
* Lists and indexing
* `randint()`
* Conditional statements
* Comparison operators
* Logical operators
* User input
* Type conversion
* `try` / `except`
* `ValueError`
* Common programming errors

## ▶️ How to Run

### 1. Make sure Python is installed

Check your Python installation:

```bash
python --version
```

### 2. Clone the repository

```bash
git clone https://github.com/your-username/python-debugging-day-13.git
```

### 3. Navigate to the project folder

```bash
cd python-debugging-day-13
```

### 4. Run the Python file

```bash
python main.py
```

## 📂 Project Structure

```text
python-debugging-day-13/
│
├── main.py
└── README.md
```

## 🎯 Learning Objective

The purpose of this project was not just to make the code run, but to understand **why the bugs occurred and how to identify them**.

Through these exercises, I practiced reading code carefully, finding logical mistakes, and applying appropriate fixes.

## 🚀 Future Improvements

* Add more debugging exercises
* Practice handling different types of exceptions
* Learn to use Python's debugger tools
* Add more complex programs containing multiple bugs
* Improve error messages and input validation

## 👤 Author

**Your Name**

GitHub: `https://github.com/your-username`

---

📚 **Part of my Python learning journey — Day 13**

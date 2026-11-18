# Python for Beginners

A learning repository for Python fundamentals. It holds two practice files, each covering its own set of topics, together with screenshots that show the output of every chapter.

| File | Content |
|------|---------|
| `latihan.py` | Python basics practice: data types, operators, conditions, loops, lists, dictionaries, functions, and classes |
| `python-dasar.py` | Python Basics, 19 chapters from installation to packages |

## Part 1: Practice Topics (`latihan.py`)

- **Variables and Data Types**: integers, floats, strings, and booleans.
- **Operators**: arithmetic, comparison, and logical operators (`and`, `or`, `not`).
- **Conditions**: `if`, `elif`, `else`, and indentation rules.
- **Loops**: `for`, `while`, `break`, and `continue`.
- **Lists and Dictionaries**: indexing, adding, updating, and removing items.
- **Functions**: arguments, `*args`, `**kwargs`, and default values.
- **Classes and Objects**: properties, constructors, and methods.

## Part 2: Python Basics (`python-dasar.py`)

1. Introduction & Python Installation
2. Basic Program Structure
3. Basic Data Types
4. Variables
5. Constants
6. Operators
7. Control Flow
8. Functions
9. List, Tuple, and Set
10. Dictionary
11. Class & Object
12. Encapsulation
13. Inheritance
14. Polymorphism
15. Abstraction
16. Exception Handling
17. File Handling
18. Modules (uses `kalkulator.py`)
19. Packages

## Prerequisites

- Python 3.12 or newer
- Git
- Visual Studio Code (optional, recommended)

## Getting Started

1. Clone the repository:

   ```
   git clone https://github.com/syuketa/python-untuk-pemula.git
   cd python-untuk-pemula
   ```

2. Create and activate a virtual environment (Windows PowerShell):

   ```
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

   If PowerShell reports an *execution policy* error, run this once:

   ```
   Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
   ```

3. Install the dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Run a program:

   ```
   python latihan.py
   python python-dasar.py
   ```

Both programs print their output from top to bottom, so the output of earlier chapters appears first.

## Project Structure

```
python-untuk-pemula/
├── screenshots/        # execution screenshots for every chapter
├── kalkulator.py       # module used in chapter 18 of Part 2
├── latihan.py          # Part 1 source code
├── python-dasar.py     # Part 2 source code
├── requirements.txt    # dependency list
├── .gitignore
└── README.md
```

Chapter 17 of Part 2 creates a file named `catatan.txt` when it runs. The file is generated automatically and should not be committed.

## Commit Convention

Every chapter is committed separately and pushed right after it is finished. Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/), for example:

```
feat(dasar): implement dictionary
feat(dasar): add function examples
docs: update README
```

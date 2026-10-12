"""NAVTTC AI/ML Program - Week 1: Tasks 1-19 and 21-25

How to run:
    python week1_tasks.py          show a menu and pick a task
    python week1_tasks.py 1          run one task (here: task 1)
    python week1_tasks.py all      run every task in this file

Requires: standard library only (Task 1 only checks for torch/tensorflow)
Tasks that ask you to type something: 4, 5, 10
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def task_01():
    """Task 1: Installation check"""
    import importlib.metadata as md
    import os
    import shutil

    print("Python  :", sys.version.split()[0], "at", sys.executable)
    conda = os.environ.get("CONDA_PREFIX") or "anaconda" in sys.version.lower()
    print("Anaconda:", "detected" if conda else "not detected in this environment")
    for pkg in ("torch", "tensorflow"):
        try:
            print(f"{pkg:<8}: {md.version(pkg)}")
        except md.PackageNotFoundError:
            print(f"{pkg:<8}: NOT installed")
    print("VS Code :", "found" if shutil.which("code") else "'code' command not found")
    print("PyCharm :", "found" if shutil.which("pycharm") or shutil.which("pycharm64") else "command not found (may still be installed)")


def task_02():
    """Task 2: Linux commands practice"""
    print("Linux commands run in a terminal (Linux, WSL or macOS), not inside Python.")
    print("Practice each one there. Reference list:\n")
    commands = [
        ("pwd", "Print working directory — shows your current folder path", "pwd"),
        ("cd", "Change directory — move into a folder", "cd Documents"),
        ("ls", "List files and folders in current directory", "ls -la"),
        ("mkdir", "Make a new directory", "mkdir my_folder"),
        ("rm", "Remove a file", "rm file.txt"),
        ("rmdir", "Remove an empty directory", "rmdir my_folder"),
        ("cp", "Copy a file to another location", "cp a.txt b.txt"),
        ("mv", "Move or rename a file", "mv old.txt new.txt"),
        ("touch", "Create an empty file", "touch notes.txt"),
        ("cat", "Print entire file content to terminal", "cat file.txt"),
        ("more", "View file content one screen at a time", "more file.txt"),
        ("less", "Like more, but allows scrolling up/down", "less file.txt"),
        ("head", "Show first 10 lines of a file", "head file.txt"),
        ("file", "Detect the type of a file", "file image.png"),
        ("sudo", "Run a command as superuser (admin)", "sudo apt update"),
        ("man", "Open the manual/help page for a command", "man ls"),
        ("ps", "Show currently running processes", "ps aux"),
        ("kill", "Terminate a process by its ID", "kill 1234"),
        ("shutdown", "Power off the system", "sudo shutdown now"),
        ("restart", "Restart the system", "sudo reboot"),
        ("chmod", "Change file permissions", "chmod +x script.sh"),
        ("bash", "Run a bash shell script", "bash script.sh"),
        ("sh", "Run a shell script", "sh script.sh"),
        ("nano", "Simple terminal text editor", "nano file.txt"),
        ("alias", "Create a shortcut for a long command", "alias ll='ls -la'"),
        ("dpkg", "Debian package manager — install/remove .deb packages", "dpkg -i package.deb"),
        ("redirection", "Redirect output to a file using `>` or `>>`", "echo \"hi\" > out.txt"),
    ]
    for name, description, example in commands:
        print(f"{name:<12} {description}")
        print(f"{'':<12} example: {example}")
    print("\nRedirection practice:")
    print('  echo "Hello" > output.txt    # write (overwrites the file)')
    print('  echo "World" >> output.txt   # append')
    print("  cat output.txt               # read both lines")


def task_03():
    """Task 3: Add two numbers"""
    num1 = 1.5
    num2 = 6.3

    sum = num1 + num2

    print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))


def task_04():
    """Task 4: Add two numbers (user input)"""
    # Task 4 — Add Two Numbers (User Input)

    num1 = input('Enter first number: ')
    num2 = input('Enter second number: ')

    sum = float(num1) + float(num2)

    print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))


def task_05():
    """Task 5: Square root"""
    # Python Program to calculate the square root

    # Note: change this value for a different result
    num = 8

    # To take the input from the user
    # num = float(input('Enter a number: '))

    num_sqrt = num ** 0.5
    print('The square root of %0.3f is %0.3f' % (num, num_sqrt))


def task_06():
    """Task 6: Square root of a complex number"""
    # Task 6 — Square Root of a Complex Number

    import cmath

    num = 1 + 2j

    num_sqrt = cmath.sqrt(num)

    print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num, num_sqrt.real, num_sqrt.imag))


def task_07():
    """Task 7: Celsius to Fahrenheit"""
    # Task 7 — Celsius to Fahrenheit Converter

    celsius = 37.5

    fahrenheit = (celsius * 1.8) + 32

    print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' % (celsius, fahrenheit))


def task_08():
    """Task 8: Area of a triangle"""
    # Task 8 — Area of a Triangle (Heron's Formula)

    a = 5
    b = 6
    c = 7

    s = (a + b + c) / 2

    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

    print('The area of the triangle is %0.2f' % area)


def task_09():
    """Task 9: Quadratic equation"""
    # Task 9 — Solve Quadratic Equation: ax**2 + bx + c = 0

    import cmath

    a = 1
    b = 5
    c = 6

    # Calculate the discriminant
    d = (b ** 2) - (4 * a * c)

    # Find two solutions using the quadratic formula
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)

    print('The solutions are {0} and {1}'.format(sol1, sol2))


def task_10():
    """Task 10: Kilometers to miles"""
    # Task 10 — Kilometers to Miles Converter

    kilometers = float(input("Enter value in kilometers: "))

    # Conversion factor: 1 km = 0.621371 miles
    conv_fac = 0.621371

    miles = kilometers * conv_fac

    print('%0.3f kilometers is equal to %0.3f miles' % (kilometers, miles))


def task_11():
    """Task 11: Simple if statement"""
    # Task 11 — Simple if Statement (no else)
    # i = 10, condition is i > 15 which is False
    # So the if block is skipped entirely

    i = 10

    if (i > 15):
        print("10 is less than 15")

    print("I am Not in if")


def task_12():
    """Task 12: if / else statement"""
    # Task 12 — if / else Statement
    # i = 20, condition i < 15 is False
    # So Python goes into the else block

    i = 20

    if (i < 15):
        print("i is smaller than 15")
        print("i'm in if Block")
    else:
        print("i is greater than 15")
        print("i'm in else Block")

    print("i'm not in if and not in else Block")


def task_13():
    """Task 13: Nested if statements"""
    # Task 13 — Nested if Statements
    # i = 10
    # Outer if (i == 10) is True → we enter it
    # Inner if (i < 15) is True → prints
    # Second inner if (i < 12) is also True → prints
    # The else is never reached

    i = 10

    if (i == 10):
        # First if statement
        if (i < 15):
            print("i is smaller than 15")
        # Nested if — only runs if the outer if above is True
        if (i < 12):
            print("i is smaller than 12 too")
        else:
            print("i is greater than 15")


def task_14():
    """Task 14: if / elif / else chain"""
    # Task 14 — if / elif / elif / else Chain
    # i = 20
    # Python checks conditions top to bottom
    # First match wins — i == 20 is True, prints and stops

    i = 20

    if (i == 10):
        print("i is 10")
    elif (i == 15):
        print("i is 15")
    elif (i == 20):
        print("i is 20")
    else:
        print("i is not present")


def task_15():
    """Task 15: for loops"""
    # Task 15 — For Loops in Python

    # Basic for loop over a list
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)

    # For loop over a range
    print("\nCounting from 1 to 5:")
    for i in range(1, 6):
        print(i)

    # For loop with range and step
    print("\nEven numbers from 0 to 10:")
    for i in range(0, 11, 2):
        print(i)

    # For loop over a string
    print("\nLetters in 'Python':")
    for letter in "Python":
        print(letter)

    # For loop with index using enumerate
    print("\nWith index:")
    for index, fruit in enumerate(fruits):
        print(index, fruit)


def task_16():
    """Task 16: while loops"""
    # Task 16 — While Loops in Python

    # Basic while loop
    count = 1
    print("Counting up:")
    while count <= 5:
        print(count)
        count += 1

    # While loop with user-defined condition
    print("\nPowers of 2 below 100:")
    num = 1
    while num < 100:
        print(num)
        num = num * 2

    # While loop as a simple menu (fixed iterations for demo)
    print("\nCountdown:")
    n = 5
    while n > 0:
        print(n)
        n -= 1
    print("Go!")


def task_17():
    """Task 17: break statement"""
    # Task 17 — Break Statement in Python

    # break in a for loop — stop when number equals 3
    print("For loop with break (stops at 3):")
    for i in range(1, 8):
        if i == 3:
            break
        print(i)

    # break in a while loop — stop when number exceeds 15
    print("\nWhile loop with break (stops when num > 15):")
    num = 1
    while True:
        print(num)
        num = num * 2
        if num > 15:
            break

    # break in a nested loop — only breaks the inner loop
    print("\nBreak in nested loop:")
    for i in range(1, 4):
        for j in range(1, 4):
            if j == 2:
                break
            print(f"  i={i}, j={j}")


def task_18():
    """Task 18: continue statement"""
    # Task 18 — Continue Statement in Python

    # continue in a for loop — skip even numbers
    print("Odd numbers from 1 to 10 (skip evens with continue):")
    for i in range(1, 11):
        if i % 2 == 0:
            continue
        print(i)

    # continue in a while loop — skip multiples of 3
    print("\nNumbers 1-10, skipping multiples of 3:")
    i = 0
    while i < 10:
        i += 1
        if i % 3 == 0:
            continue
        print(i)

    # continue to skip a specific value in a list
    print("\nFruits list, skipping 'banana':")
    fruits = ["apple", "banana", "cherry", "mango"]
    for fruit in fruits:
        if fruit == "banana":
            continue
        print(fruit)


def task_19():
    """Task 19: Various looping techniques"""
    # Task 19 — Various Looping Techniques in Python

    # 1. enumerate() — loop with index and value
    print("1. enumerate():")
    colors = ["red", "green", "blue"]
    for index, color in enumerate(colors):
        print(f"  {index}: {color}")

    # 2. zip() — loop over two lists together
    print("\n2. zip():")
    names = ["Ali", "Sara", "Zain"]
    scores = [85, 92, 78]
    for name, score in zip(names, scores):
        print(f"  {name} scored {score}")

    # 3. items() — loop over dictionary key-value pairs
    print("\n3. dict.items():")
    student = {"name": "Raheel", "age": 22, "city": "Lahore"}
    for key, value in student.items():
        print(f"  {key}: {value}")

    # 4. List comprehension — compact loop to build a list
    print("\n4. List comprehension:")
    squares = [x ** 2 for x in range(1, 6)]
    print("  Squares:", squares)

    # 5. reversed() — loop in reverse
    print("\n5. reversed():")
    for i in reversed(range(1, 6)):
        print(f"  {i}")

    # 6. sorted() — loop in sorted order
    print("\n6. sorted():")
    nums = [40, 10, 30, 20, 50]
    for n in sorted(nums):
        print(f"  {n}")


def task_21():
    """Task 21: List data type"""
    # Task 21 — List Data Type in Python

    # Creating a list
    fruits = ["apple", "banana", "cherry", "mango"]
    print("List:", fruits)

    # Accessing elements
    print("First element:", fruits[0])
    print("Last element:", fruits[-1])

    # Slicing
    print("First two:", fruits[0:2])

    # Modifying a list
    fruits[1] = "blueberry"
    print("\nAfter modifying index 1:", fruits)

    # Adding elements
    fruits.append("grape")
    print("After append:", fruits)

    fruits.insert(1, "banana")
    print("After insert at index 1:", fruits)

    # Removing elements
    fruits.remove("cherry")
    print("\nAfter remove('cherry'):", fruits)

    popped = fruits.pop()
    print("After pop():", fruits, "| Popped:", popped)

    # List operations
    nums = [3, 1, 4, 1, 5, 9, 2]
    print("\nOriginal nums:", nums)
    print("Sorted:", sorted(nums))
    print("Reversed:", list(reversed(nums)))
    print("Length:", len(nums))
    print("Count of 1:", nums.count(1))


def task_22():
    """Task 22: Tuple data type"""
    # Task 22 — Tuple Data Type in Python

    # Creating a tuple — immutable (cannot be changed)
    coordinates = (10.5, 20.3)
    colors = ("red", "green", "blue")
    mixed = (1, "hello", 3.14, True)

    print("Coordinates:", coordinates)
    print("Colors:", colors)
    print("Mixed tuple:", mixed)

    # Accessing elements
    print("\nFirst color:", colors[0])
    print("Last color:", colors[-1])

    # Slicing
    print("First two colors:", colors[0:2])

    # Tuple unpacking
    x, y = coordinates
    print(f"\nUnpacked: x={x}, y={y}")

    # Tuple methods
    nums = (4, 2, 7, 2, 9, 2, 1)
    print("\nTuple:", nums)
    print("Count of 2:", nums.count(2))
    print("Index of 7:", nums.index(7))
    print("Length:", len(nums))

    # Tuple vs List — tuples are immutable
    print("\nTuples are immutable — you cannot change their values after creation.")
    print("Use tuples for fixed data like coordinates, RGB values, days of the week.")

    # Nested tuple
    nested = ((1, 2), (3, 4), (5, 6))
    print("\nNested tuple:", nested)
    print("Access nested element [1][0]:", nested[1][0])


def task_23():
    """Task 23: String data type"""
    # Task 23 — String Data Type in Python

    name = "Raheel Shaukat"

    # Basic string info
    print("String:", name)
    print("Length:", len(name))

    # Accessing characters
    print("\nFirst char:", name[0])
    print("Last char:", name[-1])
    print("Slicing [0:6]:", name[0:6])

    # String methods
    print("\nUppercase:", name.upper())
    print("Lowercase:", name.lower())
    print("Title case:", name.title())
    print("Replace:", name.replace("Raheel", "Python"))
    print("Split:", name.split(" "))
    print("Strip whitespace:", "  hello  ".strip())

    # String checking methods
    print("\n'Raheel'.isalpha():", "Raheel".isalpha())
    print("'12345'.isdigit():", "12345".isdigit())
    print("'hello'.startswith('he'):", "hello".startswith("he"))
    print("'hello'.endswith('lo'):", "hello".endswith("lo"))

    # String formatting
    age = 22
    city = "Lahore"
    print(f"\nf-string: My name is {name}, I am {age} from {city}")
    print("format(): {} is {} years old".format(name, age))

    # String joining
    words = ["Python", "is", "awesome"]
    sentence = " ".join(words)
    print("\nJoined:", sentence)

    # Counting and finding
    text = "the quick brown fox jumps over the lazy dog"
    print("\nCount of 'the':", text.count("the"))
    print("Index of 'fox':", text.find("fox"))


def task_24():
    """Task 24: Set data type"""
    # Task 24 — Set Data Type in Python

    # Creating a set — unordered, no duplicates
    fruits = {"apple", "banana", "cherry", "mango"}
    print("Set:", fruits)

    # Duplicates are automatically removed
    nums = {1, 2, 2, 3, 3, 3, 4}
    print("Set with duplicates removed:", nums)

    # Adding and removing elements
    fruits.add("grape")
    print("\nAfter add('grape'):", fruits)

    fruits.discard("banana")
    print("After discard('banana'):", fruits)

    # Set operations
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}

    print("\nSet A:", set_a)
    print("Set B:", set_b)
    print("Union (A | B):", set_a | set_b)
    print("Intersection (A & B):", set_a & set_b)
    print("Difference (A - B):", set_a - set_b)
    print("Symmetric Difference (A ^ B):", set_a ^ set_b)

    # Membership test
    print("\nIs 3 in set_a?", 3 in set_a)
    print("Is 6 in set_a?", 6 in set_a)

    # Subset and superset
    print("\n{1,2} is subset of set_a:", {1, 2}.issubset(set_a))
    print("set_a is superset of {1,2}:", set_a.issuperset({1, 2}))


def task_25():
    """Task 25: Dictionary data type"""
    # Task 25 — Dictionary Data Type in Python

    # Creating a dictionary — key:value pairs
    student = {
        "name": "Raheel",
        "age": 22,
        "city": "Lahore",
        "course": "AI/ML"
    }

    print("Dictionary:", student)

    # Accessing values
    print("\nName:", student["name"])
    print("Age:", student.get("age"))

    # Modifying values
    student["age"] = 23
    print("\nAfter update age to 23:", student)

    # Adding a new key
    student["university"] = "Virtual University"
    print("After adding university:", student)

    # Removing a key
    del student["city"]
    print("After deleting city:", student)

    popped = student.pop("course")
    print("After pop('course'):", student, "| Popped value:", popped)

    # Looping through a dictionary
    print("\nKeys:")
    for key in student.keys():
        print(" ", key)

    print("\nValues:")
    for value in student.values():
        print(" ", value)

    print("\nKey-Value pairs:")
    for key, value in student.items():
        print(f"  {key}: {value}")

    # Dictionary methods
    print("\nAll keys:", list(student.keys()))
    print("All values:", list(student.values()))
    print("Length:", len(student))

    # Nested dictionary
    classroom = {
        "student1": {"name": "Ali", "score": 85},
        "student2": {"name": "Sara", "score": 92}
    }
    print("\nNested dict - student1 score:", classroom["student1"]["score"])


TASKS = {
    1: (task_01, "Installation check"),
    2: (task_02, "Linux commands practice"),
    3: (task_03, "Add two numbers"),
    4: (task_04, "Add two numbers (user input)"),
    5: (task_05, "Square root"),
    6: (task_06, "Square root of a complex number"),
    7: (task_07, "Celsius to Fahrenheit"),
    8: (task_08, "Area of a triangle"),
    9: (task_09, "Quadratic equation"),
    10: (task_10, "Kilometers to miles"),
    11: (task_11, "Simple if statement"),
    12: (task_12, "if / else statement"),
    13: (task_13, "Nested if statements"),
    14: (task_14, "if / elif / else chain"),
    15: (task_15, "for loops"),
    16: (task_16, "while loops"),
    17: (task_17, "break statement"),
    18: (task_18, "continue statement"),
    19: (task_19, "Various looping techniques"),
    21: (task_21, "List data type"),
    22: (task_22, "Tuple data type"),
    23: (task_23, "String data type"),
    24: (task_24, "Set data type"),
    25: (task_25, "Dictionary data type"),
}


def run_task(n):
    func, title = TASKS[n]
    print(f"\n>>> Task {n}: {title}")
    func()


def main():
    arg = sys.argv[1].lower() if len(sys.argv) > 1 else ""
    if arg == "all":
        for n in TASKS:
            run_task(n)
        return
    if arg.isdigit() and int(arg) in TASKS:
        run_task(int(arg))
        return
    if arg:
        print(f"Unknown task '{arg}'.")
    while True:
        print("\nAvailable tasks:")
        for n, (_, title) in TASKS.items():
            print(f"  {n:>2}  {title}")
        choice = input("\nTask number, 'all' or 'q' to quit: ").strip().lower()
        if choice in ("", "q", "quit", "exit"):
            break
        if choice == "all":
            for n in TASKS:
                run_task(n)
        elif choice.isdigit() and int(choice) in TASKS:
            run_task(int(choice))
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

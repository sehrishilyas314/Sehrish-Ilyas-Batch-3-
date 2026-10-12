"""NAVTTC AI/ML Program - Week 2: Tasks 20, 26, 27, 49, 50

How to run:
    python week2_tasks.py          show a menu and pick a task
    python week2_tasks.py 20          run one task (here: task 20)
    python week2_tasks.py all      run every task in this file

Requires: numpy, scipy  (pip install numpy scipy)
Tasks that ask you to type something: 26
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def task_20():
    """Task 20: User defined functions"""
    # Task 20 — User Defined Functions in Python

    # Basic function with no parameters
    def greet():
        print("Hello! Welcome to Python Functions.")

    greet()

    # Function with parameters
    def greet_user(name):
        print(f"Hello, {name}!")

    greet_user("Raheel")

    # Function with return value
    def add(a, b):
        return a + b

    result = add(10, 20)
    print(f"\n10 + 20 = {result}")

    # Function with default parameter
    def power(base, exp=2):
        return base ** exp

    print(f"3 squared = {power(3)}")
    print(f"2 to the power 5 = {power(2, 5)}")

    # Function with multiple return values
    def min_max(numbers):
        return min(numbers), max(numbers)

    nums = [4, 7, 1, 9, 3]
    minimum, maximum = min_max(nums)
    print(f"\nList: {nums}")
    print(f"Min: {minimum}, Max: {maximum}")

    # Recursive function — factorial
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        return n * factorial(n - 1)

    print(f"\nFactorial of 5 = {factorial(5)}")


def task_26():
    """Task 26: Exception handling"""
    # Task 26 — Exception Handling in Python

    # Basic try / except
    print("--- Basic try/except ---")
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

    # Catching multiple exceptions
    print("\n--- Multiple exceptions ---")
    try:
        num = int("abc")
    except ValueError:
        print("Error: Invalid conversion — 'abc' is not an integer.")
    except TypeError:
        print("Error: Wrong type provided.")

    # try / except / else
    print("\n--- try / except / else ---")
    try:
        num = int("42")
    except ValueError:
        print("Conversion failed.")
    else:
        print("Conversion succeeded! Value:", num)

    # try / except / finally
    print("\n--- try / except / finally ---")
    try:
        x = int(input("Enter a number: "))
        print("You entered:", x)
    except ValueError:
        print("That was not a valid number.")
    finally:
        print("This always runs — good for cleanup.")

    # Catching any exception with a general except
    print("\n--- General exception with 'as e' ---")
    try:
        my_list = [1, 2, 3]
        print(my_list[10])
    except Exception as e:
        print(f"An error occurred: {e}")


def task_27():
    """Task 27: User defined exceptions"""
    # Task 27 — User Defined Exception Handling in Python

    # Define a custom exception by inheriting from Exception
    class NegativeNumberError(Exception):
        def __init__(self, value):
            self.value = value
            super().__init__(f"Negative numbers are not allowed: {value}")


    class AgeOutOfRangeError(Exception):
        def __init__(self, age):
            self.age = age
            super().__init__(f"Age must be between 0 and 120. Got: {age}")


    # Using custom exception — NegativeNumberError
    print("--- NegativeNumberError ---")
    def square_root_positive(num):
        if num < 0:
            raise NegativeNumberError(num)
        return num ** 0.5

    try:
        print(square_root_positive(9))
        print(square_root_positive(-4))
    except NegativeNumberError as e:
        print(f"Caught custom error: {e}")


    # Using custom exception — AgeOutOfRangeError
    print("\n--- AgeOutOfRangeError ---")
    def validate_age(age):
        if age < 0 or age > 120:
            raise AgeOutOfRangeError(age)
        print(f"Valid age: {age}")

    try:
        validate_age(25)
        validate_age(150)
    except AgeOutOfRangeError as e:
        print(f"Caught custom error: {e}")


def task_49():
    """Task 49: Mean, median and mode"""
    import numpy as np
    from scipy import stats

    # ─────────────────────────────────────────
    # Task 49 — Mean, Median and Mode
    # ─────────────────────────────────────────
    print("=" * 50)
    print("Task 49 — Mean, Median and Mode")
    print("=" * 50)

    scores = [85, 92, 78, 95, 88, 78, 90, 78, 85, 92]
    print("Dataset:", scores)

    # Mean — average of all values
    mean = np.mean(scores)
    print(f"\nMean:    {mean}")

    # Median — middle value when sorted
    median = np.median(scores)
    print(f"Median: {median}")

    # Mode — most frequently occurring value
    mode_result = stats.mode(scores, keepdims=True)
    print(f"Mode:    {mode_result.mode[0]} (appears {mode_result.count[0]} times)")

    # Manual explanation (Using total_val to avoid shadowing sum)
    sorted_scores = sorted(scores)
    total_val = sum(scores)  # Using the built-in sum() function safely now
    count_val = len(scores)

    print(f"\nSorted: {sorted_scores}")
    print(f"Mean   = sum({total_val}) / count({count_val}) = {mean}")
    print(f"Median = middle value of sorted list = {median}")
    print(f"Mode   = most frequent = 78 (appears 3 times)")

    # Example with skewed data
    print("\n--- Skewed Data Example ---")
    salaries = [30000, 32000, 31000, 33000, 200000]
    print("Salaries:", salaries)
    print(f"Mean:    {np.mean(salaries):.2f}  ← affected by outlier")
    print(f"Median: {np.median(salaries):.2f}  ← better for skewed data")


def task_50():
    """Task 50: Standard deviation"""
    import numpy as np
    from scipy import stats

    # ─────────────────────────────────────────
    # Task 50 — Standard Deviation
    # ─────────────────────────────────────────
    print("\n" + "=" * 50)
    print("Task 50 — Standard Deviation")
    print("=" * 50)

    data = [10, 20, 30, 40, 50]
    print("Dataset:", data)

    std_dev = np.std(data)
    variance = np.var(data)
    mean_val = np.mean(data)

    print(f"\nMean:               {mean_val}")
    print(f"Variance:          {variance}")
    print(f"Standard Deviation:{std_dev:.4f}")

    print("\nInterpretation:")
    print("  Low std dev  → data points are close to the mean (consistent)")
    print("  High std dev → data points are spread out (variable)")

    # Comparing two datasets
    print("\n--- Comparing Two Datasets ---")
    class_a = [70, 72, 68, 71, 69]
    class_b = [50, 90, 40, 95, 60]

    print(f"Class A scores: {class_a}")
    print(f"Class B scores: {class_b}")
    print(f"\nClass A — Mean: {np.mean(class_a):.1f}, Std Dev: {np.std(class_a):.2f}")
    print(f"Class B — Mean: {np.mean(class_b):.1f}, Std Dev: {np.std(class_b):.2f}")
    print("\nConclusion: Both classes have similar means, but Class B has")
    print("much higher std dev — scores are more spread out / inconsistent.")

    # Percentiles
    print("\n--- Percentiles ---")
    exam_scores = [45, 55, 60, 65, 70, 75, 80, 85, 90, 95]
    print("Exam scores:", exam_scores)
    print(f"25th percentile: {np.percentile(exam_scores, 25)}")
    print(f"50th percentile: {np.percentile(exam_scores, 50)}")
    print(f"75th percentile: {np.percentile(exam_scores, 75)}")


TASKS = {
    20: (task_20, "User defined functions"),
    26: (task_26, "Exception handling"),
    27: (task_27, "User defined exceptions"),
    49: (task_49, "Mean, median and mode"),
    50: (task_50, "Standard deviation"),
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

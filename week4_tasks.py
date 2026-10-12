"""NAVTTC AI/ML Program - Week 4: Tasks 41-48 (Pandas)

How to run:
    python week4_tasks.py          show a menu and pick a task
    python week4_tasks.py 41          run one task (here: task 41)
    python week4_tasks.py all      run every task in this file

Requires: pandas, numpy  (pip install pandas numpy)
Task 45 creates sample_students.csv in the current folder.
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def write_sample_csv():
    """Create sample_students.csv (used by Tasks 45 and 46)."""
    csv_data = "\n".join([
        "Name,Age,City,Score",
        "Ali,22,Lahore,85",
        "Sara,25,Karachi,92",
        "Zain,23,Islamabad,78",
        "Maha,21,Lahore,95",
        "Raheel,22,Lahore,88",
    ]) + "\n"
    with open("sample_students.csv", "w") as f:
        f.write(csv_data)


def task_41():
    """Task 41: Pandas basics"""
    import pandas as pd
    import numpy as np

    # ─────────────────────────────────────────
    # Task 41 — Pandas Basics
    # ─────────────────────────────────────────
    print("=" * 50)
    print("Task 41 — Pandas Basics")
    print("=" * 50)

    print("Pandas version:", pd.__version__)
    print("Pandas is built on top of NumPy and provides")
    print("two key data structures: Series and DataFrame.")


def task_42():
    """Task 42: Pandas installation check"""
    import pandas as pd
    import numpy as np

    # ─────────────────────────────────────────
    # Task 42 — Pandas Installation Check
    # ─────────────────────────────────────────
    print("\n" + "=" * 50)
    print("Task 42 — Pandas Installation")
    print("=" * 50)

    print("Successfully imported pandas as pd.")
    print("Install command: pip install pandas")


def task_43():
    """Task 43: Pandas Series"""
    import pandas as pd
    import numpy as np

    # ─────────────────────────────────────────
    # Task 43 — Pandas Series
    # ─────────────────────────────────────────
    print("\n" + "=" * 50)
    print("Task 43 — Pandas Series")
    print("=" * 50)

    # Creating a Series from a list
    s1 = pd.Series([10, 20, 30, 40, 50])
    print("Series from list:\n", s1)

    # Series with custom index
    s2 = pd.Series([85, 92, 78, 95], index=["Ali", "Sara", "Zain", "Maha"])
    print("\nSeries with custom index:\n", s2)

    # Accessing elements
    print("\nScore of Sara:", s2["Sara"])
    print("Scores above 85:\n", s2[s2 > 85])

    # Series from dictionary
    s3 = pd.Series({"name": "Raheel", "city": "Lahore", "course": "AI/ML"})
    print("\nSeries from dict:\n", s3)

    # Series operations
    nums = pd.Series([1, 2, 3, 4, 5])
    print("\nOriginal Series:", nums.values)
    print("Mean:", nums.mean())
    print("Sum:", nums.sum())
    print("Max:", nums.max())


def task_44():
    """Task 44: Pandas DataFrame"""
    import pandas as pd
    import numpy as np

    # ─────────────────────────────────────────
    # Task 44 — Pandas DataFrame
    # ─────────────────────────────────────────
    print("\n" + "=" * 50)
    print("Task 44 — Pandas DataFrame")
    print("=" * 50)

    data = {
        "Name":   ["Ali", "Sara", "Zain", "Maha", "Raheel"],
        "Age":    [22, 25, 23, 21, 22],
        "City":   ["Lahore", "Karachi", "Islamabad", "Lahore", "Lahore"],
        "Score":  [85, 92, 78, 95, 88]
    }
    df = pd.DataFrame(data)
    print("DataFrame:\n", df)

    # Accessing columns
    print("\nNames column:\n", df["Name"])

    # Accessing rows with loc and iloc
    print("\nRow at index 0 (loc):\n", df.loc[0])
    print("\nRow at position 2 (iloc):\n", df.iloc[2])

    # Adding a new column
    df["Grade"] = ["B", "A", "C", "A", "B"]
    print("\nWith Grade column:\n", df)

    # DataFrame info
    print("\nShape:", df.shape)
    print("Columns:", list(df.columns))
    print("dtypes:\n", df.dtypes)


def task_45():
    """Task 45: Pandas: read CSV"""
    import pandas as pd
    import numpy as np

    # ─────────────────────────────────────────
    # Task 45 — Reading CSV Files
    # ─────────────────────────────────────────
    print("\n" + "=" * 50)
    print("Task 45 — Pandas Read CSV")
    print("=" * 50)

    # Create a sample CSV file to read
    write_sample_csv()

    df_csv = pd.read_csv("sample_students.csv")
    print("DataFrame from CSV:\n", df_csv)
    print("\nFirst 3 rows (head):\n", df_csv.head(3))
    print("\nLast 2 rows (tail):\n", df_csv.tail(2))


def task_46():
    """Task 46: Pandas: analyzing data"""
    import pandas as pd
    import numpy as np

    # ─────────────────────────────────────────
    # Task 46 — Data Analysis
    # ─────────────────────────────────────────
    print("\n" + "=" * 50)
    print("Task 46 — Pandas Data Analysis")
    print("=" * 50)

    # Same sample file as Task 45, so this task also works on its own
    write_sample_csv()
    df_csv = pd.read_csv("sample_students.csv")

    print("Basic info:")
    df_csv.info()

    print("\nDescriptive statistics:\n", df_csv.describe())
    print("\nMean score:", df_csv["Score"].mean())
    print("Max score:", df_csv["Score"].max())
    print("Min age:", df_csv["Age"].min())

    print("\nValue counts for City:\n", df_csv["City"].value_counts())

    # Filtering
    lahore_students = df_csv[df_csv["City"] == "Lahore"]
    print("\nStudents from Lahore:\n", lahore_students)

    high_scorers = df_csv[df_csv["Score"] > 85]
    print("\nHigh scorers (>85):\n", high_scorers)

    # Sorting
    sorted_df = df_csv.sort_values("Score", ascending=False)
    print("\nSorted by Score (desc):\n", sorted_df)


def task_47():
    """Task 47: Pandas: cleaning data"""
    import pandas as pd
    import numpy as np

    # ─────────────────────────────────────────
    # Task 47 — Data Cleaning
    # ─────────────────────────────────────────
    print("\n" + "=" * 50)
    print("Task 47 — Pandas Data Cleaning")
    print("=" * 50)

    dirty_data = {
        "Name":  ["Ali", "Sara", None, "Maha", "Raheel"],
        "Age":   [22, None, 23, 21, 22],
        "Score": [85, 92, 78, None, 88]
    }
    df_dirty = pd.DataFrame(dirty_data)
    print("Dirty DataFrame:\n", df_dirty)

    print("\nNull values:\n", df_dirty.isnull().sum())

    df_filled = df_dirty.copy()
    df_filled["Age"] = df_filled["Age"].fillna(df_filled["Age"].mean())
    df_filled["Score"] = df_filled["Score"].fillna(df_filled["Score"].mean())
    df_filled["Name"] = df_filled["Name"].fillna("Unknown")
    print("\nAfter filling nulls:\n", df_filled)

    df_dropped = df_dirty.dropna()
    print("\nAfter dropping null rows:\n", df_dropped)

    # Removing duplicates
    df_dup = pd.DataFrame({
        "Name": ["Ali", "Sara", "Ali", "Zain"],
        "Score": [85, 92, 85, 78]
    })
    print("\nWith duplicates:\n", df_dup)
    print("After drop_duplicates:\n", df_dup.drop_duplicates())


def task_48():
    """Task 48: Pandas: correlation"""
    import pandas as pd
    import numpy as np

    # ─────────────────────────────────────────
    # Task 48 — Data Correlation
    # ─────────────────────────────────────────
    print("\n" + "=" * 50)
    print("Task 48 — Pandas Data Correlation")
    print("=" * 50)

    corr_data = {
        "StudyHours": [2, 4, 6, 8, 10, 3, 7, 5],
        "Score":      [50, 65, 75, 85, 95, 55, 80, 70],
        "Absences":   [5, 3, 2, 1, 0, 4, 1, 2]
    }
    df_corr = pd.DataFrame(corr_data)
    print("DataFrame:\n", df_corr)

    correlation_matrix = df_corr.corr()
    print("\nCorrelation Matrix:\n", correlation_matrix)

    print("\nCorrelation between StudyHours and Score:",
          round(df_corr["StudyHours"].corr(df_corr["Score"]), 4))
    print("Correlation between Absences and Score:",
          round(df_corr["Absences"].corr(df_corr["Score"]), 4))
    print("\nInterpretation:")
    print("  Close to +1 = strong positive correlation")
    print("  Close to -1 = strong negative correlation")
    print("  Close to  0 = no correlation")


TASKS = {
    41: (task_41, "Pandas basics"),
    42: (task_42, "Pandas installation check"),
    43: (task_43, "Pandas Series"),
    44: (task_44, "Pandas DataFrame"),
    45: (task_45, "Pandas: read CSV"),
    46: (task_46, "Pandas: analyzing data"),
    47: (task_47, "Pandas: cleaning data"),
    48: (task_48, "Pandas: correlation"),
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

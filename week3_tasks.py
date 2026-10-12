"""NAVTTC AI/ML Program - Week 3: Tasks 28-40 (NumPy)

How to run:
    python week3_tasks.py          show a menu and pick a task
    python week3_tasks.py 28          run one task (here: task 28)
    python week3_tasks.py all      run every task in this file

Requires: numpy  (pip install numpy)
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def task_28():
    """Task 28: NumPy: creating arrays"""
    import numpy as np

    # ─────────────────────────────────────────
    # Task 28 — Creating Arrays
    # ─────────────────────────────────────────
    print("=" * 50)
    print("Task 28 — Creating Arrays")
    print("=" * 50)

    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([[1, 2, 3], [4, 5, 6]])
    arr_zeros = np.zeros((2, 3))
    arr_ones = np.ones((2, 3))
    arr_range = np.arange(0, 10, 2)
    arr_linspace = np.linspace(0, 1, 5)

    print("1D array:", arr1)
    print("2D array:\n", arr2)
    print("Zeros:\n", arr_zeros)
    print("Ones:\n", arr_ones)
    print("Arange (0-10, step 2):", arr_range)
    print("Linspace (0 to 1, 5 pts):", arr_linspace)


def task_29():
    """Task 29: NumPy: indexing"""
    import numpy as np

    # ─────────────────────────────────────────
    # Task 29 — Array Indexing
    # ─────────────────────────────────────────
    print("\n" + "=" * 50)
    print("Task 29 — Array Indexing")
    print("=" * 50)

    arr = np.array([10, 20, 30, 40, 50])
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    print("Array:", arr)
    print("Index 0:", arr[0])
    print("Index -1:", arr[-1])
    print("\nMatrix:\n", matrix)
    print("Element at row 1, col 2:", matrix[1, 2])
    print("Entire row 0:", matrix[0])
    print("Entire col 1:", matrix[:, 1])


def task_30():
    """Task 30: NumPy: slicing"""
    import numpy as np

    # ─────────────────────────────────────────
    # Task 30 — Array Slicing
    # ─────────────────────────────────────────
    print("\n" + "=" * 50)
    print("Task 30 — Array Slicing")
    print("=" * 50)

    arr = np.array([10, 20, 30, 40, 50, 60, 70])
    print("Array:", arr)
    print("arr[1:4]:", arr[1:4])
    print("arr[:3]:", arr[:3])
    print("arr[4:]:", arr[4:])
    print("arr[::2]:", arr[::2])

    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("\nMatrix:\n", matrix)
    print("First 2 rows:\n", matrix[:2])
    print("Last 2 cols:\n", matrix[:, 1:])


def task_31():
    """Task 31: NumPy: data types"""
    import numpy as np

    # ─────────────────────────────────────────
    # Task 31 — NumPy Data Types
    # ─────────────────────────────────────────
    print("\n" + "=" * 50)
    print("Task 31 — NumPy Data Types")
    print("=" * 50)

    arr_int = np.array([1, 2, 3], dtype=np.int32)
    arr_float = np.array([1.1, 2.2, 3.3], dtype=np.float64)
    arr_bool = np.array([True, False, True], dtype=bool)
    arr_str = np.array(["a", "b", "c"], dtype=str)

    print("int32 array:", arr_int, "| dtype:", arr_int.dtype)
    print("float64 array:", arr_float, "| dtype:", arr_float.dtype)
    print("bool array:", arr_bool, "| dtype:", arr_bool.dtype)
    print("str array:", arr_str, "| dtype:", arr_str.dtype)

    # Type conversion
    arr_converted = arr_int.astype(float)
    print("\nConverted int to float:", arr_converted, "| dtype:", arr_converted.dtype)


def task_32():
    """Task 32: NumPy: copy vs view"""
    import numpy as np

    # ─────────────────────────────────────────
    # Task 32 — Copy vs View
    # ─────────────────────────────────────────
    print("\n" + "=" * 50)
    print("Task 32 — Copy vs View")
    print("=" * 50)

    original = np.array([1, 2, 3, 4, 5])

    view_arr = original.view()
    copy_arr = original.copy()

    original[0] = 99

    print("Original after change:", original)
    print("View reflects change:", view_arr)
    print("Copy does NOT change:", copy_arr)


def task_33():
    """Task 33: NumPy: array shape"""
    import numpy as np

    # ─────────────────────────────────────────
    # Task 33 — Array Shape
    # ─────────────────────────────────────────
    print("\n" + "=" * 50)
    print("Task 33 — Array Shape")
    print("=" * 50)

    arr1d = np.array([1, 2, 3, 4, 5])
    arr2d = np.array([[1, 2, 3], [4, 5, 6]])
    arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

    print("1D shape:", arr1d.shape)
    print("2D shape:", arr2d.shape)
    print("3D shape:", arr3d.shape)
    print("ndim of 3D:", arr3d.ndim)
    print("size of 2D:", arr2d.size)


def task_34():
    """Task 34: NumPy: reshaping"""
    import numpy as np

    # ─────────────────────────────────────────
    # Task 34 — Array Reshaping
    # ─────────────────────────────────────────
    print("\n" + "=" * 50)
    print("Task 34 — Array Reshaping")
    print("=" * 50)

    arr = np.arange(1, 13)
    print("Original (12 elements):", arr)

    reshaped_2d = arr.reshape(3, 4)
    print("Reshaped to (3,4):\n", reshaped_2d)

    reshaped_3d = arr.reshape(2, 3, 2)
    print("Reshaped to (2,3,2):\n", reshaped_3d)

    flattened = reshaped_2d.flatten()
    print("Flattened back:", flattened)


def task_35():
    """Task 35: NumPy: iteration"""
    import numpy as np

    # ─────────────────────────────────────────
    # Task 35 — Array Iteration
    # ─────────────────────────────────────────
    print("\n" + "=" * 50)
    print("Task 35 — Array Iteration")
    print("=" * 50)

    arr1d = np.array([10, 20, 30])
    arr2d = np.array([[1, 2, 3], [4, 5, 6]])

    print("Iterating 1D:")
    for x in arr1d:
        print(" ", x)

    print("Iterating 2D rows:")
    for row in arr2d:
        print(" ", row)

    print("Iterating 2D elements with nditer:")
    for x in np.nditer(arr2d):
        print(" ", x, end=" ")
    print()

    print("With index using ndenumerate:")
    for idx, val in np.ndenumerate(arr2d):
        print(f"  index {idx}: {val}")


def task_36():
    """Task 36: NumPy: joining"""
    import numpy as np

    # ─────────────────────────────────────────
    # Task 36 — Matrix Joining
    # ─────────────────────────────────────────
    print("\n" + "=" * 50)
    print("Task 36 — Array Joining")
    print("=" * 50)

    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    concatenated = np.concatenate((a, b))
    print("Concatenate 1D:", concatenated)

    arr1 = np.array([[1, 2], [3, 4]])
    arr2 = np.array([[5, 6], [7, 8]])

    hstacked = np.hstack((arr1, arr2))
    vstacked = np.vstack((arr1, arr2))

    print("hstack (side by side):\n", hstacked)
    print("vstack (top to bottom):\n", vstacked)


def task_37():
    """Task 37: NumPy: splitting"""
    import numpy as np

    # ─────────────────────────────────────────
    # Task 37 — Array Splitting
    # ─────────────────────────────────────────
    print("\n" + "=" * 50)
    print("Task 37 — Array Splitting")
    print("=" * 50)

    arr = np.array([1, 2, 3, 4, 5, 6])
    split3 = np.array_split(arr, 3)
    print("Split into 3:", split3)

    matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    hsplit = np.hsplit(matrix, 2)
    print("hsplit into 2:\n", hsplit)

    vsplit_arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    vsplit = np.vsplit(vsplit_arr, 2)
    print("vsplit into 2:\n", vsplit)


def task_38():
    """Task 38: NumPy: searching"""
    import numpy as np

    # ─────────────────────────────────────────
    # Task 38 — Array Searching
    # ─────────────────────────────────────────
    print("\n" + "=" * 50)
    print("Task 38 — Array Searching")
    print("=" * 50)

    arr = np.array([10, 20, 30, 40, 50, 30, 20])

    where_30 = np.where(arr == 30)
    print("Indices where value == 30:", where_30)

    where_gt25 = np.where(arr > 25)
    print("Indices where value > 25:", where_gt25)

    search_sorted = np.searchsorted(np.array([1, 3, 5, 7, 9]), 4)
    print("searchsorted — insert 4 at index:", search_sorted)


def task_39():
    """Task 39: NumPy: sorting"""
    import numpy as np

    # ─────────────────────────────────────────
    # Task 39 — Array Sorting
    # ─────────────────────────────────────────
    print("\n" + "=" * 50)
    print("Task 39 — Array Sorting")
    print("=" * 50)

    arr = np.array([40, 10, 30, 20, 50])
    print("Original:", arr)
    print("Sorted ascending:", np.sort(arr))
    print("Sorted descending:", np.sort(arr)[::-1])

    arr2d = np.array([[30, 10, 20], [60, 40, 50]])
    print("\n2D sorted along axis=1 (row-wise):\n", np.sort(arr2d, axis=1))
    print("2D sorted along axis=0 (col-wise):\n", np.sort(arr2d, axis=0))


def task_40():
    """Task 40: NumPy: random"""
    import numpy as np

    # ─────────────────────────────────────────
    # Task 40 — Random Techniques
    # ─────────────────────────────────────────
    print("\n" + "=" * 50)
    print("Task 40 — NumPy Random")
    print("=" * 50)

    np.random.seed(42)

    rand_int = np.random.randint(1, 100, size=5)
    rand_float = np.random.rand(5)
    rand_normal = np.random.randn(5)
    rand_choice = np.random.choice([10, 20, 30, 40, 50], size=3)

    print("Random integers (1-100):", rand_int)
    print("Random floats (0-1):", rand_float)
    print("Normal distribution:", rand_normal)
    print("Random choice:", rand_choice)

    arr = np.array([1, 2, 3, 4, 5])
    np.random.shuffle(arr)
    print("Shuffled array:", arr)


TASKS = {
    28: (task_28, "NumPy: creating arrays"),
    29: (task_29, "NumPy: indexing"),
    30: (task_30, "NumPy: slicing"),
    31: (task_31, "NumPy: data types"),
    32: (task_32, "NumPy: copy vs view"),
    33: (task_33, "NumPy: array shape"),
    34: (task_34, "NumPy: reshaping"),
    35: (task_35, "NumPy: iteration"),
    36: (task_36, "NumPy: joining"),
    37: (task_37, "NumPy: splitting"),
    38: (task_38, "NumPy: searching"),
    39: (task_39, "NumPy: sorting"),
    40: (task_40, "NumPy: random"),
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

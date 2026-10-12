"""NAVTTC AI/ML Program - Week 5: Tasks 51-52 (Machine Learning)

How to run:
    python week5_tasks.py          show a menu and pick a task
    python week5_tasks.py 51          run one task (here: task 51)
    python week5_tasks.py all      run every task in this file

Requires: numpy, matplotlib, scikit-learn  (pip install numpy matplotlib scikit-learn)
Tasks 51 and 52 save their plots as .png files in the current folder.
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def task_51():
    """Task 51: Linear regression"""
    # Task 51 — Linear Regression with scikit-learn
    # Dataset: Boston-style housing data (generated)
    # Goal: Predict house price based on number of rooms

    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

    # ── Step 1: Create Dataset ──────────────────────────────────────────────────
    np.random.seed(42)
    rooms = np.random.uniform(3, 10, 100).reshape(-1, 1)
    price = rooms * 50000 + np.random.normal(0, 20000, 100).reshape(-1, 1)

    print("=" * 55)
    print("Task 51 — Linear Regression")
    print("=" * 55)
    print(f"Dataset: {len(rooms)} houses")
    print(f"Feature: Number of rooms (X)")
    print(f"Target : House price in $ (y)")

    # ── Step 2: Split into Train and Test ───────────────────────────────────────
    X_train, X_test, y_train, y_test = train_test_split(
        rooms, price, test_size=0.2, random_state=42
    )
    print(f"\nTrain size: {len(X_train)} | Test size: {len(X_test)}")

    # ── Step 3: Train the Model ─────────────────────────────────────────────────
    model = LinearRegression()
    model.fit(X_train, y_train)

    print(f"\nModel trained.")
    print(f"Slope (coefficient) : ${model.coef_[0][0]:,.2f} per room")
    print(f"Intercept           : ${model.intercept_[0]:,.2f}")

    # ── Step 4: Make Predictions ────────────────────────────────────────────────
    y_pred = model.predict(X_test)

    # ── Step 5: Evaluate the Model ──────────────────────────────────────────────
    mae  = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2   = r2_score(y_test, y_pred)

    print(f"\n── Evaluation Metrics ──")
    print(f"MAE  (Mean Absolute Error) : ${mae:,.2f}")
    print(f"RMSE (Root Mean Sq Error)  : ${rmse:,.2f}")
    print(f"R²   (Accuracy score)      : {r2:.4f}  (1.0 = perfect)")

    # ── Step 6: Predict a New Value ─────────────────────────────────────────────
    new_house_rooms = np.array([[7]])
    predicted_price = model.predict(new_house_rooms)
    print(f"\nPrediction: A house with 7 rooms → ${predicted_price[0][0]:,.2f}")

    # ── Step 7: Plot ─────────────────────────────────────────────────────────────
    plt.figure(figsize=(8, 5))
    plt.scatter(X_test, y_test, color="steelblue", alpha=0.7, label="Actual prices")
    plt.plot(X_test, y_pred, color="red", linewidth=2, label="Regression line")
    plt.xlabel("Number of Rooms")
    plt.ylabel("House Price ($)")
    plt.title("Task 51 — Linear Regression: Rooms vs House Price")
    plt.legend()
    plt.tight_layout()
    plt.savefig("task_51_linear_regression.png", dpi=150)
    print("\nPlot saved as: task_51_linear_regression.png")


def task_52():
    """Task 52: Logistic regression"""
    # Task 52 — Logistic Regression with scikit-learn
    # Dataset: Breast Cancer (built-in sklearn dataset)
    # Goal: Classify tumour as Malignant (0) or Benign (1)

    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.datasets import load_breast_cancer
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import (accuracy_score, confusion_matrix,
                                 classification_report)

    # ── Step 1: Load Dataset ─────────────────────────────────────────────────────
    data = load_breast_cancer()
    X = data.data
    y = data.target

    print("=" * 55)
    print("Task 52 — Logistic Regression")
    print("=" * 55)
    print(f"Dataset : Breast Cancer (sklearn built-in)")
    print(f"Samples : {X.shape[0]}")
    print(f"Features: {X.shape[1]}")
    print(f"Classes : {data.target_names}")

    # ── Step 2: Train / Test Split ───────────────────────────────────────────────
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print(f"\nTrain size: {len(X_train)} | Test size: {len(X_test)}")

    # ── Step 3: Feature Scaling ──────────────────────────────────────────────────
    # Logistic Regression is sensitive to feature scale — we normalise
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test  = scaler.transform(X_test)

    # ── Step 4: Train the Model ──────────────────────────────────────────────────
    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train, y_train)
    print("\nModel trained.")

    # ── Step 5: Predictions ──────────────────────────────────────────────────────
    y_pred = model.predict(X_test)

    # ── Step 6: Evaluate ─────────────────────────────────────────────────────────
    accuracy = accuracy_score(y_test, y_pred)
    cm       = confusion_matrix(y_test, y_pred)

    print(f"\n── Evaluation Metrics ──")
    print(f"Accuracy: {accuracy * 100:.2f}%")
    print(f"\nConfusion Matrix:")
    print(f"  True Negative  (Malignant correctly predicted): {cm[0][0]}")
    print(f"  False Positive (Malignant predicted as Benign): {cm[0][1]}")
    print(f"  False Negative (Benign predicted as Malignant): {cm[1][0]}")
    print(f"  True Positive  (Benign correctly predicted)   : {cm[1][1]}")
    print(f"\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=data.target_names))

    # ── Step 7: Predict One New Sample ───────────────────────────────────────────
    sample = X_test[0].reshape(1, -1)
    prediction = model.predict(sample)
    probability = model.predict_proba(sample)
    print(f"Sample prediction : {data.target_names[prediction[0]]}")
    print(f"Confidence        : {max(probability[0]) * 100:.2f}%")

    # ── Step 8: Plot Confusion Matrix ────────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(5, 4))
    im = ax.imshow(cm, interpolation="nearest", cmap=plt.cm.Blues)
    plt.colorbar(im)
    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])
    ax.set_xticklabels(data.target_names)
    ax.set_yticklabels(data.target_names)
    for i in range(2):
        for j in range(2):
            ax.text(j, i, cm[i, j], ha="center", va="center",
                    color="white" if cm[i, j] > cm.max() / 2 else "black",
                    fontsize=14)
    ax.set_xlabel("Predicted Label")
    ax.set_ylabel("True Label")
    ax.set_title("Task 52 — Logistic Regression: Confusion Matrix")
    plt.tight_layout()
    plt.savefig("task_52_logistic_regression.png", dpi=150)
    print("\nPlot saved as: task_52_logistic_regression.png")


TASKS = {
    51: (task_51, "Linear regression"),
    52: (task_52, "Logistic regression"),
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

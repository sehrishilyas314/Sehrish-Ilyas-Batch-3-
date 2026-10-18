# OOP Practice Exercises : All Solutions


# ============================================================
# OOP - Task 1: Your First Class
# ============================================================
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


book1 = Book("Deep Work", "Cal Newport")
print(book1.title)
print(book1.author)


# ============================================================
# OOP - Task 2: A Method That Returns a Value
# ============================================================
class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def summary(self):
        return f"{self.title} ({self.year})"


movie1 = Movie("Inception", 2010)
print(movie1.summary())


# ============================================================
# OOP - Task 3: Class Attribute vs Instance Attribute
# ============================================================
class Car:
    wheels = 4  # class attribute (shared by all cars)

    def __init__(self, brand):
        self.brand = brand  # instance attribute (unique per car)


car1 = Car("Toyota")
car2 = Car("Honda")

print(car1.brand, car1.wheels)
print(car2.brand, car2.wheels)


# ============================================================
# OOP - Task 4: Multiple Objects in a Loop
# ============================================================
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


employees = [
    Employee("Ali", 50000),
    Employee("Sara", 65000),
    Employee("Ahmed", 48000),
]

for emp in employees:
    print(f"{emp.name}: {emp.salary}")


# ============================================================
# OOP - Task 5: __str__ for Readable Output
# ============================================================
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employee: {self.name}, Salary: {self.salary}"


employee1 = Employee("Ali", 50000)
print(employee1)


# ============================================================
# OOP - Task 6: A Method That Uses Other Attributes
# ============================================================
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


rect1 = Rectangle(5, 3)
print("Area:", rect1.area())
print("Perimeter:", rect1.perimeter())


# ============================================================
# OOP - Task 7: Encapsulation with a Guard Condition
# ============================================================
class Wallet:
    def __init__(self, balance):
        self._balance = balance

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance: {self._balance}")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self._balance


wallet1 = Wallet(1000)
wallet1.withdraw(300)    # succeeds
wallet1.withdraw(5000)   # fails
print("Final balance:", wallet1.get_balance())


# ============================================================
# OOP - Task 8: Basic Inheritance
# ============================================================
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def describe(self):
        return f"{self.brand} can travel at {self.speed} km/h."


class ElectricVehicle(Vehicle):
    def __init__(self, brand, speed, battery_range):
        super().__init__(brand, speed)
        self.battery_range = battery_range

    def describe(self):
        base = super().describe()
        return f"{base} It has a battery range of {self.battery_range} km."


ev = ElectricVehicle("Tesla", 250, 500)
print(ev.describe())


# ============================================================
# OOP - Task 9: A List of Mixed Objects with a Shared Method (Polymorphism)
# ============================================================
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * 3.1416


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


shapes = [Circle(5), Square(4)]

for shape in shapes:
    print(f"{type(shape).__name__} area: {shape.area():.2f}")


# ============================================================
# OOP - Task 10: Combine Class + List Comprehension
# ============================================================
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


products = [
    Product("Keyboard", 45),
    Product("Monitor", 150),
    Product("Mouse", 25),
    Product("Laptop", 1200),
]

expensive_names = [p.name for p in products if p.price > 100]
print(expensive_names)


# ============================================================
# OOP - Task 11: A Simple Dataset Class
# ============================================================
class Dataset:
    def __init__(self, values):
        self.values = values

    def mean(self):
        return sum(self.values) / len(self.values)

    def minimum(self):
        return min(self.values)

    def maximum(self):
        return max(self.values)

    def normalize(self):
        low = self.minimum()
        high = self.maximum()
        return [(v - low) / (high - low) for v in self.values]


data = Dataset([10, 20, 30, 40, 50])
print("Mean:", data.mean())
print("Min:", data.minimum())
print("Max:", data.maximum())
print("Normalized:", data.normalize())


# ============================================================
# OOP - Task 12: A Base Model Class and Two Subclasses
# ============================================================
class BaseModel:
    def __init__(self):
        self.is_trained = False

    def predict(self):
        if not self.is_trained:
            raise ValueError("Model has not been trained yet. Call fit() first.")


class ConstantModel(BaseModel):
    def __init__(self):
        super().__init__()
        self.constant = None

    def fit(self, training_values):
        self.constant = max(training_values)
        self.is_trained = True

    def predict(self, n):
        super().predict()  # reuse the parent's "not trained" guard
        return [self.constant] * n


class AverageModel(BaseModel):
    def __init__(self):
        super().__init__()
        self.average = None

    def fit(self, training_values):
        self.average = sum(training_values) / len(training_values)
        self.is_trained = True

    def predict(self, n):
        super().predict()  # reuse the parent's "not trained" guard
        return [self.average] * n


training_data = [5, 10, 15, 20, 25]

constant_model = ConstantModel()
constant_model.fit(training_data)
print("ConstantModel:", constant_model.predict(3))

average_model = AverageModel()
average_model.fit(training_data)
print("AverageModel:", average_model.predict(3))

# Untrained model should raise an error
untrained_model = AverageModel()
try:
    untrained_model.predict(2)
except ValueError as error:
    print("Error:", error)


# ============================================================
# OOP - Task 13: Records as Objects
# ============================================================
class StudentRecord:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        else:
            return "F"


students = [
    StudentRecord("Ali", [78, 85, 90]),
    StudentRecord("Sara", [88, 92, 95]),
    StudentRecord("Ahmed", [55, 62, 58]),
    StudentRecord("Ayesha", [90, 87, 93]),
]

for s in students:
    print(f"{s.name}: average={s.average():.2f}, grade={s.grade()}")

top_students = [s.name for s in students if s.grade() in ("A", "B")]
print("Students with grade A or B:", top_students)

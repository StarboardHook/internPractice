# Design Patterns in Python

A concise demonstration of fundamental design patterns widely used in software engineering:.
Each section includes an explanation, use cases, benefits, and Python examples.

---

## 📚 Table of Contents
- [Factory Pattern](#-factory-pattern)
  - [Purpose](#purpose)
  - [When to Use](#when-to-use)
  - [Benefits](#benefits)
  - [Example](#example)
- [Observer Pattern](#-observer-pattern)
  - [Purpose](#purpose-1)
  - [When to Use](#when-to-use-1)
  - [Benefits](#benefits-1)
  - [Example](#example-1)
- [Singleton Pattern](#-singleton-pattern)
  - [Purpose](#purpose-2)
  - [When to Use](#when-to-use-2)
  - [Benefits](#benefits-2)
  - [Example](#example-2)
- [Comparison Table](#-comparison-table)

---

# 🏭 Factory Pattern

## Purpose
The Factory Pattern provides a centralized way to create objects without exposing the instantiation logic to the client.  
The factory decides **which object to create**, improving modularity and scalability.

---

## When to Use
- You need to create objects from a **family of related classes**
- Creation depends on **runtime conditions**
- You want to avoid large `if/elif` blocks throughout your code
- You want **loose coupling** and **cleaner architecture**

---

## Benefits
- Centralized object creation  
- Simplifies adding new object types  
- Reduces code duplication  
- Respects the **Open/Closed Principle** (OCP)

---

## Example
Internship Implementation: [View Code](./FactoryPattern)
```python
class Shape:
    def draw(self): pass


class Circle(Shape):
    def draw(self):
        print("Drawing Circle")


class Square(Shape):
    def draw(self):
        print("Drawing Square")


class ShapeFactory:
    @staticmethod
    def create(shape_type):
        if shape_type == "circle":
            return Circle()
        if shape_type == "square":
            return Square()
        raise ValueError("Unknown shape type")


shape = ShapeFactory.create("circle")
shape.draw()
```
---

# 👀 Observer Pattern

## Purpose
The Observer Pattern establishes a one-to-many relationship between objects.
When the subject's state changes, all observers are automatically notified.

---

## When to Use
- Many components must react to changes in one object
- You're building event-driven or real-time systems
- You want to avoid manually updating dependent components
- Examples: UI systems, notification systems, trading bots, loggers

---

## Benefits
- Loose coupling between subject and observers
- Automatic state propagation
- Easily extensible—add observers without modifying the subject
- Encourages modular, reactive designs

---

## Example
Internship Implementation: [View Code](./ObserverPattern)
```python
class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, data):
        for obs in self.observers:
            obs.update(data)


class Logger:
    def update(self, data):
        print(f"[LOG]: {data}")


class Emailer:
    def update(self, data):
        print(f"Sending email: {data}")


subject = Subject()
subject.attach(Logger())
subject.attach(Emailer())

subject.notify("System started")
```
---

# 🔒 Singleton Pattern

## Purpose
Ensures that only one instance of a class exists and provides a global access point to that instance.

---

## When to Use
- Centralized configurations
- Logging system
- Database connection manager
- Cache system
- Anything where multiple copies would cause inconsistency or wasted resources

---

## Benefits
- Guarantee a single shared instance
- Prevent expensive resource duplication
- Global access to shared state
- Useful for app-wide shared configuration

## Example
Internship Implementation: [View Code](./SingletonPattern)
```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


a = Singleton()
b = Singleton()

print(a is b)  # True

print(a is b)  # True
```
---

# ⭐ Comparison Table
| Pattern       | Category   | Problem Solved                                         | Typical Use Cases                                 |
| ------------- | ---------- | ------------------------------------------------------ | ------------------------------------------------- |
| **Factory**   | Creational | Centralized, flexible object creation                  | Parsers, UI elements, plugin systems              |
| **Observer**  | Behavioral | Notify multiple objects automatically of state changes | UI events, messaging systems, trading price feeds |
| **Singleton** | Creational | Ensure exactly one instance exists                     | Config, DB connection, logs, cache managers       |

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance  # protected

    def get_balance(self):
        return self._balance


# Create object OUTSIDE the class
acc1 = BankAccount("shrutika hinge", 10000)
print(acc1.name, acc1.get_balance())
class Employee:
    start_time = "10am"
    end_time = "4pm"


class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject


# create object OUTSIDE the class
t1 = Teacher("maths")
print(t1.subject, t1.start_time, t1.end_time)
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class Lion(Animal):
        def make_sound(self):
            print("rove")

            from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        print("roar")


class Cow(Animal):
    def make_sound(self):
        print("moo")


# create objects outside
lion = Lion()
lion.make_sound()

cow = Cow()
cow.make_sound()

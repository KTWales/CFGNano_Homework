"""

TASK 1

Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

"""

class CashRegister:
    total_items = []
    total_price = 0

    def __init__(self, item, price):

        # self.total_items = None #{'item': 'price'}
        # self.total_price = 0
        self.discount = 0.10
        self.item = item
        self.price = price

    def add_item(self, item,price):
        # pass
        self.total_items.append(self.item)
        self.total_price += self.price

    def remove_item(self):
        # pass
        self.item.remove(self.item)
        self.price.remove(self.price)


    def apply_discount(self):
        # pass
        total_price_discount = self.total_price * self.discount
        return total_price_discount

    def get_total(self):
        # pass
        self.total_price += self.price
        return total_price

    def show_items(self):
        # pass
        self.total_items.append(self.total_items + self.item)
        return total_items

    def reset_register(self):
        # pass
        self.item = item.clear()
        self.price = price.clear()
        self.total_price = total_price.clear()
        self.total_items = total_items.clear()
        self.discount = discount.clear()

    def show_details(self):
        print("Item: ", self.item)
        print("Price: ", self.price)
        print("Discount: ", self.discount)
        print("Total Price: ", self.total_price)
        print("Total Items: ", self.total_items)


# EXAMPLE code run:

# ADD
item1 = CashRegister('jeans',12.99)
print(item1)
print(item1.show_details())
item2 = CashRegister('top',5.99)
print(item2)
print(item2.show_details())

"""

TASK 2

Write a base class to represent a student. Below is a starter code. 
Feel free to add any more new features to your class. 
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student. 

"""

class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()

# class CFGStudent(<should inherit from Student>)
#     create new methods that manage student's subjects (add/remove new subject and its grade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)

class CFGStudent(Student):
    def __init__(self, name, age, id, subject, grade):
        super().__init__(name, age, id)
        self.subject = subject
        self.grade = grade

    def add_subject(self, subject, grade=0):
        self.subjects[subject] = grade

    def remove_subject(self, subject):
        self.subjects.pop(subject)

    def add_grades(self, subject, grade):
        self.subjects[subject] = grade

    def show_details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("ID: ", self.id)
        print("Subject: ", self.subject)
        print("Grade: ", self.grade)

x1 = CFGStudent('Jon',21, 'ID001', 'Maths','A')
x1.show_details()
x2 = CFGStudent('Dave',24, 'ID002', 'Software Engineering','B')
x2.show_details()
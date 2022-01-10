"""
TASK 1

Design a parent class called CFGStudent.

It should have general attributes like name, surname, age, email, student id
and methods to fetch student’s full name and student’s id.

Design a child class called NanoStudent, which  inherits from CFGStudent class.
This class should have exactly the same attributes as its parent class,
as well as an additional one called ‘specialization’ and course grades.

The child class ‘generate_id’ method should override its parent method to add the suffix ‘NANO’
in front of the id.

New methods ‘add_new_grade’ and ‘get_course_grades’ should be added.
You can use  it as a skeleton code for your classes OR adjust it and create your own.

SEE NOTES BELOW

"""
import random

class CFGStudent:

    def __init__(self, name, surname, age, email):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.student_id = random.randint(1000,10000)

    @staticmethod
    def generate_id():
        'your code goes here'
        'create a random new id, which is any number between 1,000 and 10,000'
        'return id as a string'
        "Example '8754' "
        return self.student_id

    def get_id(self):
        return '{}'.format(self.student_id)
        'fetch student id'

    def get_fullname(self):
        "Expected outcome should be 'Name Surname' "
        return '{} {}'.format(self.name, self.surname)


class NanoStudent(CFGStudent):

    def __init__(self, specialization, name, surname, age, email, course_grades=None, students=None ):
        super().__init__(name, surname, age, email)
        self.specialization = specialization

        if students is None:
            self.students = []
        else:
            self.students = students

        if course_grades is None:
            self.course_grades = []
        else:
            self.course_grades = course_grades

    @staticmethod
    def generate_id():
        'your code goes here'
        'create a random new id, which is a word NANO followed by any number between 1,000 and 10,000'
        'return id as a string'
        "Example 'NANO1234' "
        return 'NANO'+str(random.randint(1000, 10000))

    def add_new_grade(self, new_grade):
        'your code goes here'
        for course_grades in self.course_grades:
            self.new_grade = new_grade
        'update course_grades container'
        "Example: pass in a task name and its grade, so that both are added to course_grades"

    def get_course_grades(self):
        'your code goes here'
        'fetch course grades container and its values'
        for student in self.students:
            print('--> ' + student.name() + student.surname() + '--> ' + student.course_grades)


############################################

# Example run

s = CFGStudent('Anna', 'Smith', 18, 'anna@mail.com')  # do not pass ID, it should be generated automatically
print(s.get_fullname())
# returns 'Anna Smith'
print(s.student_id)
# returns '3868' or some other random number

cfg_s = NanoStudent('Software', name='Mia', surname='Papandopulu', age=20, email='mia@mail.com')
print(cfg_s.get_fullname())
# returns 'Mia Papandopulu'
print(cfg_s.get_id())
# returns 'NANO6180' or some other random number

cfg_s.add_new_grade('theory', 95)
cfg_s.add_new_grade('project', 78)
print(cfg_s.get_course_grades())
# returns {'theory': 95, 'project': 78}



"""
TASK 2

Given an index limit, find all corresponding Fibonacci values up to that limit in a sequence 
and return the sum of all even Fibonacci numbers. See more details in the task description in 
your assessment paper. 
"""
def even_fibonacci_sum(limit):
    #Fibonacci series
    fib = [0, 1]  # starting from 0 and 1
    for i in range(2, limit + 1):
        fib.append(fib[-1] + fib[-2])
    print('Fibonacci series: ', fib)

    #Even fiboancci series
    even = []
    for x in fib:
        if x % 2 == 0:
            even.append(x)
    print('Fibonacci even series: ', even)

    #Sum of even numbers
    print("Sum of even fibonacci series: ", sum(even))


##### TESTS ####

print(even_fibonacci_sum(limit=10))  # should be 44
print(even_fibonacci_sum(limit=15))  # should be 188
print(even_fibonacci_sum(limit=1))   # should be 0





"""
TASK 3

Validate subsequence. Use suggested tests below to check
correctness of your solution. 
"""

def is_valid_subsequence(array, sequence):
    len_array = len(array)
    len_seq = len(sequence)
    match = []
    for a in range(0, len_array, 1):
        for s in range(0, len_seq, 1):
            if sequence[s] == array[a]:
                match.append(sequence[s])
    if len(match) == len_seq:
        return True
    else:
        return False


#### TESTS ####

array1 = [5,1,22,25,6,-1,8,10]
sequence1 = [1,6,-1,-2]

print(is_valid_subsequence(array1, sequence1))  # FALSE


array2 = [5,1,22,25,6,-1,8,10]
sequence2 = [1,6,-1, 10]

print(is_valid_subsequence(array2, sequence2))  # TRUE


array3 = [5,1,22,25,6,-1,8,10]
sequence3 = [25]

print(is_valid_subsequence(array3, sequence3))  # TRUE



"""
TASK 4

WRITTEN ASSIGNMENT

Write a review on how 'class Employee' can be improved.
(See PDF document with the code example)
"""

# 1) Adding comments to each sub-section of the class, for example,
# before each "def" function there can be a brief summary of what this code does.
# 2) Depending on the company and how the employee table is utilised, maybe there can be a
# some fields added such as "date created" and "date inactive" and "date transferred".
# At this point the employee table only takes into consideration to automatically create a
# new employee row with details, and how to delete the employee details.
# Maybe the employee just transferred to another department and hasn't left the company.
# 3) The employee ID can be randomly generated so it is unique and not used multiple times.
# 4) If there was an ID that was reused, or a name entered multiple times, then an exception
# error handling message would be handy in this code.






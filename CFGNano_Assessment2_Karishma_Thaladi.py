"""  PYTHON AND MYSQL ASSESSMENT TEST - 2 hours  """


""" 1. Python theory questions """

# 1.	What is the program?
"""
Program is a collection of instructions written by a programmer/coder.
The program can then be executed with a click of a button.
"""
# 2.	What is the process?
"""
Process is when a computer program is being executed/in execution.
"""

# 3.	What is Cache?
"""
Cache is a small memory like RAM (random access memory)
It is built in a CPU.
"""
# 4.	What is Thread and Multithreading?
"""
Thread (also known as single thread) is when there is only one 
command that is processed at a time.
Multi-threading is when multiple lines of commands are processed within one 
process.
"""

# 5.	What is GIL in Python and how does it work?
""" 
GIL = Global Interpreter Lock 
Only one thread at a time can be executed in python.
"""
# 6.	What is Concurrency and Parallelism and what are the differences?
"""
Concurrency - when multiple computations are being run at the same time.
Parallelism - this is when multiple computations are separated into 
smaller chunks and run simultaneously.
Difference - during debugging of the code, it is very hard to debug in 
concurrency while it is somewhat simpler in parallelism
"""

# 7.	What do these stand for in programming: DRY, KISS, BDUF
"""
DRY - Don't Repeat Yourself
KISS - Keep It Simple and Straight / Keep It Simple, Silly
BDUF - Big Design Up Front
"""

# 8.	What is Garbage collector? How does it work?
"""
This is an automatic de-allocation of python objects 
(strings, lists, integers, etc).
A memory collector stores all the python objects while a garbage collector 
will automatically de-allocate them and free up some memory.
"""

# 9.	What are ‘deadlock’ and ‘livelock’ in a relational database?
"""
'Deadlock' is when all processes are block each other resulting in no progress.

'Livelock' is similar to 'deadlock' but doesn't necessarily block the entire process.
For example, in SQL, if a user is given read access but not write access to a database.
"""

# 10.	What is Flask and what can we use it for?
"""
Flask contains tools that allows the user/coder to build web applications.
It can be used to create a blog, webpages, calendars, etc.
"""



""" 2. Discuss the difference between Python 2 and Python 3 """
"""
Python 2 is the previous version of python programming and uses ASCII coding.
Python 3 is the most recent version and uses UTF-8 coding.

"""
""" 3. Write a function that can define whether a word is a Palindrome 
or not (a word, phrase, or sequence that reads the same backwards as 
forwards, e.g. madam) """

def Palindrome(word):
    reverse = word[::-1]
    if len(word) == 1:
        print("Length is 1, so it is a Palindrome of itself!")
    else:
        if reverse == word:
            print("{} is a Palindrome".format(word))
        else:
            print("{} is not a Palindrome".format(word))
# text = 'madam'
# Palindrome(text)



""" 4.	Write tests for the newly created Palindrome function.
Provide a brief explanation for your test case options. """
try:
    text = input('type in a word to check if it is a Palindrome: ')
except (TypeError):
    print("Please type a word and not digits.")
else:
    Palindrome(text)
"""
Try the Palindrome function, except there is a TypeError, then 
print "Please type a word and not digits."
else continue with running the Palindrome function
"""


""" 5. Agile methodology, Scrum: name at least 3 types of meetings that are 
exercised by Agile teams and describe the objective of each meeting. """

"""
Daily Scrum - this is a daily 15-minute or short meeting that updates
everyone in the Agile team on the progress of the sprint (i.e. goal).

Sprint review - this happens at the very end of the sprint.
Almost like an overview and also a discussion on what went well,
what could be improved for the future,
any further backlogs that may arise and how to tackle them.

Sprint planning - this is one of the early stage meeting where 
the scrum master, product owner, developpers have a planning meeting on the 
current sprint and its goals, and how to go about project planning it, 
delegating tasks, discussing any product backlogs, etc.
"""



""" 6.	Exception handling in Python, explain what each of the following blocks 
means in the program flow:
   
    try, except, else, finally 
"""

"""
Try: this is where your first attempt of your code is run in python
Except: this is where any errors that could arise are caught 
and any specific exception can be executed
Else: if there wasn't any exception, then this section of the code will run
Finally: this is the code that always runs no matter 
what happens in the previous 3 blocks (try, except and else)
"""


def TypeNetflixShow(name):
    if ',' in name:
        raise ValueError("Please remove any comma, question marks, exclamation marks and fullstops")

    if '!' in name:
        raise ValueError("Please remove any comma, exclamation marks and fullstops")

    if '?' in name:
        raise ValueError("Please remove any comma, question marks, exclamation marks and fullstops")

    if '.' in name:
        raise ValueError("Please remove any comma, exclamation marks and fullstops")

entered = False

try:
    name = input("Please enter your favourite Netflix show: ")
    TypeNetflixShow(name)

except ValueError:
    print("Invalid input")

else:
    with open("netflixshows.txt", 'a+') as file:
        file.write("{}".format(name))
    entered = True

finally:
    if entered:
        print("Thank you for your input")
    else:
        print("Please type your favourite Netflix show again")



""" 7. How can we connect a Python program (process) with a database? 
Explain how it works and how do we fetch / insert data into DB tables from a python program. """

"""
A Python program is connected to the SQL database using the python library: 
import mysql.connector
and feeding the database hostname, username and password
Once done, the Python program can speak to the relevant 
database and fetch/insert data into database tables from a python program.
"""


""" 
8. Given two SQL tables below: authors and books (!!!PLEASE CHECK THE ASSESSMENT2 DOCUMENT FOR THE TABLES!!!)
●	 The authors dataset has 1M+ rows
●	 The books dataset also has 1M+ rows 
Create an SQL query that shows the TOP 3 authors who sold the most books in total!

"""

"""
SELECT DISTINCT a.author_name FROM authors as a
WHERE (
    SELECT * FROM books as b
    ORDER BY b.sold_copies DESC
)
LIMIT 3;
"""




"""
9.	TWO NUMBER SUM: 

●	Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. 
    If any two numbers in the input array sum up to the target sum, the function should return 
    them in an array, in any order. If no tWo numbers sum up to the target sum, the function should 
    return an empty array.
    
●	Note that the target sum has to be obtained by summing two different integers in the array. 
    You cannot add a single integer to itself in order to obtain the target sum.
    
●	You can assume that there will be at most one pair of numbers summing up to the target sum. 

Sample Input: 
    numbers = [3, 5, -4 ,8, 11, 1, -1, 6]  
    target_sum = 10
    
Sample Output: 
    [-1, 11] the numbers can be in any  order, it does not matter. 

"""

def TwoNumberSum(my_nums, target):
    n = len(my_nums) # length of the array
    result = []
    used_indices = []
    for i in range(0,n):
        for j in range(0,n):
            if i != j and my_nums[i] + my_nums[j] == target:
                # makes sure the same indices aren't used and that they add up
                if i not in used_indices and j not in used_indices:
                    # prevents it from adding the reversed set of indices
                    used_indices.append(i)
                    used_indices.append(j)
                    result.append([my_nums[i], my_nums[j]])


    if len(result) == 0: # checks to make sure that result list is zero i.e. no results found
        print("No result found: ", result)
    else:
        print("Answer:", result)

my_numbers = [3,5,-4,8,11,1,-1,6]
target_sum = 10
TwoNumberSum(my_numbers,target_sum)

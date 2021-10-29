#CFG - Homework 4
# TASK 1 - Question 1
"""
GIT WORKFLOW FUNDAMENTALS
·        Working Directory - also known as working tree, this is a local directory on the filesystem that is associated with git repository. This is the first one that one sees when they look at a folder containing git repository. It may contain exactly the same content as a branch in the repository, but it can also be completely different, depending on the changes that are made to it. Git is aware of everything that happens inside the working tree, but it only tracks the files that it is told to track. By running the command git status, this will show you 2 things: files in working tree and files in staging area.
·        Staging Area - this is also known as index. The Git index sits between the working directory (working tree) and the Git repository. It allows the user to precisely control what Git must track, what it must include when the user decides to create a commit, and so on. When adding/removing content to/from the index, we are often talking about staging/unstaging changes.
·        Local Repo (head) - this is everything that is in the .git directory. it will contain all the checkpoints or commits. It is the area that saves everything so it is recommended to not delete it. The command git commit takes all changes in the staging area, wraps them together and puts them in the local repository. A commit is simply a checkpoint telling git to track all changes that have occurred up to this point using our last commit as a comparison. After committing, your Staging Area will be empty.
·        Remote repo (master) - Git local repository is the one on which we will make local changes, typically this local repository is on our computer. Git remote repository is the one of the server, typically a machine situated at 42 miles away and that is accessible for all team members - most likely on the internet or on a local network.

WORKING DIRECTORY STATES:
·        Staged - If a particular version of a file has been modified and was added to the staging area, it is staged.
·        Modified - If a particular version of a file was changed since it was checked out but has not been staged, it is modified.
·        Committed - If a particular version of a file is in the Git directory, it’s considered committed.

GIT COMMANDS:
·        Git add - this can be used to track a new file. For instance, to track README file, the following can be run: git add README. Also, when we create, modify or delete a file, these changes only take place in the local directory and won’t be included in the next commit. this is when git add command can be used.
·        Git commit - this will commit the file that is staged. A very popular command, this is like setting a checkpoint in the development process which you can go back to later if needed. Git commit saves the changes only locally.
·        Git push - this is run when you have a project that you want to share, and you push it upstream. Git push uploads your project commits to the remote server (remote repository). It is important that the changes are committed before running git push.
·        Git fetch - to get data from remote projects, this can be run. It will fetch all the changes on the server that you don’t have yet, it will not modify your working directory at all. It will simply get the data for you and let you merge it yourself.
·        Git merge - Once the development in your branch is complete and everything works well, the final step is to merge the branch with the parent branch (that is the dev or master). This is when git merge is run.
·        Git pull - this is a git fetch followed by git merge in most cases. It will look up what server and branch your current branch is tracking, fetch from that server and then try to merge in that remote branch. Generally it’s advised to simply use the fetch and merge commands explicitly as the magic of git pull can often be confusing.

"""

# TASK 2 - Question 1

balance = 100
attempts = 3
user_pin = 1234

while attempts != 0:
    try:
        user_input = int(input("Welcome, please enter your PIN: "))

# if PIN is incorrect
        if user_input != user_pin:
            attempts -= 1
            print("Wrong PIN number. You have {} attempts left".format(attempts))
            break

        else:
            # go to next step
            user_choice = int(input("Please select from the following options:\n1.Display account balance\n2.Cash Withdrawal\n3. Cancel\n"))

# Display Account Balance
            if user_choice == 1:
                print("Your account balance is £{}".format(balance))
                user_choice = input("Would you like another service? Y/N ")
                if user_choice == 'N':
                    print("Thank you and have a wonderful day!")
                    break
                else:
                    continue

# Cash Withdrawal
            if user_choice == 2:
                user_w = int(input("Please enter the amount you would like to withdraw: "))
                if user_w > balance:
                    user_end = input("Sorry, you do not have sufficient funds in your account.\nWould you like to select another amount? Y/N ")
                    if user_end == 'N':
                        print("Thank you and have a wonderful day!")
                        break
                    else:
                        continue
                else:
                    balance -= user_w
                    print("£{} has been withdrawn. Your account balance is now £{}.".format(user_w,balance))

# Cancel/End process
        user_exit = input("Would you like to select another service? Y/N ")
        if user_exit == 'N':
            print("Thank you and have a wonderful day!")
            break
        else:
            continue

    except ValueError:
        print("Wrong PIN number. You have {} attempts left".format(attempts))
        user_input = int(input("Welcome, please enter your PIN: "))
        continue

# TASK 3 - Question 1

def userpin(digits, attempts):

    while attempts != 0:
        digits = int(input("Welcome, please enter your PIN: "))

        if digits <= 1000 or digits >= 9999:
            raise ValueError

        # if PIN is incorrect
        if digits != user_pin:
            attempts -= 1
            print("Wrong PIN number. You have {} attempts left".format(attempts))
            break


def userbalance(user_choice):
# Display Account Balance

    # go to next step
    user_choice = int(input("Please select from the following options:\n1.Display account balance\n2.Cash Withdrawal\n3. Cancel\n"))

    try:
        if user_choice != 1 or user_choice != 2 or user_choice != 3:
            raise ValueError
            break
    except:
        if user_choice == 1:
            print("Your account balance is £{}".format(balance))
            user_choice = input("Would you like another service? Y/N ")
            if user_choice == 'N':
                print("Thank you and have a wonderful day!")
                break


def userwithdrawal(balance,user_w):
    try:
        if balance >= user_w:
            break
    except ValueError:
        print("Please enter the amount you would like to withdraw")
        continue


import unittest
from HW4_Karishma_Thaladi import userpin, userbalance, userwithdrawal

class TestATM(unittest.TestCase):

    def test_user_pin(self):
        expected = 1234
        result = userpin(1234)
        self.assertEqual(expected, result)

    def test_out_of_range(self):
        self.assertRaises(ValueError, userpin, 0000)

    def test_cash_withdrawal(self):
        if userwithdrawal(balance,user_w):
            break
        expected = balance - user_w
        result = calc.subtract(balance, user_w)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.CFGNano_HW4()
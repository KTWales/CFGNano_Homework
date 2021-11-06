HOMEWORK WEEK 5-6
(handout for students)


TASK 1 (Agile Techniques)

Question 1
Complete definitions for Scrum related key terminology provided below.
SCRUM CEREMONIES
·        Product backlog refinement - this is an on-going process where the product owner and development team work in collaboration to ensure the items on the product backlog are understood in the same way, they have a relative complexity and effort for their implementation. 
·        Sprint planning. - this is an event that kicks off the sprint; it is one of 5 parts of Scrum. It defines what can be delivered in the sprint and how that work will be achieved. The product owner describes the goal (Sprint Goal) and what the backlog items contribute to that goal. 
·        Daily scrum. - this is term used for a daily 15-minute event for the developers of the scrum team; it is held at same time and place which reduces complexity. The purpose of this daily scrum is to inspect progress towards the Sprint Goal and adapt to any Product Backlogs that needs to be adjusted into the upcoming planned work.
·        Sprint review. - this event takes place at the end of the sprint and the purpose of this review is to inspect, evaluate the outcome of the sprint, and consider any adaptations for the product’s future. The scrum team will present the findings of their work to key stakeholders and progress towards the product goal.
·        Sprint retrospective - this is an essential part of the scrum framework where a meeting is held at end of the sprint to discuss what went well during previous sprint cycle and what can be improved for the next sprint. It is useful for developing, delivering, and managing complex projects.
 
 SCRUM ROLES
·        ScrumMaster - the role of a scrum master is to ensure the scrum team lives by the values/practices/framework of scrum; coach the scrum team to focus and do their best work and be open to opportunities to improve the team’s workflow. 
·        Product Owner - this is a project’s key stakeholder and responsible to convey the vision of what they wish to build to the scrum team. They are accountable for maximising the value of the product resulting from the work of the scrum team.
·        Development Team - this is the integral part of a bigger scrum team. It comprises professionals who deliver/create the product in a sprint.
 
Question 2
 
You are leading a development team that was given a task to create a new yoga booking system.

High level description of the system is as follows:
 
·        It has a very simple interface to accept user input (bookings) and display classes information
·        All bookings, appointments, schedules etc should be stored in a SQL database.
·        There is a ‘backend’ system that should be written in Python to handle the logic and manage the data flow. 
Your team has two weeks to build a simple prototype that will be shown to the client to seek their feedback and discuss further enhancements.
 
TASK
·        Break this task into smaller stories (chunks of work) for the team to work on.
·        Assume that one person works on one task.
·        Mark tasks that can be worked on in parallel and perhaps those that need to be worked on in particular order.

Answer:
Leading a development team of 3 people, I will assign the following tasks to the individuals:
Person 1: assigned to take care of SQL database and tables setup (tables include: all bookings, appointments, schedules etc). Also, to create unique primary and foreign keys that link the tables together to create a relational database.
Person 2: assigned to set-up the simple user interface that requests the user to add input details such as Random number generator for booking ID or reference, Name, Day, Time, Date, Location, Contact Details, Yoga instructor, etc, and define classes and any unit testing required.
Person 3: assigned to take care of the “backend” system written in Python. Work in parallel with both Person 1 and 2 to ensure the data is flowing from the user interface and SQL database tables and there is no product backlog concerns.
In two weeks (excluding the weekend leaves 10 woking days), Person 1, 2 and 3 will have daily scrum 15-minute meetings with scrum master to discuss the process flow of the data from user input and SQL database and the expected outcomes. If there are any product backlogs like the entry of the user is not characters or invalid with symbols, etc, these will have been discussed and a work-around also discussed.
In the first 5 days, the team will focus on creating an empty SQL database and tables; simple Python code and also carry out some unit testing in Python. The following 2 days will be spent testing with dummy data and resolving any further issues/concerns that had cropped up.
Following 2 days, the team will create various scenarios of dummy data to be used to showcase how the booking system works and requests scrum master to provide any coaching if necessary at this stage.
And on final day 10, the developing team presents the yoga booking system to the key stakeholder, that is, the product owner. During this presentation, the product owner may add their evaluation and/or concerns, which will be considered as part of the next sprint goal.


TASK 2 (SQL)

Question 1
Design a cinema booking system.
Think how you would approach the problem and what are potential ways of solving it?


You do not need to write actual code, but describe the high-level approach:
·        Draw a list of key requirements - List of movies, Dates and Timings of the movies, Location of the bookings, Number of seats in the cinema theatre, Number of seats occupied, Number of seats not occupied, Cost of each seat, Prices based on child, adult and elderly; customer contact details, customer receipt with booking confirmation
·        What are your main considerations? - customer booking twice or more by accident for the same seat or different seats, customer typing incorrect movie name, customer entering incorrect contact details, customer giving incorrect dates and timings for the movies
·        What would be your common or biggest problems? - Common problems would be mis-spelled words and also invalid entries such as Name = “ajgfbyue”. Two users could be assigned the same booking ID. If the entries are all upper case or lower case or include numbers or camel-form of typing such as “hElen”.
If a user adds invalid entries then these details would need to be immediately flagged. Also, if the user typed a certain field incorrectly, the user interface must request the user to re-type the correct response. Using .lower() will resolve any text formatting issues. 
·        What components or tools would you potentially use? - Python for building a user interface and building a unit testing backend system; SQL database and tables for storing cinema booking details and also customer details.
·        You are welcome to draw a diagram (a very simple one) for the process flow to explain how  it is going to work.


SQL 			>> 		Python Interface 	>> 	Online booking system
SQL Relational Database
Online booking system
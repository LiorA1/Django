
# ORM Queries - 
 A django Project that used me as a learning the ORM.  
 I taken past DB that was built with SQL, and build it with Django ORM and applied past Queries using the ORM.
 
### How to load the data ?
1. open the console
2. migrate all the tables, using: "*python manage.py migrate --run-syncdb*"
3. load the data from the json file, using: "*python manage.py loaddata datadump.json*"
4. open the shell (using:"*python manage.py shell*")
5. import all the models ("*from store.models import \* *")
6. start query the database, to answer the following questions.
 
### Questions are:
1. Find all customers that their id's numbers are bigger than all of texses customers id's. return id, fname, lname.
2. Find all customers that theirs address contains 'x' or 'X'
3. Find all Customers that did orders only in the 1994 year.
4. What are the products names and descriptions, that was ordered by customers that theirs first name starts with 'L' ?
5. Do the former question, but insted of 'L', use your own first letter name.
6. Which customers didnt make any order ? (return id, first name, last name)
7. Which customers didnt order a product that its name contains the word 'shirt', but did at least one order. (return id, fname, lname)
8. For Which customers (id, fname, lname), employee 299 was the only employee that handle theirs orders ?
9. For each departement find its id, name, number of employees and theirs average salary. 
10. Find the number of orders that each employee handled. (return employee id, fname, lname and the orders number)
11. What is the date of the last order ?
12. From which state most of the customers ?
13. Find the customers that employee 129 handle at least one order of. (id, fname, lname and total orders number)


### Additional Questions:
1. find the employee with the higher salary
2. find the employee that handled most of the orders
3. find the total price of each order
4. 

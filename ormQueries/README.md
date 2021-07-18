
# ORM Queries - 
 A django Project that used me as a learning the ORM.  
 I taken past DB that was built with SQL, and build it with Django ORM and applied past Queries using the ORM.
 
### How to load the data ?
1. open the console
2. migrate all the tables, using: "*python manage.py migrate --run-syncdb*"
3. load the data from the json file, using: "*python manage.py loaddata datadump.json*"
4. open the shell (using:"*python manage.py shell*")
5. import all the models ("*from store.models import \**")
6. start query the database, to answer the following questions.
 
### Questions are:
1. Find customers that their id's numbers are bigger than all of texas's customers id's. return id, fname, lname.
2. Find customers that theirs address contains the letter 'x' or 'X'
3. Find Customers that each order is from 1994 (year). (return id, first name and last name)
4. What are the products names and descriptions, that was ordered by customers that theirs first name starts with 'L' ? (results names need to be in a asc order )

5. Which customers didnt make any order ? (return id, first name, last name)
6. Which customers didnt order a product that its name contains the word 'shirt', but order other products. (return id, fname, lname)
7. For Which customers (id, fname, lname), employee 299 was the only employee that handle theirs orders ?
8. For each departement find its id, name, number of employees and theirs average salary. 
9. Find the number of orders that each employee handled. (return employee id, fname, lname and the orders number)
10. What is the date of the last order ?
11. From which state most of the customers ?
12. Find the customers that employee 129 handle at least one order of. (id, fname, lname and total orders number)


### Additional Questions:
0. Find Orders that been made in the last 60 days
0. Find Customers that ordered more than 3 products (quantity)
0. Find Customers that Ordered more than 3 products, in the last two months.


1. find the employee with the higher salary
2. find the employee that handled most of the orders

3. find the total price of each order
4. Do the forth question, but insted of 'L', use your own first letter name.

5. find how many items of each product was selled by now

6. find how much each customer spent
7. Classify Customers by purchases total: if more than 4000 USD - label as "prefered client". else - "regular client".
8. Classify Customers by purchases total: if more than the average total - label as "prefered client". else - "regular client".
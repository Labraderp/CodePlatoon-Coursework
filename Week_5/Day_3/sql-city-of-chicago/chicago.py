# Your code goes here!
import psycopg2, csv

# ========== HELPER FUNCTIONS ========== #

def create_employee(fname, lname, job, time, dept, sal):
    if not type(sal) == int or sal < 0:
        print("Salary must be a positive integer")
        return
    
    if time == 'Hourly':
        sal = sal * 2000

    inject = f"INSERT INTO employees (first_name, last_name, job_title, full_or_part_time, department, annual_salary) "
    inject += f"VALUES ('{fname}', '{lname}', '{job}', '{time}', '{dept}', '{sal}');"
    return inject

# ========== HELPER VARIABLES ========== #

employee_table_create = "CREATE TABLE employees (first_name varchar, last_name varchar, job_title varchar, full_or_part_time varchar, department varchar, annual_salary integer);"

# ========== MAIN FUNCTION ========== #


connection = psycopg2.connect(f"dbname=chicago_salaries")
cur = connection.cursor()

cur.execute("DROP TABLE IF EXISTS employees")
cur.execute(employee_table_create)

with open('/var/lib/postgresql/chicago.csv', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file, skipinitialspace=True)
    for row in csv_reader:
        name = row['Name']
        job_title = row['Job Titles']
        


# tim = create_employee('Tim', 'McVey', 'Bomber', 'Full Time', 'Security', 180000)
# jack = create_employee('Jack', 'Horner', 'Evil Villain', 'Hourly', 'Magic Crap', 25)

# cur.execute(tim)
# cur.execute(jack)

connection.commit()
connection.close()



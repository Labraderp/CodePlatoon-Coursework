import psycopg2

connection = psycopg2.connect(f"dbname=class_roster")
cur = connection.cursor()

student_table_creation_query = "CREATE TABLE students (id serial PRIMARY KEY, name varchar(255), favorite_food varchar(255));"
locker_table_creation_query = "CREATE TABLE locker (id serial PRIMARY KEY, name varchar(255), favorite_food varchar(255));"

cur.execute("DROP TABLE IF EXISTS students")
cur.execute(student_table_creation_query)

# name = "Carol"
# food = "tuna"

# inject = f"INSERT INTO students (name, favorite_food) VALUES ('{name}', '{food}');"
# cur.execute(inject)

connection.commit()
connection.close()


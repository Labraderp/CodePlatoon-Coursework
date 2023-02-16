from . import School, Student, Staff, Person

school = School('Ridgemont High') 

student_info = {'name' : 'Diana', 'password' : 'password', 'school_id' : 12345, 'age' : 17, 'role' : 'Student'}
Student(**student_info)
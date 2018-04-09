# report_classlist.py
# CSC 370 - Spring 2018 - Starter code for Assignment 4
#
# The code below generates a mockup of the output of report_classlist.py
# as specified in the assignment. You can copy and paste the functions in this
# program into your solution to ensure the correct formatting.
#
# B. Bird - 02/26/2018

import psycopg2, sys

psql_user = 'rhysl' #Change this to your username
psql_db = 'rhysl' #Change this to your personal DB name
psql_password = 'V00818835' #Put your password (as a string) here
psql_server = 'studdb1.csc.uvic.ca'
psql_port = 5432

conn = psycopg2.connect(dbname=psql_db,user=psql_user,password=psql_password,host=psql_server,port=psql_port)
cursor = conn.cursor()

def print_header(course_code, course_name, term, instructor_name):
	print("Class list for %s (%s)"%(str(course_code), str(course_name)) )
	print("  Term %s"%(str(term), ) )
	print("  Instructor: %s"%(str(instructor_name), ) )
	
def print_row(student_id, student_name, grade):
	if grade is not None:
		print("%10s %-25s   GRADE: %s"%(str(student_id), str(student_name), str(grade)) )
	else:
		print("%10s %-25s"%(str(student_id), str(student_name),) )

def print_footer(total_enrolled, max_capacity):
	print("%s/%s students enrolled"%(str(total_enrolled),str(max_capacity)) )

if len(sys.argv) < 3:
	print('Usage: %s <course code> <term>'%sys.argv[0], file=sys.stderr)
	sys.exit(0)
	
course_code, term = sys.argv[1:3]

cursor.execute("select course_code,course_name,term_code,instructor_name from course_offerings where course_code = %s and term_code = %s;",(course_code,term))

row = cursor.fetchone()

print_header(row[0],row[1],row[2],row[3])

cursor.execute("""select student_id,name,final_grade from students natural join enrollments where course_code = %s and term_code = %s;""",(course_code,term))

rows_found = 0
while True:
	row = cursor.fetchone()
	if row is None:
		break
	rows_found += 1
	print_row(row[0],row[1],row[2])

cursor.execute("""select (select count(*) from enrollments where course_code = %s and term_code = %s), max_cap from course_offerings where course_code = %s and term_code = %s;""",(course_code,term,course_code,term))

row = cursor.fetchone()

print_footer(row[0],row[1])

cursor.close()
conn.close()

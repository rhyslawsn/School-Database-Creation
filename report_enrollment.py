# report_enrollment.py
# CSC 370 - Spring 2018 - Starter code for Assignment 4
#
# The code below generates a mockup of the output of report_enrollment.py
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

def print_row(term, course_code, course_name, instructor_name, total_enrollment, maximum_capacity):
	print("%6s %10s %-35s %-25s %s/%s"%(str(term), str(course_code), str(course_name), str(instructor_name), str(total_enrollment), str(maximum_capacity)) )

# Mockup: Print some data for a few made up classes
cursor.execute("select term_code, course_code, course_name, instructor_name,(select count(student_id) from enrollments where enrollments.course_code = course_offerings.course_code and enrollments.term_code = course_offerings.term_code), max_cap from course_offerings order by term_code;" )


		
rows_found = 0
while True:
	row = cursor.fetchone()
	if row is None:
		break
	rows_found += 1
	print_row(row[0], row[1], row[2], row[3], row[4], row[5])


cursor.close()
conn.close()

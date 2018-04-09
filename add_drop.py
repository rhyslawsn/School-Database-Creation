# add_drop.py
# CSC 370 - Spring 2018 - Starter code for Assignment 4
#
#
# B. Bird - 02/26/2018

import sys, csv, psycopg2

if len(sys.argv) < 2:
	print("Usage: %s <input file>",file=sys.stderr)
	sys.exit(0)
	
input_filename = sys.argv[1]

# Open your DB connection here

with open(input_filename) as f:
	for row in csv.reader(f):
		if len(row) == 0:
			continue #Ignore blank rows
		if len(row) != 5:
			print("Error: Invalid input line \"%s\""%(','.join(row)), file=sys.stderr)
			#Maybe abort the active transaction and roll back at this point?
			break
		add_or_drop,student_id,student_name,course_code,term = row
		
		#Do something with the data here
		#Make sure to catch any exceptions that occur and roll back the transaction if a database error occurs.
		
		if add_or_drop == 'ADD' or add_or_drop == 'DROP':
			pass # Nothing to see here folks ...
		else:
			print("Error: Invalid input for add_or_drop")
			print(row)
			#Maybe abort the active transaction and roll back at this point?
			break
		if len(student_id) != 9:
			print("Error: Invalid input for add_or_drop")
			print(row)
			#Maybe abort the active transaction and roll back at this point?
			break
		if len(student_name) > 255:
			print("Error: Invalid input for add_or_drop")
			print(row)
			#Maybe abort the active transaction and roll back at this point?
			break
		if len(course_code) > 10:
			print("Error: Invalid input for add_or_drop")
			print(row)
			#Maybe abort the active transaction and roll back at this point?
			break
		if term[-2:] == '01' or term[-2:] == '05' or term[-2:] == '09':
			pass # Nothing to see here folks ...
		else:
			print("Error: Invalid term number")
			print(row)
			#Maybe abort the active transaction and roll back at this point?
			break
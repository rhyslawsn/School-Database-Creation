# create_courses.py
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
try:
    os.system("ssh rhysl@studdb1.csc.uvic.ca -L -p 22")
except:
    print("Error: Unable to connect to the database")

with open(input_filename) as f:
	print("Opened: " + input_filename)
	for row in csv.reader(f):
		if len(row) == 0:
			continue #Ignore blank rows
		if len(row) < 4:
			print("Error: Invalid input line \"%s\""%(','.join(row)), file=sys.stderr)
			#Maybe abort the active transaction and roll back at this point?
			break
		code, name, term, instructor, capacity = row[0:5]
		prerequisites = row[5:] #List of zero or more items
		
		#Do something with the data here
		#Make sure to catch any exceptions that occur and roll back the transaction if a database error occurs.
		
		# Catch constraint violations here
		if len(code) > 10:
			print("Error: Invalid input for code")
			print(row)
			#Maybe abort the active transaction and roll back at this point?
			break
		if len(name) < 1 or len(name) > 128:
			print("Error: Invalid input for name")
			print(row)
			#Maybe abort the active transaction and roll back at this point?
			break
		if len(instructor) < 1:
			print("Error: Invalid input for instructor")
			print(row)
			#Maybe abort the active transaction and roll back at this point?
			break
		if len(instructor) < 1:
			print("Error: Invalid input for instructor")
			print(row)
			#Maybe abort the active transaction and roll back at this point?
			break
		if int(capacity) < 1:
			print("Error: Invalid input for capacity")
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
# Task5_Q14
# ABCXYZ company has up to 100 employees.The company decides to create a unique identification number (UID) for each of its employees.
# The company has assigned you the task of validating all the randomly generated UIDs.
# A valid UID must follow the rules below:

   # It must contain at least 2 uppercase English alphabet characters.
   # It must contain at least 3 digits (0 - 9).
   # It should only contain alphanumeric characters (a - z, A - Z & 0 - 9).
   # No character should repeat.
   # There must be exactly 10 characters in a valid UID.

import re
for _ in range(int(input().strip())):
    valid = True
    id = input().strip()
    if re.match(r'[a-zA-Z0-9]{10}', id) == None:
        valid = False
    elif re.search(r'([a-zA-Z0-9]{1}).*\1{1}', id) != None:
        valid = False
    elif re.search(r'[0-9]{1}.*[0-9]{1}.*[0-9]{1}', id) == None:
        valid = False
    elif re.search(r'[A-Z]{1}.*[A-Z]{1}', id) == None:
        valid = False
    if valid:
        print("Valid")
    else:
        print("Invalid")
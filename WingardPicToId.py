import os
import csv
import re

# Read the students.csv file and create a dictionary with last name and first name as keys and student_id as the value
students = {}
with open('students.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        students[row['Last_name'] + '_' + row['First_name']] = row['Student_id']

# Create a new folder for the student ID pictures
if not os.path.exists('StudentIdPictures'):
    os.makedirs('StudentIdPictures')

# Keep track of duplicates
duplicates = []

# Iterate through the files in the Student Name Pictures folder
for filename in os.listdir('Student Name Pictures'):
    if filename.endswith('.jpg'):
        # Search the file name for a pattern of last name _ first name
        match = re.search(r'(^.*)_([A-Za-z]+)', filename)
        if match:
            name = match.group(1) + '_' + match.group(2)
            if name in students:
                # Rename the file and move it to the new folder
                os.rename('Student Name Pictures/' + filename, 'StudentIdPictures/' + students[name] + '.jpg')
                # Remove the name from the dictionary so we know it's been used
                students.pop(name)
            else:
                # If the name is not in the students.csv file
                duplicates.append(name)

# Write the duplicates to an error.csv file
with open('error.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['duplicate_name'])
    for duplicate in duplicates:
        writer.writerow([duplicate])
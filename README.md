# Wingard_Picture_Change
# Takes the clever (or any) students.csv and uses the Last_name, First_name and Student_id headers to search a folder named "Student Name Pictures" with all the .jpg pictures in it. 
# When it finds a name in one of those file names it gets the ID number for that student and puts the file in a different folder with only the id number for that filename. 
# It uses Last_name then First_name with an underscore in the middle for the search and ignores the rest of the filename since this is how Wingard formats the file names.
#if there's an error it will write it to an errors csv and the picture wil remain in the original folder.
# Open cmd and navigate to the folder you created where both the students.csv file and Student Name Pictures folder (the one with all the pictures in it) are copied and run the script there.

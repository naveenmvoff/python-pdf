# Given a CSV file with student names and scores, find the student with the highest score.

import csv

csvfile = r"C:\WORKS\Learning\Python Learn\python-pdf\day_8\2high_score\csvfile.csv"

highscore = 0
student_name = ""

with open(csvfile, newline='') as file:
    reader = csv.DictReader(file)
    for i in reader:
        score = int(i['mark'])  # for converting integer
        if score > highscore:
            highscore = score
            student_name = i['name']
            
print(f"The student {student_name} got the {highscore}, This is the highest score")


# The Code with error handling
"""
import csv
import os

csvfile = r"C:\WORKS\Learning\Python Learn\python-pdf\day_8\2\csvfile.csv"

highscore = 0
student_name = ""

# Check if the file exists
if not os.path.exists(csvfile):
    print("Error: CSV file not found.")
else:
    try:
        # Open and read the CSV file
        with open(csvfile, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Print each row for debugging
                print(f"Row: {row}")
                
                # Convert 'mark' to integer and check if it's the highest
                score = int(row['mark'])
                if score > highscore:
                    highscore = score
                    student_name = row['name']
                    
        # Final output
        if student_name:
            print(f"The student with the highest score is {student_name} with a score of {highscore}.")
        else:
            print("No data found in CSV.")
            
    except KeyError as e:
        print(f"Error: Missing column in CSV - {e}")
    except ValueError:
        print("Error: Ensure all scores are valid integers.")
    except Exception as e:
        print(f"Unexpected error: {e}")

"""
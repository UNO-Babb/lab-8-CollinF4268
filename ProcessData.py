#ProcessData.py
#Name: Collin Frederick 
#Date: 4/6/25
#Assignment: Student list

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  for line in inFile:
    parts = line.strip().split()

    # Skip lines that are too short
    if len(parts) < 7:
      continue

    # Extract fields from fixed positions
    first = parts[0]
    last = parts[1]
    email = parts[2]
    student_id = parts[3]
    dob = parts[4]
    year = parts[5]
    
    # Major may be multiple words, so we join everything else
    major = " ".join(parts[6:])

    # Create User ID: first initial + last name (+ X if short) + last 3 digits of student ID
    user_id = first[0].lower() + last.lower()
    if len(last) < 5:
      user_id += "X"
    user_id += student_id[-3:]

    # Convert year to abbreviation
    if year == "Freshman":
      year_abbr = "FR"
    elif year == "Sophomore":
      year_abbr = "SO"
    elif year == "Junior":
      year_abbr = "JR"
    elif year == "Senior":
      year_abbr = "SR"
    else:
      year_abbr = "NA"

    # Format major-year string
    major_year = major[:3].upper() + "-" + year_abbr

    # Build CSV line
    csv_line = last + "," + first + "," + user_id + "," + major_year + "\n"

    # Write to the output file
    outFile.write(csv_line)

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

if __name__ == '__main__':
  main()

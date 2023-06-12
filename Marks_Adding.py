import csv
# Dictionary to store the roll number and total marks
roll_marks = {}

# Read data from the input CSV file
with open('data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    
    # Skip the header row
    header = next(csv_reader)
    
    # Process each row
    for row in csv_reader:
        roll_number = row[0]
        marks = int(row[1])
        
        # Update the total marks for the roll number
        if roll_number in roll_marks:
            roll_marks[roll_number] += marks
        else:
            roll_marks[roll_number] = marks

# Write the processed data to a new CSV file
with open('processed_data.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    
    # Write the header row
    csv_writer.writerow(header)
    
    # Write the roll number and total marks for each entry
    for roll_number, marks in roll_marks.items():
        csv_writer.writerow([roll_number, marks])

print("Data processing completed.")
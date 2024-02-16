import csv

csv_file_path = 'serial_mappings.csv'

# Read the CSV file
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    rows = list(csv_reader)

# Remove rows with 'Mapping' column equal to '*'
filtered_rows = [row for row in rows if row['Mapping'] != '*']

# Write the modified data back to the CSV file
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=csv_reader.fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(filtered_rows)

print("Mappings with '*' removed from the CSV file.")
import serial
import csv

# Set the serial port and baud rate
serial_port = 'COM5'
baud_rate = 115200
last_received_data = None

# Open the serial port
ser = serial.Serial(serial_port, baud_rate, timeout=1)

# Create a CSV file to store mappings
csv_file_path = 'serial_mappings.csv'
csv_header = ['Received_Value', 'Mapping']
csv_exists = False

try:
    # Check if the CSV file already exists
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_exists = any(row for row in csv_reader)

    # If the CSV file doesn't exist, create it with the header
    if not csv_exists:
        with open(csv_file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(csv_header)

    while True:
        data = ser.readline().strip()

        if data != last_received_data:
            print("Received data (hex):", data)

            # Check if the mapping exists in the CSV file
            with open(csv_file_path, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                mapping_found = any(row['Received_Value'] == data for row in csv_reader)

            if not mapping_found:
                # If the mapping doesn't exist, allow user input and store in CSV
                new_mapping = input("Enter the mapping for the received value: ")
                with open(csv_file_path, 'a', newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow([data, new_mapping])

            last_received_data = data

except KeyboardInterrupt:
    # Close the serial port when the program is terminated
    ser.close()
    print("\nSerial port closed.")
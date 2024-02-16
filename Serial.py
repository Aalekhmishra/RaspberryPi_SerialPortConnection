import serial

# Set the serial port and baud rate
serial_port = 'COM5'
baud_rate = 115200
last_received_data = None

# Open the serial port
ser = serial.Serial(serial_port, baud_rate, timeout=1)

try:
    while True:
        # Read data from the serial port
        data = ser.readline()

        if data != last_received_data:
        # Print the received data as bytes
            print("Received data (bytes):", data)

        # If you want to decode the bytes to a string
            try:
                decoded_data = data.decode('utf-8').strip()
                print("Received data (decoded):", decoded_data)
                last_received_data = data
            except UnicodeDecodeError as e:
                print(f"Error decoding data: {e}")

except KeyboardInterrupt:
    # Close the serial port when the program is terminated
    ser.close()
    print("\nSerial port closed.")

import serial
import pyautogui

serial_port = 'COM5'
baud_rate = 115200

ser = serial.Serial(serial_port, baud_rate, timeout=1)
                    
try:
    while True:
        # Read data from the serial port as bytes
        data = ser.readline()

        # Print the raw byte values
        print("Received data (raw bytes):", data)

        # Emulate keypress based on received bytes
        if data == b'\x82\xfc':
            pyautogui.press('w')
            print("Emulated Left Arrow Press")
        elif data == b'\x8c\xfc':
            pyautogui.press('x')
            print("Emulated Right Arrow Press")
        
except KeyboardInterrupt:
    ser.close()
    print("\nSerial port closed.")

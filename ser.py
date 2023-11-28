import serial
import csv

# Establish serial connection with the Arduino
arduino = serial.Serial('COM1', 115200, timeout=1)  # Change 'COM1' to your Arduino's port

# Open a CSV file to store the received values
csv_file = open('arduino_data.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Received Values'])  # Write header

# Send "1" to start the program on Arduino
arduino.write(b'1')

# Receive and store values until timeout
while True:
    received_data = arduino.readline().decode().strip()
    if received_data:
        print(f"Received: {received_data}")
        csv_writer.writerow([received_data])  # Write data to CSV file
    else:
        break  # Break the loop when no more data is received

# Close the CSV file and serial connection
csv_file.close()
arduino.close()


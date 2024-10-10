import serial
import time

ser = serial.Serial('COM3', 9600, timeout=1) 


time.sleep(2) 


ser.flushInput()
ser.flushOutput()


ser.write(b'Hello Arduino!\n')
print("Message sent to Arduino.")


time.sleep(2)


while True:
    if ser.in_waiting > 0:
        response = ser.readline().decode().strip()
        print(f"Received from Arduino: {response}")
        break 


ser.close()

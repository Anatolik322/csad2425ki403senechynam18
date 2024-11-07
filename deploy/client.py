import serial
import time
import tkinter as tk
from tkinter import messagebox

ser = serial.Serial('COM3', 9600, timeout=1) 
time.sleep(2)  

ser.flushInput()
ser.flushOutput()

def send_choice(choice):
    """Send player's choice to Arduino and wait for the result."""
    try:
        ser.write(f'{choice}\n'.encode())  
        print(f"Sent to Arduino: {choice}")

        start_time = time.time()
        response = ""
        while time.time() - start_time < 3:  
            if ser.in_waiting > 0:
                response = ser.readline().decode().strip()
                break
            time.sleep(0.1)  # Small delay to avoid excessive CPU usage

        if response:
            print(f"Received from Arduino: {response}")
            display_result(response)
        else:
            print("No response received from Arduino.")
            display_result("No response received. Try again.")
    except Exception as e:
        print(f"Error: {e}")

def display_result(result):
    """Show game result in a message box."""
    messagebox.showinfo("Game Result", f"{result}")

window = tk.Tk()
window.title("Rock-Paper-Scissors Game")
window.geometry("300x200")

btn_rock = tk.Button(window, text="Rock", command=lambda: send_choice("rock"))
btn_paper = tk.Button(window, text="Paper", command=lambda: send_choice("paper"))
btn_scissors = tk.Button(window, text="Scissors", command=lambda: send_choice("scissors"))

btn_rock.pack(pady=10)
btn_paper.pack(pady=10)
btn_scissors.pack(pady=10)

window.mainloop()

ser.close()

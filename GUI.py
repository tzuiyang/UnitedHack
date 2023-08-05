import tkinter as tk
from tkinter import messagebox
import time
import threading

def set_alarm():
    alarm_time = entry.get()
    try:
        alarm_time = time.strptime(alarm_time, "%H:%M")
        current_time = time.localtime()

        # Calculate the time difference between current time and alarm time
        time_diff = (
            alarm_time.tm_hour - current_time.tm_hour
        ) * 3600 + (alarm_time.tm_min - current_time.tm_min) * 60

        # If the alarm time is in the past, add 24 hours to the time difference
        if time_diff < 0:
            time_diff += 24 * 3600

        # Start the alarm after the calculated time difference
        threading.Timer(time_diff, ring_alarm).start()

        message = f"Alarm set for {time.strftime('%H:%M', alarm_time)}"
        messagebox.showinfo("Alarm Set", message)

    except ValueError:
        messagebox.showerror("Error", "Invalid time format. Please use HH:MM format (24-hour clock).")

def ring_alarm():
    messagebox.showinfo("Break Alarm", "Time for break, go do ten pushups!!!! I'll be watching!!!")

# Create the main application window
root = tk.Tk()
root.title("Break Alarm")
root.geometry('600x400')

# Create a label and an entry field for setting the alarm time
label = tk.Label(root, text="Set Break Alarm Time (HH:MM):")
label.pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

# Create a button to set the alarm
set_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_button.pack(pady=10)

# Start the main event loop
root.mainloop()


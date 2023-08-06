import tkinter as tk
from tkinter import ttk, messagebox
import time
import threading
import random

# A list of jokes to choose from
jokes = [
    ("Why don't scientists trust atoms?", "Because they make up everything!"),
    ("What's orange and sounds like a parrot?", "A carrot!"),
    ("Why do we never tell secrets on a farm?", "Because the potatoes have eyes and the corn has ears."),
    ("How do you catch a squirrel?", "Climb up in a tree and act like a nut!"),
    ("Why did the scarecrow win an award?", "Because he was outstanding in his field!"),
]

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
    messagebox.showinfo("Break Alarm", "Time for a break, go do ten pushups! I'll be watching!!!")

    # Get a random joke from the list and display it
    joke = random.choice(jokes)
    messagebox.showinfo("Joke Time", f"{joke[0]}\n{joke[1]}")

# Create the main application window
root = tk.Tk()
root.title("Break Alarm")
root.geometry('400x200')
root.configure(bg='pink')

# Create a custom bold font for the label text
label_font = ("Arial", 16, "bold")

# Create a label with bold and bigger font and pink background
label_text = "Set Break Alarm Time (HH:MM):"
label = tk.Label(root, text=label_text, font=label_font, bg='pink')
label.pack(pady=10)

# Create an entry field for setting the alarm time
entry = tk.Entry(root, bg='sky blue')
entry.pack(pady=5)

# Create a round and yellow "Set Alarm" button
button_style = ttk.Style()
button_style.configure('Round.TButton',  background='yellow')
set_button = ttk.Button(root, text="Set Alarm", command=set_alarm, style='Round.TButton')
set_button.pack(pady=10)

# Start the main event loop
root.mainloop()

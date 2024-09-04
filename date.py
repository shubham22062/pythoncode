import tkinter as tk
import time
from datetime import datetime

# Function to update the time and date
def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    current_date = datetime.now().strftime("%A, %B %d, %Y")
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    time_label.after(1000, update_time)

# Set up the main application window
root = tk.Tk()
root.title("Date and Time")
root.geometry("400x200")
root.configure(bg="black")

# Create and configure time label
time_label = tk.Label(root, font=("Helvetica", 48), fg="cyan", bg="black")
time_label.pack(pady=20)

# Create and configure date label
date_label = tk.Label(root, font=("Helvetica", 24), fg="white", bg="black")
date_label.pack(pady=10)

# Initialize the update_time function
update_time()

# Start the Tkinter event loop
root.mainloop()

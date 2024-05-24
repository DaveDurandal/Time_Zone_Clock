import tkinter as tk
from datetime import datetime, timezone, timedelta

# Function to update the time
def update_time():
    current_utc_time = datetime.now(timezone.utc).strftime('%b %d -- %H:%M:%S')
    current_pacific_time = (datetime.now(timezone(timedelta(hours=-7))).strftime('%b %d -- %H:%M'))
    current_mst_time = (datetime.now(timezone(timedelta(hours=-6))).strftime('%b %d -- %H:%M'))
    current_cst_time = (datetime.now(timezone(timedelta(hours=-5))).strftime('%b %d -- %H:%M'))
    current_est_time = (datetime.now(timezone(timedelta(hours=-4))).strftime('%b %d -- %H:%M'))
    utc_label['text'] = f"UTC Time: {current_utc_time}"
    pacific_label['text'] = f"Pacific Time: {current_pacific_time}"
    mst_label['text'] = f"Mountain Time: {current_mst_time}"
    cst_label['text'] = f"Central Time: {current_cst_time}"
    est_label['text'] = f"Eastern Time: {current_est_time}"
    root.after(1000, update_time)  # Update time every 1000 milliseconds (1 second)

# Creating the main window
root = tk.Tk()
root.title("Time Zones")
root.configure(bg='black')  # Set background color to black

# Create label for UTC time
utc_label = tk.Label(root, font=('Arial', 20), fg='red', bg='black')
utc_label.pack(padx=25, pady=15)

# Create label for Pacific time
pacific_label = tk.Label(root, font=('Arial', 18), fg='grey', bg='black')
pacific_label.pack(padx=25, pady=15)

# Create label for Mountain time
mst_label = tk.Label(root, font=('Arial', 20), fg='red', bg='black')
mst_label.pack(padx=25, pady=15)

# Create label for Central time
cst_label = tk.Label(root, font=('Arial', 18), fg='grey', bg='black')
cst_label.pack(padx=25, pady=15)

# Create label for Eastern time
est_label = tk.Label(root, font=('Arial', 18), fg='grey', bg='black')
est_label.pack(padx=25, pady=15)


# Initial call to update_time to start displaying time
update_time()

# Start the main loop
root.mainloop()
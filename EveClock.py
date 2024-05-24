import tkinter as tk
from datetime import datetime, timezone, timedelta

# Function to update the time
def update_time():
    # Get the current time in UTC
    current_utc_time = datetime.now(timezone.utc).strftime('%b %d %Y %H:%M:%S')

    # Convert UTC time to different time zones
    pacific_time = (datetime.now(timezone(timedelta(hours=-7)))).strftime('%b %d %Y %H:%M')
    mountain_time = (datetime.now(timezone(timedelta(hours=-6)))).strftime('%b %d %Y %H:%M')
    central_time = (datetime.now(timezone(timedelta(hours=-5)))).strftime('%b %d %Y %H:%M')
    eastern_time = (datetime.now(timezone(timedelta(hours=-4)))).strftime('%b %d %Y %H:%M')

    # Update the labels with adjusted spaces
    utc_label['text'] = f"UTC Time: {current_utc_time}"
    pacific_label['text'] = f"Pacific Time: {pacific_time}"
    mst_label['text'] = f"Mountain Time: {mountain_time}"
    cst_label['text'] = f"Central Time: {central_time}"
    est_label['text'] = f"Eastern Time: {eastern_time}"

    # Move the square
    move_square()

    root.after(50, update_time)  # Update time every 50 milliseconds

# Function to move the square
def move_square():
    global direction

    x1, y1, x2, y2 = canvas.coords(square)

    # Check if the square has reached the right edge
    if x2 >= canvas.winfo_width():
        direction = -1  # Move to the left
    # Check if the square has reached the left edge
    elif x1 <= 0:
        direction = 1  # Move to the right

    canvas.move(square, 5 * direction, 0)  # Move in the current direction

# Creating the main window
root = tk.Tk()
root.title("Time Zones and Moving Square")
root.configure(bg='black')  # Set background color to black

# Create labels for displaying time with increased padding between rows
utc_label = tk.Label(root, font=('Arial', 18), fg='red', bg='black')
utc_label.pack(pady=10)
pacific_label = tk.Label(root, font=('Arial', 14), fg='red', bg='black')
pacific_label.pack(pady=10)
mst_label = tk.Label(root, font=('Arial', 20), fg='red', bg='black')
mst_label.pack(pady=10)
cst_label = tk.Label(root, font=('Arial', 14), fg='red', bg='black')
cst_label.pack(pady=10)
est_label = tk.Label(root, font=('Arial', 14), fg='red', bg='black')
est_label.pack(pady=10)

# Create a canvas for drawing
canvas = tk.Canvas(root, width=300, height=55, bg='grey')
canvas.pack()

# Create a square on the canvas
square = canvas.create_rectangle(1, 5, 50, 50, fill='blue')

# Initial direction of movement
direction = 1  # Start by moving to the right

# Initial call to update_time to start displaying time
update_time()

# Start the main loop
root.mainloop()

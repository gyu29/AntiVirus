import tkinter as tk
from tkinter import filedialog, messagebox
import os
from PIL import Image, ImageTk, ImageSequence

# Function to scan a file for viruses
def scan_file(file_path):
    with open(file_path, "rb") as f:
        file_content = f.read()
        virus_signature = rb"X50!P%@AP[4\PZX54(P^)7CC)7}$ESPRIT-"
        if virus_signature in file_content:
            return "Detected"
        else:
            return "Undetected"

def scan_directory():
    directory = directory_entry.get()
    
    if os.path.exists(directory):
        if os.path.isfile(directory):
            result = scan_file(directory)
            messagebox.showinfo("Antivirus Result", result)
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid file path.")
    else:
        messagebox.showerror("Invalid Directory", "The input directory is invalid.")
        directory_entry.delete(0, tk.END)



# Function to update the splash screen animation
def update_splash_screen():
    try:
        img = next(animation_iterator)
        img = ImageTk.PhotoImage(img)
        splash_label.config(image=img)
        splash_label.image = img
        root.after(25, update_splash_screen)  # Schedule the next update after 25 milliseconds
    except StopIteration:
        transition_to_main_screen()  # Animation is finished, transition to the main screen

# Create the main window
root = tk.Tk()
root.title("Antivirus")

# Set the window size and position it in the center of the screen
window_width = 800
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Load and display splash screen animation
animation_iterator = iter(ImageSequence.Iterator(Image.open('assets/load.gif')))
splash_label = tk.Label(root)
splash_label.place(relx=0.5, rely=0.2, anchor="center")
update_splash_screen()  # Start the animation

# Create and place description label, text box, and scan button (initially hidden)
directory_label = tk.Label(root, text="Enter File/Folder Directory:", font=("Helvetica", 12), bg="white")
directory_entry = tk.Entry(root, font=("Helvetica", 12))
scan_button = tk.Button(root, text="Scan", font=("Helvetica", 12), command=scan_directory)

# Function to transition from splash screen to main screen
def transition_to_main_screen():
    splash_label.place_forget()  # Remove splash screen elements
    # background_label.place(relwidth=1, relheight=1)  # Show the background image
    
    # Show the description label, text box, and scan button
    directory_label.place(relx=0.5, rely=0.35, anchor="center")
    directory_entry.place(relx=0.5, rely=0.45, relwidth=0.5, anchor="center")
    scan_button.place(relx=0.5, rely=0.55, anchor="center")

# Set background image
background_image = tk.PhotoImage(file="assets/background.png")
background_label = tk.Label(root, image=background_image)

# Hide the elements initially
directory_label.place_forget()
directory_entry.place_forget()
scan_button.place_forget()

root.mainloop()

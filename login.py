import tkinter as tk
from tkinter import messagebox

# Function to verify the login credentials
def verify_login():
    username = entry_username.get()
    password = entry_password.get()

   
    if username == "Wadhwa30" and password == "Password123":
        messagebox.showinfo("Congratulation", "You have successfully logged in!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password!")

# Create the main window
root = tk.Tk()
root.title("Login Page")
root.geometry("300x200")

# Create and place the username label and entry field
label_username = tk.Label(root, text="Username:")
label_username.pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

# Create and place the password label and entry field
label_password = tk.Label(root, text="Password:")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*")  # The password will be hidden
entry_password.pack(pady=5)

# Create and place the login button
login_button = tk.Button(root, text="Login", command=verify_login)
login_button.pack(pady=20)

# Run the application
root.mainloop()

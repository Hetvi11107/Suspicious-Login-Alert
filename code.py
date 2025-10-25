import tkinter as tk
from tkinter import messagebox
import datetime
import requests

def get_location():
    try:
        res = requests.get('http://ipinfo.io')
        data = res.json()
        country = data.get('country', 'unknown')
        ip = data.get('ip', 'N/A')
        return country, ip
    except:
        return "unknown", "N/A"

def check_login():
    username = entry_username.get().strip()
    password = entry_password.get().strip()

    correct_username = "admin"
    correct_password = "password123"
    normal_country = 'India'
    normal_hours = range(7,1)  # 7 AM to 1 PM

    if username == correct_username and password == correct_password:
        now = datetime.datetime.now()
        current_hour = now.hour
        current_country, current_ip = get_location()

        if current_country != normal_country or current_hour not in normal_hours:
            messagebox.showwarning(
                title="Suspicious Login",
                message=f"Login from {current_country} at {current_hour}:00\nIP: {current_ip}"
            )
        else:
            messagebox.showinfo(title="Login Successful", message="Welcome again!")
    else:
        messagebox.showerror(title="Error", message="Invalid username or password")

# GUI setup
root = tk.Tk()
root.title("Suspicious Login Detector")
root.geometry("350x200")

tk.Label(root, text="Username:").pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="Password:").pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack()

tk.Button(root, text="Login", command=check_login).pack(pady=20)

root.mainloop()






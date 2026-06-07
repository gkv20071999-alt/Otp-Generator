import random
import tkinter as tk
from tkinter import messagebox

# OTP Generator Function
def otp_generator(length):
    digit = "0123456789"
    s = ""

    for i in range(length):
        s += random.choice(digit)

    return s


# Generate OTP Function
def generate_otp():
    length = entry.get()

    if length.isdigit() and int(length) > 0:
        otp = otp_generator(int(length))
        result_label.config(text=otp)
    else:
        messagebox.showerror("Error", "Enter valid OTP length")


# Copy OTP Function
def copy_otp():
    otp = result_label.cget("text")

    if otp != "":
        root.clipboard_clear()
        root.clipboard_append(otp)
        messagebox.showinfo("Copied", "OTP copied successfully")
    else:
        messagebox.showwarning("Warning", "Generate OTP first")


# Clear Function
def clear_data():
    entry.delete(0, tk.END)
    result_label.config(text="")


# Main Window
root = tk.Tk()
root.title("OTP Generator")
root.geometry("400x350")
root.config(bg="lightblue")

# Heading
title = tk.Label(
    root,
    text="OTP Generator",
    font=("Arial", 22, "bold"),
    bg="lightblue",
    fg="darkblue"
)
title.pack(pady=20)

# Enter Length
label = tk.Label(
    root,
    text="Enter OTP Length",
    font=("Arial", 14),
    bg="lightblue"
)
label.pack()

# Entry Box
entry = tk.Entry(
    root,
    font=("Arial", 16),
    justify="center"
)
entry.pack(pady=10)

# Generate Button
generate_btn = tk.Button(
    root,
    text="Generate OTP",
    font=("Arial", 14, "bold"),
    bg="green",
    fg="white",
    command=generate_otp
)
generate_btn.pack(pady=10)

# OTP Result
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 20, "bold"),
    bg="white",
    fg="red",
    width=15
)
result_label.pack(pady=20)

# Copy Button
copy_btn = tk.Button(
    root,
    text="Copy OTP",
    font=("Arial", 12),
    bg="orange",
    command=copy_otp
)
copy_btn.pack(pady=5)

# Clear Button
clear_btn = tk.Button(
    root,
    text="Clear",
    font=("Arial", 12),
    bg="red",
    fg="white",
    command=clear_data
)
clear_btn.pack(pady=5)

# Run GUI
root.mainloop()
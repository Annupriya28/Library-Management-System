import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Connect to MySQL Database
conn = mysql.connector.connect(
    host="000.0.0.0",
    user="abc",  # Change this if you have a different username
    password="xxxxxxx",  # Replace with your MySQL password
    database="library_management"
)
cursor = conn.cursor()


# Function to Issue a Book
def issue_book():
    book_id = book_id_entry.get()
    user = user_entry.get()

    if book_id and user:
        try:
            query = "INSERT INTO issue_books (book_id, issued_to) VALUES (%s, %s)"
            cursor.execute(query, (book_id, user))
            conn.commit()
            messagebox.showinfo("Success", "Book issued successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"MySQL Error: {err}")
    else:
        messagebox.showerror("Error", "Please enter Book ID and User!")


# Function to Add a Book
def add_book():
    title = title_entry.get()
    author = author_entry.get()
    year = year_entry.get()

    if title and author and year:
        try:
            query = "INSERT INTO books (title, author, year) VALUES (%s, %s, %s)"
            cursor.execute(query, (title, author, year))
            conn.commit()
            messagebox.showinfo("Success", "Book added successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"MySQL Error: {err}")
    else:
        messagebox.showerror("Error", "Enter all book details!")


# GUI Window
root = tk.Tk()
root.title("Library Management System")
root.geometry("400x300")

# Labels and Entry Fields
tk.Label(root, text="Book ID:").grid(row=0, column=0)
book_id_entry = tk.Entry(root)
book_id_entry.grid(row=0, column=1)

tk.Label(root, text="Issued To (User):").grid(row=1, column=0)
user_entry = tk.Entry(root)
user_entry.grid(row=1, column=1)

tk.Label(root, text="Book Title:").grid(row=2, column=0)
title_entry = tk.Entry(root)
title_entry.grid(row=2, column=1)

tk.Label(root, text="Author:").grid(row=3, column=0)
author_entry = tk.Entry(root)
author_entry.grid(row=3, column=1)

tk.Label(root, text="Year:").grid(row=4, column=0)
year_entry = tk.Entry(root)
year_entry.grid(row=4, column=1)

# Buttons
issue_button = tk.Button(root, text="Issue Book", command=issue_book)
issue_button.grid(row=5, column=0, columnspan=2)

add_button = tk.Button(root, text="Add Book", command=add_book)
add_button.grid(row=6, column=0, columnspan=2)

# Run GUI
root.mainloop()

# Close MySQL Connection
conn.close()
